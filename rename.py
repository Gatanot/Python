import os, shutil

print("enter folder address: ")
address=str(input())
print(os.getcwd())
os.chdir(address)
print("enter file suffixes: ")
suffixes=str(input())
index = 0
for filename in os.listdir(address):
    index += 1
    newname = str(index) + "."+suffixes
    absWorkingDir = os.path.abspath(
        address
    )
    filename = os.path.join(absWorkingDir, filename)
    newname = os.path.join(absWorkingDir, newname)
    print('Rename "%s" to "%s"...' % (filename, newname))
    shutil.move(filename, newname)
print(os.getcwd())
