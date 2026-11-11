"""Start a temporary local TensorBoard server, check HTTP, then shut it down."""
from pathlib import Path
import subprocess
import sys
import time
import urllib.request

folder = Path(__file__).resolve().parents[1]
command = [sys.executable, '-m', 'tensorboard.main', '--logdir', str(folder / 'runs'),
           '--host', '127.0.0.1', '--port', '6006', '--load_fast', 'false']
with (folder / 'outputs/tensorboard-server.txt').open('w') as log:
    log.write('$ ' + ' '.join(command) + '\n')
    log.flush()
    process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
    try:
        for attempt in range(90):
            if process.poll() is not None:
                raise RuntimeError(f'TensorBoard exited: {process.returncode}; see server log')
            try:
                with urllib.request.urlopen('http://127.0.0.1:6006/', timeout=1) as response:
                    assert response.status == 200
                    print('TensorBoard local HTTP status:', response.status)
                    log.write('HTTP check: 200\n')
                    break
            except OSError:
                time.sleep(1)
        else:
            raise TimeoutError('TensorBoard did not start within 90 seconds')
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        log.write('Temporary server shut down.\n')
