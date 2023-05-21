from osUtils import *
from dateUtils import *

configDict = dict({
        "theme" : None,
        "candidates" : None,
        "votingPeriod" : None,
        "configMade" : False
})
candidatesList = list()

def validateConfigs():
    valuesList = list(configDict.values())
    if (not None in valuesList) and ([] not in valuesList):
        configDict["configMade"] = True
    else:
        configDict["configMade"] = False
    return configDict

def validateCandidateNumber(myNumber):
    valuesList = list()
    for each in candidatesList:
        valuesList.append(each["number"])
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
    while 1:
        configDict = validateConfigs()
        clearScreen()
        configScreen()
        decisionInput = input("Digite a opção desejada: ")
        match decisionInput:
            case "1":
                configTheme()
            case "2":
                configCandidates()
            case "3":
                configPeriod()
                break
            case "6":
                break # Implementar método de teste com configsMade
    print(configDict)

def configScreen():
    print("Configurações da Urna Eletrônica")
    print()
    print(" 1 - Configurar o tema de votação")
    print(" 2 - Configurar os candidatos")
    print(" 3 - Configurar o período de votação")
    print(" 4 - Confirmar a necessidade de validação de CPF")
    print(" 5 - Usar configuração existente")
    print(" 6 - Finalizar configuração") if configDict["configMade"] else None
    print()


def configTheme():
    clearScreen()
    print("Configurar o tema de votação")
    print()
    print("0 - Voltar à tela principal")
    caseInput = input("Digite o tema da votação: ")
    if caseInput == "0":
        return 0
    else:
        configDict["theme"] = caseInput

def configCandidates():
    configDict["candidates"] = candidatesList
    candidatesLister = False if len(candidatesList) == 0 else True
    clearScreen()
    print("Configurar os candidatos")
    print()
    print("0 - Voltar à tela principal")
    print("1 - Listar candidatos")
    print("2 - Inserir candidato")
    print("3 - Remover candidato")
    print()
    caseInput = input("Digite a opção escolhida: ")
    match caseInput: 
        case "1":
            printCandidates() if candidatesLister else print("Não tem candidatos inscritos!")
            delayScreen(2)
        case "2":
            insertCandidate()
        case "3":
            removeCandidate()

def printCandidates():
    clearScreen()
    for each in candidatesList:
        print(each)
        print()
    delayScreen(1 * len(candidatesList) - 1)

def insertCandidate():
    clearScreen()
    candidateName = input("Digite o nome do candidato: ")
    candidateNumber = input("Digite o número do candidato: ")
    if not validateCandidateNumber(candidateNumber):
        print("Número de candidato já existente!")
        delayScreen(1)
        return 0
    print(f"Número para votação do candidato '{candidateName}': {candidateNumber}")
    print()
    candidateConfirm = input("Digite S para confirmar a inserção do candidato: ")
    if candidateConfirm.upper() == "S":
        candidatesList.append({"name" : candidateName, "number" : candidateNumber})
    else:
        print("Candidatura cancelada!")
        delayScreen(1)
        return 0
    
def removeCandidate():
    clearScreen()
    candidateName = input("Digite o nome do candidato a ser removido: ")
    candidate = searchCandidate(candidateName)
    if candidate != False:
        print("O nome do candidato a ser excluído é: ", candidate["name"])
        print("O número do candidato a ser excluído é: ", candidate["number"])
        print()
        confirmNumber = input("Para confirmar a exclusão do candidato, digite seu número de candidatura: ")
        if candidate["number"] == confirmNumber:
            candidatesList.remove(candidate)
        else:
            print("Remoção do candidato cancelada!")
            delayScreen(1.5)
    else:
        print("Candidato Inexistente!")
        delayScreen(1.5)

def searchCandidate(candidateName):
    for candidate in candidatesList:
        if candidateName == candidate["name"]:
            return candidate
        else:
            return False


def configPeriod():
    clearScreen()
    print("Configurar o período de votação")
    print()
    print(" 1 - Votação por período de tempo")
    print(" 2 - Votação por número de pessoas votantes")
    print(" 3 - Sair")
    print()
    caseInput = input("Digite a opção escolhida: ")
    match caseInput:
        case "1":
            break


def configDates():
    
