"""

"""
import datetime
import time
import sys
from colorama import Fore, Back, Style

try:
    valor_aporte = float(input('Valor que deseja contribuir mensalmente EM R$: '))               #| ATUALIZA O VLAOR
except ValueError:                                                                               #| DA CONTRIBUIÇÃO
    valor_aporte = float(input('Apenas numeros devem ser digitados!\n'                           #| MENSAL
                             'Tente novamente: '))                                               #|
finally:
    for char in ('OK...'):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)

try:
    valor_juros = float(input('\nDigite QUANTO PORCENTO seu investimento renderá por mês: '))    # | ATUALIZA O VLAOR
except ValueError:                                                                               # | DO JUROS MENSAL
    valor_juros = float(input('Apenas numeros devem ser digitados!\n'                            # | 
                             'Tente novamente: '))                                               # |
finally:
    for char in ('OK...'):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)

try:
    anos_contribuição = int(input('\nDigite por quantos ANOS deseja contribuir: '))                # | ATUALIZA O TEMPO
except ValueError:                                                                                 # | DE CONTRIBUIÇÃO
    anos_contribuição = int(input('Apenas numeros devem ser digitados!\n'                          # | ANUAL
                             'Tente novamente: '))                                                 # |
finally:
    for char in ('OK...'):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)

try:
    valor_ativacao_receita_federal = int(input('\nDigite o valor rendimento anual preciso para pagar IMPOSTO DE RENDA: '))
except ValueError:                                                                                # | DEFINE O VALOR
    valor_ativacao_receita_federal = int(input('Apenas numeros devem ser digitados!\n'            # | DE ATIVAÇÃO
                             'Tente novamente: '))                                                # | DA RECEITA FEDERAL
finally:
    for char in ('OK...'):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)

ver_anos = ''
try:
    ver_anos = str(input('Deseja ver o anos em que declarará IR?\n'                        # | VERIFICA SE O CLIENTE
                         'Digite "S" para SIM\n'                                           # | DESEJA VER OS ANOS EM
                         'Digite "N" para não:')).upper()                                  # | QUE SERÁ PAGO IR
except ValueError:
    ver_anos = str(input('\nAVISO: Apenas "S" ou "N" deve ser digitado!\n'
                         'Tente novamente: ')).upper()
finally:
    for char in ('OK...'):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)

juros = valor_aporte / 100 * valor_juros                                    #DEFINE O VALOR DO PRIMEIRO JUROS
meses_contribuicao = anos_contribuição * 12                                 #TRANSFORMA OS ANOS DE CONTRIBUIÇÃO EM MESES
ano = 0
contador_come_cota = 0
contador_meses = 0
somatorio_ir = 0
come_cota = 0
somatorio_come_cota = 0
valor_total = 0
rendimentos = 0
ir_pago = 0
rendimento_anual = 0
somatorio_aporte = valor_aporte
anos_ir_pago = []                                         #CRIA UMA LISTA ONDE SERÁ ARMAZENADA OS ANOS QUE O IR FOI PAGO
data_atual = datetime.date.today()

def func_come_cota():                 #DEFINE A FUNÇÃO COME COTA, PAGA PARA CORRETORA 0,1% DO VALOR TOTAL A CADA 6 MESES
    global contador_come_cota
    global come_cota
    global somatorio_come_cota
    global valor_total
    contador_come_cota = 0                #Zera a variável que estava definida com o valor do laço anterior
    come_cota = valor_total / 1000        #define 0,1% a ser subtraido do valor total
    valor_total -= come_cota              #subtrai 0,1% do valor total!
    somatorio_come_cota += come_cota      #Adiciona o valor pago no somatório para as estátisticas finais!
    #print(Back.BLACK+Fore.YELLOW+f'Come cota em ação, Valor real: {valor_total:.2f} \n {come_cota:.2f}Pago para a corretora!',Style.RESET_ALL)

def func_ir_pago():                                       #FUNÇÃO QUE PAGA O IMPOSTO DE RENDA E O SUBTRAI DO VALOR TOTAL
    global ano
    global anos_ir_pago
    global rendimento_anual
    global valor_total
    global somatorio_ir
    ir_pago = (rendimento_anual / 100) * 15   #Define o valor de 15% do rendimento anual
                                              # (APLICAVEL APENAS PARAPRODUTOS DO TESOURO DIRETO COM MAIS DE 721 DIAS DE POSSE)
    valor_total -= ir_pago                                                       #Subtrai o valor de 15% do valor total
    rendimento_anual = 0
    somatorio_ir += ir_pago                               #Adiciona o valor pago ao somário para as estatisticas finais!
    #print(Back.BLACK+Fore.RED+f'Receita federal em ação, valor real: {valor_total:.2f}, '
    #      f'\nValor pago de IR: {ir_pago:.2f}'+Style.RESET_ALL)
    anos_ir_pago.append(ano + data_atual.year)

def aniversario_investimento ():                                                               #FUNÇÃO QUE CONTA OS ANOS
    global ano
    global contador_meses
    ano += 1
    #print(Back.WHITE+Fore.LIGHTCYAN_EX+'-+-'*10,f'\n seu investimento tem {ano} anos!\n','-+-'*10,Style.RESET_ALL)
    contador_meses = 0                                                           #Zera a variável1
    if rendimento_anual >= valor_ativacao_receita_federal:                    #VERIFICA SE SERÁ TAXADO PELA RECEITA
        func_ir_pago()                                                        #CHAMA A FUNÇÃO QUE PAGA A RECEITA FEDERAL

def mostrar_anos_ir_pagos ():
    for anos in anos_ir_pago:
        print(f'Você terá pago IMPOSTO DE RENDA NOS ANOS: {anos}')

for x in range(meses_contribuicao):                     #CRIA UM LAÇO COM A QUANTIDADE DE MESES DEFINIDA PELO CLIENTE
    somatorio_aporte += valor_aporte
    juros = (valor_total / 100) * valor_juros           #DEFINE O JUROS INPUTADO PELO CLIENTE
    valor_total += valor_aporte + juros                 #ATUALIZA O  VALOR TOTAL
    contador_come_cota += 1
    contador_meses += 1
    #print(f'valor total: {valor_total:.2f}')
    #print(f'Rendimentos mensal: {juros:.2f}')
    rendimentos += juros                                             #Cria um somatório apenas com os valores de juros!
    rendimento_anual += juros
    if contador_come_cota == 6:                                      #VERIFICA SE É PERIODO DE PAGAR A CORRETORA
        func_come_cota()

    if contador_meses == 12:                                         #VERIFICA SE É PERIODO DE PAGAR A RECEITA
        aniversario_investimento()

print(Back.BLACK + Fore.GREEN + '♣♦♠♥' * 21)
time.sleep(0.3)
print(f'Ao final você terá acumulado:{valor_total:.2f}')
time.sleep(0.3)
print('_-' * 45)
time.sleep(0.25)
print(f'Juros mensal de: {juros:.2f}')
time.sleep(0.3)
print('_-' * 45)
time.sleep(0.3)
print(Fore.CYAN+f'Ao longo de {ano} anos você terá pago {somatorio_ir:.2f} de inposto de renda'
      f'\n                                   {somatorio_come_cota:.2f} de taxas administrativas!')
time.sleep(0.3)
print('_-'* 45)
time.sleep(0.3)
print(f'Você investiu um total de:{somatorio_aporte} e o juros de seus investimentos renderam: {rendimentos:.2f}')
time.sleep(0.3)
if ver_anos == ('S'):
    mostrar_anos_ir_pagos()
time.sleep(0.2)
for char in ('---------FIM---------'):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)
