from osUtils import *
from random import randint

def validateConfigs(validationDict):
    valuesList = validationDict.values()
    if not None in valuesList:
        validationDict["configMade"] = True
    else:
        validationDict["configMade"] = False
    
    return validationDict

def validateCandidateNumber(myList, myNumber):
    valuesList = list()
    for each in myList:
        valuesList.append(each["candidateNumber"])
    if not myNumber in valuesList:
        return True
    else:
        return False
        

def configExists():
    myBool = pathExists("config.json")
    if not myBool:
        open("config.json", "a")
    return myBool

def configStart():
    configDict = dict({
        "theme" : None,
        "candidates" : None,
        "configMade" : False
    })
    candidatesList = list()
    while 1:
        configDict = validateConfigs(configDict)
        clearScreen()
        configScreen(configDict["configMade"])
        decisionInput = input("Digite a opção desejada: ")
        match decisionInput:
            case "1":
                clearScreen()
                print("Configurar o tema de votação")
                print()
                print("0 - Voltar à tela principal")
                caseInput = input("Digite o tema da votação: ")
                if caseInput == "0":
                    continue
                else:
                    configDict["theme"] = caseInput
            case "2":
                candidatesLister = False if len(candidatesList) == 0 else True
                clearScreen()
                print("Configurar os candidatos")
                print()
                print("0 - Voltar à tela principal")
                print("1 - Listar candidatos") if not candidatesLister else None
                print("2 - Inserir candidato")
                print("3 - Remover candidato")
                print()
                caseInput = input("Digite a opção escolhida: ")
                match caseInput: 
                    case "1":
                        clearScreen()
                        printCandidates() if candidatesLister else print("Não tem candidatos inscritos!")
                        delayScreen(5)
                    case "2":
                        clearScreen()
                        candidateName = input("Digite o nome do candidato: ")
                        candidateNumber = input("Digite o número do candidato: ")
                        if not validateCandidateNumber:
                            print("Número de candidato já existente!")
                            delayScreen(1)
                            continue
                        print(f"Número para votação do candidato '{candidateName}': {candidateNumber}")
                        print()
                        candidateConfirm = input("Digite S para confirmar a inserção do candidato: ")
                        if candidateConfirm.upper() == "S":
                            candidatesList.append({"candidateName" : candidateName,
                                                    "candidateNumber" : candidateNumber
                                                    })
                            configDict["candidates"] = candidatesList
                        else:
                            print("Candidatura cancelada!")
                            delayScreen(1)
                            continue
            case "6":
                break
    print(configDict)

def configScreen(configsMade):
    print("Configurações da Urna Eletrônica")
    print()
    print(" 1 - Configurar o tema de votação")
    print(" 2 - Configurar os candidatos")
    print(" 3 - Configurar o período de votação")
    print(" 4 - Confirmar a necessidade de validação de CPF")
    print(" 5 - Usar configuração existente")
    print(" 6 - Finalizar configuração") if configsMade else None
    print()

def printCandidates(listOfCandidates):
    for each in listOfCandidates:
        print(each)
        print()
