import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date
import sys

# Criar a janela principal
interface = tk.Tk()
interface.title("Gerador de PDF")

def molde_pdf(nome, porcentagem, dia, aplicacao,rendimentobruto, taxaconsultoria, lucroliquido,carteiraantesdaretirada, retirada,saldofinal):

    #Variavéis estáticas
    mes = date.today().month 
    ano = date.today().year
    #Criando a variável mês anterior, utilizada no cabeçalho do relatório.
    mesanterior = mes - 1
    #Taxa atual da consultoria Next Capital.
    taxanext = 15

    # Criar o PDF
    touch = canvas.Canvas("Relatorio.pdf")
    # Converter a medida de pontos flutuantes para centímetros.
    def mm_to_cm(cm):
        return cm / 0.352777 * 10
    
    #Adicionando Imagens

    #Next Logo
    touch.drawImage("logo.png", mm_to_cm(2) ,mm_to_cm(27), mask='auto', width=200, height=60)
    #Linha Horizontal Preta
    touch.drawImage("black.png", mm_to_cm(0) ,mm_to_cm(26), mask='auto', width=600, height=1)
    #Linha Vertical Preta
    touch.drawImage("black2.png", mm_to_cm(0) ,mm_to_cm(0), mask='auto', width=20, height=900)
    #Template Tabela
    touch.drawImage("tab1.png", mm_to_cm(5) ,mm_to_cm(17), mask='auto', width=330, height=55)
    #Assinatura
    touch.drawImage("ass.png", mm_to_cm(6) ,mm_to_cm(2), mask='auto', width=250, height=160)


    #Informações do cabeçalho

    touch.setFont('Helvetica-Oblique', 12)
    touch.drawString(mm_to_cm(15) , mm_to_cm(28.3) ,'Avenida Ário Barnabé, 1149')
    touch.drawString(mm_to_cm(15) , mm_to_cm(27.9) ,'Indaiatuba, São Paulo.')
    touch.drawString(mm_to_cm(15) , mm_to_cm(27.2) ,'(19)99881-7857')

    #Título de descrição do relatório

    touch.setFont('Helvetica-Bold', 22)
    touch.drawString(mm_to_cm(2) , mm_to_cm(24.5) ,'Relatório mensal do resultado das aplicações:')

    #Cliente

    touch.setFont('Helvetica', 14)
    touch.drawString(mm_to_cm(2) , mm_to_cm(23.9) ,'Cliente:')
    touch.setFont('Helvetica-Oblique', 14)
    touch.drawString(mm_to_cm(3.8) , mm_to_cm(23.9) ,nome)

    #Avalia os dados necessários e adiciona data ao PDF.
    if (dia < 10) & (mes < 10):
        touch.setFont('Helvetica-Bold', 18)
        touch.drawString(mm_to_cm(7.5) , mm_to_cm(21) ,'De 0'+str(dia)+'/0'+str(mesanterior)+ '/24 a 0'+str(dia)+'/0'+str(mes)+'/24')
    elif (dia < 10) & (mes > 10):
        touch.setFont('Helvetica-Bold', 18)
        touch.drawString(mm_to_cm(7.5) , mm_to_cm(21) ,'De 0'+str(dia)+'/'+str(mesanterior)+ '/24 a 0'+str(dia)+'/'+str(mes)+'/24')
    elif (dia > 10) & (mes < 10):
        touch.setFont('Helvetica-Bold', 18)
        touch.drawString(mm_to_cm(7.5) , mm_to_cm(21) ,'De '+str(dia)+'/0'+str(mesanterior)+ '/24 a '+str(dia)+'/0'+str(mes)+'/24')
    else:
        touch.setFont('Helvetica-Bold', 18)
        touch.drawString(mm_to_cm(7.5) , mm_to_cm(21) ,'De '+str(dia)+'/'+str(mesanterior)+ '/24 a '+str(dia)+'/'+str(mes)+'/24')
    #-------------------------------------------------------------------------------
    #Tab1

    #Título
    touch.setFont('Helvetica', 15)
    touch.drawString(mm_to_cm(5) , mm_to_cm(19.2) ,'Balanço mensal:')

    #Linha 1

    #Célula 1 
    touch.setFont('Helvetica-Bold', 16)
    touch.drawString(mm_to_cm(5.6) , mm_to_cm(18.3) ,'Aplicação')
    #Célula 2
    touch.setFont('Helvetica', 14)
    touch.drawString(mm_to_cm(5.9) , mm_to_cm(17.3) , 'R$' + str(aplicacao))

    #Linha 2

    #Célula 1
    touch.setFont('Helvetica-Bold', 16)
    touch.drawString(mm_to_cm(9.3) , mm_to_cm(18.3) ,'Rendimento')
    #Célula 2
    touch.setFont('Helvetica', 14)
    touch.drawString(mm_to_cm(9.35) , mm_to_cm(17.3) ,'BNB-US -' + str(porcentagem) + '%')

    #Linha 3

    #Célula 1
    touch.setFont('Helvetica-Bold', 16)
    touch.drawString(mm_to_cm(13.3) , mm_to_cm(18.3) ,'Resultado')
    #Célula 2
    touch.setFont('Helvetica', 14)
    touch.drawString(mm_to_cm(13.5) , mm_to_cm(17.3) ,'R$' + str('%.2f' %rendimentobruto))

    #-------------------------------------------------------------------------------

    #Tab2---------------------------------------------------------------------------

    #Título
    touch.setFont('Helvetica', 15)
    touch.drawString(mm_to_cm(5) , mm_to_cm(15.5) ,'Taxa da consultoria financeira:')

    #Tabela
    touch.drawImage("tab2.png", mm_to_cm(5) ,mm_to_cm(13.3), mask='auto', width=330, height=55)
    touch.setFont('Helvetica-Bold', 16)
    touch.drawString(mm_to_cm(13.3) , mm_to_cm(18.3) ,'Resultado')

    #Linha1

    #Célula1
    touch.setFont('Helvetica-Bold', 14)
    touch.drawString(mm_to_cm(5.3) , mm_to_cm(14.6) ,'Rendimento bruto')

    #Célula2
    touch.setFont('Helvetica', 14)
    touch.drawString(mm_to_cm(6.6) , mm_to_cm(13.6) ,'R$%.2f' %(rendimentobruto))

    #Linha2

    #Célula1
    touch.setFont('Helvetica-Bold', 14)
    touch.drawString(mm_to_cm(10.5) , mm_to_cm(14.6) ,'-15% Consultoria Next')

    #Célula2
    touch.setFont('Helvetica', 14)
    touch.drawString(mm_to_cm(12.5) , mm_to_cm(13.6) , 'R$%.2f' %(taxaconsultoria))

    #--------------------------------------------------------

    #Tab2.1
    touch.drawImage("tab3.png", mm_to_cm(7.5) ,mm_to_cm(12.5), mask='auto', width=170, height=25)

    #Contéudo
    touch.setFont('Helvetica-Bold', 14)
    touch.drawString(mm_to_cm(7.6) , mm_to_cm(12.8) ,'Lucro líquido:')
    touch.setFont('Helvetica', 12.6)
    touch.drawString(mm_to_cm(11) , mm_to_cm(12.8) ,'R$%.2f' %lucroliquido)

    #-------------------------------------------------------------------------
    #TAB #

    #Título
    touch.setFont("Helvetica",15)
    touch.drawString(mm_to_cm(5) , mm_to_cm(10.8) ,'Situação atual:')

    #Layout
    touch.drawImage("tab4.png", mm_to_cm(5) ,mm_to_cm(8), mask='auto', width=330, height=70)

    #Linha 1

    #Célula1
    touch.setFont('Helvetica-Bold', 15)
    touch.drawString(mm_to_cm(7.5) , mm_to_cm(9.8) ,'Saldo')
    #Célula2
    touch.setFont('Helvetica-Bold', 15)
    touch.drawString(mm_to_cm(7.2) , mm_to_cm(9) ,'Retirada')
    #Carteira
    touch.setFont('Helvetica-Bold', 15)
    touch.drawString(mm_to_cm(7.2) , mm_to_cm(8.2) ,'Carteira')

    #Linha2
    #Célula1
    touch.setFont('Helvetica', 15)
    touch.drawString(mm_to_cm(13) , mm_to_cm(9.8) ,'R$%.2f' %carteiraantesdaretirada)
    #Célula2
    touch.setFont('Helvetica', 15)
    touch.drawString(mm_to_cm(12.7) , mm_to_cm(9) ,'-')
    touch.setFont('Helvetica', 15)
    touch.drawString(mm_to_cm(13) , mm_to_cm(9) ,'R$%.2f' %retirada)
    #Carteira
    touch.setFont('Helvetica', 15)
    touch.drawString(mm_to_cm(13) , mm_to_cm(8.2) ,'R$%.2f' %saldofinal)

    #------------------------------------------------------------------------------
    #Assinatura

    touch.save()

