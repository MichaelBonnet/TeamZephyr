## USED FOR TESTING PURPOSES
import os
import subprocess

cmd = ''
while cmd != 'quit':
  curr_dir = os.getcwd()
  cmd = input(curr_dir + '>')
  try:
    subprocess.run(cmd)
  except:
    # do something here
    i = 0
