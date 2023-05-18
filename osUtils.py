from os import path, system

def clearScreen():
    system("clear || cls")

def pathExists(filePath):
    myBool = path.exists(filePath)
    return myBool