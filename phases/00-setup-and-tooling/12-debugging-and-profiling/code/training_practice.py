"""CPU training, injected NaNs, profiling and TensorBoard exercise runner."""
import argparse
import json
from pathlib import Path
import time
import tracemalloc

import torch
from torch import nn
from torch.utils.tensorboard import SummaryWriter
from debug_tools import check_shapes, check_devices, debug_print, detect_nan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    torch.manual_seed(7)
    torch.set_num_threads(1)
    output = Path(__file__).resolve().parents[1] / 'outputs'
    logdir = Path(__file__).resolve().parents[1] / 'runs' / 'overfit'
    tracemalloc.start()
    started = time.perf_counter()
    x = torch.randn(12, 8)
    y = torch.randn(12, 1)
    val_x = torch.randn(128, 8)
    val_y = torch.randn(128, 1)
    loading_seconds = time.perf_counter() - started
    # Random independent targets deliberately expose memorization of a tiny set.
    model = nn.Sequential(nn.Linear(8, 64), nn.Tanh(), nn.Linear(64, 1))
    optimizer = torch.optim.Adam(model.parameters(), lr=0.03)
    criterion = nn.MSELoss()
    check_shapes(model, x)
    check_devices(model, x, y)
    debug_print('training inputs', x)
    history = []
    forward_seconds = backward_seconds = 0.0
    with SummaryWriter(str(logdir)) as writer:
        for step in range(300):
            optimizer.zero_grad(set_to_none=True)
            started = time.perf_counter()
            prediction = model(x)
            loss = criterion(prediction, y)
            forward_seconds += time.perf_counter() - started
            started = time.perf_counter()
            loss.backward()
            if args.debug and step == 0:
                breakpoint()  # Inspect x.shape, x.device, model[0].weight.grad.
            optimizer.step()
            backward_seconds += time.perf_counter() - started
            with torch.no_grad():
                validation_loss = criterion(model(val_x), val_y).item()
            history.append({'step': step, 'train': loss.item(), 'validation': validation_loss})
            writer.add_scalar('loss/train', loss.item(), step)
            writer.add_scalar('loss/validation', validation_loss, step)
            if step % 50 == 0:
                for name, param in model.named_parameters():
                    writer.add_histogram('weights/' + name, param, step)
                    writer.add_histogram('gradients/' + name, param.grad, step)
    # Inject 0/0 in a separate model so the useful run is not corrupted.
    class BrokenModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.layer = nn.Linear(8, 1)

        def forward(self, inputs):
            result = self.layer(inputs)
            return (result - result) / 0.0

    broken = BrokenModel()
    bad_loss = criterion(broken(x), y)
    bad_loss.backward()
    assert detect_nan(broken, bad_loss, 0), 'Injected NaN was not detected'
    print('Top Python allocations (tensor storage is not included):')
    for stat in tracemalloc.take_snapshot().statistics('lineno')[:5]:
        print(stat)
    tracemalloc.stop()
    (output / 'training-history.json').write_text(json.dumps(history, indent=2) + '\n')
    print('First epoch:', history[0])
    print('Last epoch:', history[-1])
    print('Measured loading / forward / backward+update seconds:',
          loading_seconds, forward_seconds, backward_seconds)
    print('Overfitting pattern:', history[-1]['train'] < history[0]['train']
          and history[-1]['validation'] > history[0]['validation'])
    print('CUDA available:', torch.cuda.is_available())
    print('TensorBoard event directory:', logdir)


if __name__ == '__main__':
    main()
