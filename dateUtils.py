from datetime import date

def receiveDate():
    day, month, year = [int(x) for x in input("Digite a data de início(DD/MM/YYYY): ").split('/')]

    fullDate = date(year, month, day)

    return fullDate