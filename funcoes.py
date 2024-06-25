import sys

#Josiane Igor, Marcos Zero, Sylei Pastor, Rose do Marco.

def buscaindice(nomeinformado):
    tabela = ["Adelmook", 5723.48, 22, "Marcosok", 32890.27, 20, "Cilsook", 71468.74, 3, "Alineok", 2000, 20, "Airanok",
    36403.07, 20, "Josianeok" , 26917.05, 19, "Siley", 14330.96, 27, "Rose", 31785, 24,
    "Jonatas Evangelista", 8523.86, 2, "Jéssica", 11000, 20, "Ana Caroline", 1000, 18, "Adélia", 5000, 18, "Joarbson", 6000, 17, "Clemente", 20000, 20]
    if nomeinformado in tabela:
        client = tabela.index(nomeinformado)
        aplicacao = tabela[client+1]
        dia = tabela[client+2]
        return aplicacao, dia
    else:
        print("Nome incorreto!")
        print("Verifique a lista e rode o programa novamente!")
        sys.exit()

def rendimento(carteira,porcentagem):
    lucro = carteira * (porcentagem/100)
    return lucro
        
def taxanxt(lucro, taxa):
    desconto =lucro * (taxa/100)
    return desconto

def lucroliqui(lucrobruto, taxa):
    lucroliquido = lucrobruto - taxa
    return lucroliquido

def afterretirada(a,b,c):
    saldobruto = a + b - c
    return saldobruto

def beforeretirada(a,b):
    retirada = a - b
    return retirada
