from osUtils import *

def validateConfigs(validationDict):
    valuesList = validationDict.values()
    if not None in valuesList:
        validationDict["configMade"] = True
    else:
        validationDict["configMade"] = False
    
    return validationDict
        

def configExists():
    myBool = pathExists("config.json")
    if not myBool:
        open("config.json", "a")
    return myBool

def configStart():
    configDict = dict({
        "theme" : None,
        "candidatos" : None,
        "configMade" : False
    })
    candidatosList = list()
    while 1:
        configDict = validateConfigs(configDict)
        clearScreen()
        configScreen(configDict["configMade"])
        decisionInput = input("Digite a opção desejada: ")
        match decisionInput:
            case "1":
                print("Configurar o tema de votação")
                print()
                print("0 - Voltar à tela principal")
                caseInput = input("Digite o tema da votação: ")
                if caseInput == "0":
                    continue
                else:
                    configDict["theme"] = caseInput
            case "2":
                print("Configurar os candidatos")
                print()
                print("0 - Voltar à tela principal")
                if len(candidatosList) == 0 : print("1 - Listar candidatos")
                print("2 - Inserir candidato")
                print("3 - Remover candidato")
                print()


def configScreen(configsMade):
    print("Configurações da Urna Eletrônica")
    print()
    print(" 1 - Configurar o tema de votação")
    print(" 2 - Configurar os candidatos")
    print(" 3 - Configurar o período de votação")
    print(" 4 - Confirmar a necessidade de validação de CPF")
    if configsMade : print(" 5 - Finalizar configuração")
    print()


