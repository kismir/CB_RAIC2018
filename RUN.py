#!/usr/bin/env python3
''' Run LR and Runner.py simultaneously'''

import subprocess
import time

# local runner start args
terminal_name = 'lxterminal'
start_arg = '-e'
lr_path = '../codeball2018-linux/codeball2018'

# Runner.py start args
python_dir = '%your_python_dir%'
#unbuffered binary stdout and stderr
python_arg = '-u'
runner_path = 'Runner.py'

p = subprocess.Popen([terminal_name, start_arg, lr_path])
time.sleep(0.5)
p1 = subprocess.Popen([python_dir, python_arg, runner_path])
