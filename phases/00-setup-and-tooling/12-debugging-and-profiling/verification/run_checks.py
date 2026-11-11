from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[4]
python = str(root / '.venv/bin/python')
base = root / 'phases/00-setup-and-tooling'

def run(slug, name, command, stdin=None):
    folder = base / slug
    result = subprocess.run(command, cwd=folder, input=stdin, text=True, capture_output=True, timeout=180)
    report = '$ ' + ' '.join(command) + '\n'
    if stdin:
        report += 'Scripted debugger input (agent verification, not learner practice):\n' + stdin
    report += result.stdout + result.stderr + f'\nExit code: {result.returncode}\n'
    (folder / 'outputs' / (name + '.txt')).write_text(report)
    print(slug, name, 'exit', result.returncode, flush=True)
    return result.returncode

slug = '12-debugging-and-profiling'
run(slug, 'upstream-demo', [python, 'code/debug_tools.py'])
run(slug, 'training', [python, 'code/training_practice.py'])
run(slug, 'training-cprofile', [python, '-m', 'cProfile', '-s', 'cumtime', 'code/training_practice.py'])
run(slug, 'debugger', [python, 'code/training_practice.py', '--debug'],
    'p x.shape\np x.device\np model[0].weight.grad.shape\np torch.isfinite(model[0].weight.grad).all().item()\nc\n')
run(slug, 'line-profile', [python, '-c',
    'import sys;sys.path.insert(0,"code");from line_profiler import LineProfiler;from profile_practice import load_data,score_data;p=LineProfiler(load_data,score_data);p.runcall(lambda:score_data(load_data()));p.print_stats()'])
run(slug, 'memory-profile', [python, '-c',
    'import sys;sys.path.insert(0,"code");from memory_profiler import profile;from profile_practice import load_data;values=profile(load_data)();print("Rows:",len(values))'])
run(slug, 'tensorboard-inspect', [python, '-c',
    'from tensorboard.backend.event_processing.event_accumulator import EventAccumulator;e=EventAccumulator("runs/overfit");e.Reload();print(e.Tags());t=e.Scalars("loss/train");v=e.Scalars("loss/validation");print("Train first/last:",t[0].value,t[-1].value);print("Validation first/last:",v[0].value,v[-1].value);assert len(t)>=300 and len(v)>=300;assert t[-1].value<t[0].value and v[-1].value>v[0].value'])
slug = '13-python-for-ai-engineering'
run(slug, 'exercises', [python, 'code/exercises.py'])
run(slug, 'tests', [python, '-m', 'unittest', 'discover', '-s', 'code/tests', '-v'])
run(slug, 'typescript-demo', [str(base/slug/'node_modules/.bin/tsx'), 'code/main.ts'])
run(slug, 'python-demo', [python, 'code/main.py'])
result = subprocess.run([python, '-m', 'pip', 'freeze'], capture_output=True, text=True, check=True)
for slug in ['12-debugging-and-profiling','13-python-for-ai-engineering']:
    (base/slug/'verification/environment.txt').write_text(result.stdout)
