from os import path, system
from time import sleep

def clearScreen():
    system("clear || cls")

def pathExists(filePath):
    myBool = path.exists(filePath)
    return myBool

def delayScreen(seconds):
    sleep(seconds)
