from config import *

if not configExists():
    print("Arquivo de configuração inexistente")
    print("")

configStart()
validateConfigs()