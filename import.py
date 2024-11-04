import subprocess
import sys

a=["mss","Image","PIL"]

def install(name):
    subprocess.call([sys.executable, '-m', 'pip', 'install', name])

for i in a:
    install(i)