#Bibliotecas usadas no código
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date

#Arquivo com as funções utilizadas
from funcoes import *

#Criação do PDF e do nome do arquivo
touch = canvas.Canvas("Relatorio.pdf")

#Puxando as datas atuais direto da Web
mes = date.today().month 
ano = date.today().year

#Criando a variável mês anterior, utilizada no cabeçalho do relatório.
mesanterior = mes - 1

#Taxa atual da consultoria Next Capital.
taxanext = 15

#Captura do nome do cliente e chamado a função.
nome = input("Insira o nome do cliente: ")
tabelagerada = buscaindice(nome)

#A função retorna duas saídas o que faz da variavél tabela gerada uma lista com dois índices: aplicação e dia de recebimento dos dividendos.
aplicacao = tabelagerada[0]
dia = tabelagerada[1]

#Captura o rendimento percentual do mês
porcentagem = int(input("Insira a porcentagem que será aplicada:"))

#Cálculo do lucro bruto apartir da carteira atual + a porcentagem mensal.
rendimentobruto = rendimento(aplicacao,porcentagem)

#Calcula-se o valor da taxa de consultoria apartir do lucro bruto mensal e o subtrai do lucro bruto, gerando o lucro líquido.
taxaconsultoria = taxanxt(rendimentobruto,taxanext)

#Lucro líquido: Subtrai-se a taxa da consultoria do saldo bruto.
lucroliquido = lucroliqui(rendimentobruto,taxaconsultoria)

#Váriavel que adiciona o lucro líquido mensal ao valor da carteira antes dele.
carteiraantesdaretirada = afterretirada(aplicacao, rendimentobruto, taxaconsultoria)

#Recebe a informação de se o cliente retirou algo.
retirada= float(input("O cliente quer retirar alguma quantia, se sim qual?"))

#Temos o saldo final após o tratamento das iformações.
saldofinal = beforeretirada(carteiraantesdaretirada, retirada)

print('R$%.2f' %rendimentobruto)
print(taxaconsultoria)
print(carteiraantesdaretirada)
print(retirada)
print(saldofinal)

#----------------------------------------

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
#touch.drawImage("ass.png", mm_to_cm(6) ,mm_to_cm(2), mask='auto', width=250, height=160)


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
