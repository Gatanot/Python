import os, shutil
while(True):
    print("enter folder address: ")
    address = str(input())
    print(os.getcwd())
    os.chdir(address)
    print("enter file suffixes: ")
    suffixes = str(input())
    index = 0
    for filename in os.listdir(address):
        index += 1
        newname = ""
        if(index<10):
            newname = "00"+str(index) + "." + suffixes
        elif(index<100):
            newname = "0"+str(index) + "." + suffixes
        else:
            newname = str(index) + "." + suffixes
        absWorkingDir = os.path.abspath(address)
        filename = os.path.join(absWorkingDir, filename)
        newname = os.path.join(absWorkingDir, newname)
        print('Rename "%s" to "%s"...' % (filename, newname))
        shutil.move(filename, newname)
    print(os.getcwd())
