import random

matriz = [[1,2,3],[4,5,6],[7,8,9]]
for i in matriz: print(i)
x_ganhou = False
o_ganhou = False
vez = random.randint(1,2)
while x_ganhou or o_ganhou == False:
    op_x = 0
    if vez % 2 != 0: # Se a vez for ímpar é vez de x!

        op_x = int(input('Escolha uma opção X: '))
        op_x_linha = 0
        op_x_coluna = 0
        if op_x > 0 and op_x< 4:
            op_x_linha = 0
            if op_x == 1:
                op_x_coluna = 0
            elif op_x == 2:
                op_x_coluna = 1
            else:
                op_x_coluna = 2
        elif op_x > 3 and op_x < 7:
            op_x_linha = 1
            if op_x == 4:
                op_x_coluna = 0
            elif op_x == 5:
                op_x_coluna = 1
            else:
                op_x_coluna = 2
        elif op_x > 6 and op_x < 10:
            op_x_linha = 2
            if op_x == 7:
                op_x_coluna = 0
            elif op_x == 8:
                op_x_coluna = 1
            else:
                op_x_coluna = 2
        else:
            print('Opção ínvalida, tente novamente')
            continue
        if matriz[op_x_linha][op_x_coluna] == 'X' or matriz[op_x_linha][op_x_coluna] == 'O':
            print('Boa tentativa!')
        else:
            matriz[op_x_linha][op_x_coluna] = 'X'
            vez += 1
            for i in matriz: print(i)


    elif vez % 2 == 0: # Se a vez for par é vez de O!

        op_o = int(input('Escolha uma opção O: '))
        op_o_coluna = 0
        if op_o > 0 and op_o< 4:
            op_o_linha = 0
            if op_o == 1:
                op_o_coluna = 0
            elif op_o == 2:
                op_o_coluna = 1
            else:
                op_o_coluna = 2
        elif op_o > 3 and op_o < 7:
            op_o_linha = 1
            if op_o == 4:
                op_o_coluna = 0
            elif op_o == 5:
                op_o_coluna = 1
            else:
                op_o_coluna = 2
        elif op_o > 6 and op_o < 10:
            op_o_linha = 2
            if op_o == 7:
                op_o_coluna = 0
            elif op_o == 8:
                op_o_coluna = 1
            else:
                op_o_coluna = 2
        else:
            print('Opção ínvalida, tente novamente')
            continue
        if matriz[op_o_linha][op_o_coluna] == 'X' or matriz[op_o_linha][op_o_coluna] == 'O':
            print('Boa tentativa!')
        else:
            matriz[op_o_linha][op_o_coluna] = 'O'
            vez += 1
            for i in matriz: print(str(i).center(1))

    #TESTA SE ALGUÉM GANHOU
    if matriz[0][0] == matriz[0][1] == matriz[0][2]:
        if matriz[0][0] == 'X':
            x_ganhou = True
        elif matriz[0][0] == 'O':
            o_ganhou = True
    elif matriz[1][0] == matriz[1][1] == matriz[1][2]:
        if matriz[1][0] == 'X':
            x_ganhou = True
        elif matriz[1][0] == 'O':
            o_ganhou = True
    elif matriz[2][0] == matriz[2][1] == matriz[2][2]:
        if matriz[2][0] == 'X':
            x_ganhou = True
        elif matriz[2][0] == 'O':
            o_ganhou = True
    elif matriz[0][0] == matriz[1][0] == matriz[2][0]:
        if matriz[0][0] == 'X':
            x_ganhou = True
        elif matriz[0][0] == 'O':
            o_ganhou = True
    elif matriz[0][1] == matriz[1][1] == matriz[2][1]:
        if matriz[0][1] == 'X':
            x_ganhou = True
        elif matriz[0][1] == 'O':
            o_ganhou = True
    elif matriz[0][2] == matriz[1][2] == matriz[2][2]:
        if matriz[0][2] == 'X':
            x_ganhou = True
        elif matriz[0][2] == 'O':
            o_ganhou = True
    elif matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[0][0] == 'X':
            x_ganhou = True
        elif matriz[0][0] == 'O':
            o_ganhou = True
    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[0][2] == 'X':
            x_ganhou = True
        elif matriz[0][2] == 'O':
            o_ganhou = True
    if x_ganhou:
        print('PARABÉNS X GANHOU!!!')
        break
    elif o_ganhou:
        print('PARABÉNS O GANHOU!!!')
        break