def captura_pdf():
    nome = entry_nome.get()
    porcentagem = entry_porcentagem.get()
    retirada = entry_valor_retirado.get()
    molde_pdf(nome, porcentagem, retirada)

def dados_pdf(nome):
        tabela = ["Adelmo", 5722.50, 22, "Marcos", 32890.27, 19, "Cilso", 68336.68, 2, "Aline", 4000, 20, "Airan",
        32278.02, 20, "Josiane" , 24054,56, 19, "Siley", 14330,96, 27, "Rose", 16.785, 4,
        "Jonatas Evangelista", 8523.86, 1, "Jéssica", 10809, 19]
        if nome in tabela:
            client = tabela.index(nome)
            aplicacao = tabela[client+1]
            dia = tabela[client+2]
            return aplicacao, dia
        else:
            print("Nome incorreto!")
            print("Verifique a lista e rode o programa novamente!")
            sys.exit()

# Criar a janela principal
interface = tk.Tk()
interface.title("Gerador de PDF")

# Criar o título e define sua posição na tela
label_nome = tk.Label(interface, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10)

#Cria a caixa de texo e define sua posição na tela.
entry_nome = tk.Entry(interface)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_porcentagem = tk.Label(interface, text="Porcentagem:")
label_porcentagem.grid(row=1, column=0, padx=10, pady=10)
entry_porcentagem = tk.Entry(interface)
entry_porcentagem.grid(row=1, column=1, padx=10, pady=10)

label_valor_retirado = tk.Label(interface, text="Valor Retirado:")
label_valor_retirado.grid(row=2, column=0, padx=10, pady=10)
entry_valor_retirado = tk.Entry(interface)
entry_valor_retirado.grid(row=2, column=1, padx=10, pady=10)

#O parâmetro command define a função que será chamada quando o botão for ativado.
button_gerar_pdf = tk.Button(interface, text="Gerar PDF", command=criar_pdf)
button_gerar_pdf.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Executar o loop principal do tkinter
interface.mainloop()