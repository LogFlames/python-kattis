import random
import os
import subprocess

while True:
    N = random.randint(1,30)
    L = random.randint(1,15)
    with open("temp.data", "w+") as f:
        f.write(f'{N}\n{L}\n{" ".join([str(random.randint(1,L)) for _ in range(N)])}\n')

    a = subprocess.check_output("python lastafarjan.py < temp.data", shell=True)
    b = subprocess.check_output("python lfw.py < temp.data", shell=True)
    if a != b:
        print("what!")
        exit()

os.remove("temp.data")
