import subprocess
import os
#print(os.getcwd())


res = subprocess.run(["minizinc", "./model/solver.mzn", "./model/exampleFile.dzn"], capture_output=True)
out = res.stdout
blocks = str(out).split('\'')[1].split('=')[1].split(';')[0].split('[')[1].split(']')[0].strip().split('|')

resList = []

for i in range(1,10):
    b = blocks[i].split(' ')
    for j in range(1,9):
        resList.append(int(b[j].split(',')[0]))
    resList.append(int(b[9].split('\\')[0]))
print(len(resList))
print(resList)
for i in range(0,81):
    print(resList.pop(0))

