from osUtils import *


def configExists():
    myBool = pathExists("config.txt")
    return myBool

def configStart():
    configArchive = open("config.txt", "a")
    clearScreen()
    configScreen()

def configScreen():
    print("Configurações da Urna Eletrônica")
    print()

