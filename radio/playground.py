## USED FOR TESTING PURPOSES
import os
import subprocess
from traceback import print_exception

## Functions that are apart of the shell itself
## 1. cd
## 2. history

hist = []
cmds = ''

while cmds != 'quit':
  curr_dir = os.getcwd()
  cmds = input(curr_dir + '>')
  
  if len(cmds) > 40: 
    print('BASE ERROR: cmds are greater than 40 chars')
    continue

  try:
    output = subprocess.run(
      cmds, 
      stdout=subprocess.PIPE, 
      stderr=subprocess.STDOUT,
      shell=True,
      timeout=5
      )
    print(output.stdout.decode('utf-8'))
  except Exception:
    print_exception(Exception)