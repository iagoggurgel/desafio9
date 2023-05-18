from os import path, system

def clearScreen():
    system("clear")

def pathExists(path):
    myBool = path.exists(path)
    return myBool