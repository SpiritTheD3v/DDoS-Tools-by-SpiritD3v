import sys
import subprocess

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'colorama'])
except:
    print("error")
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])
except:
    print("error")