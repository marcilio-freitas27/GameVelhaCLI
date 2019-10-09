# -*- coding: utf-8 -*-

print('\t\tJogo da velha em Python v1.0.0\n')

# Matriz correspondente ao tabuleiro 
pos = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# Variável contadora de jogadas
c = 1

# Escolha do jogador e seu símbolo(J1/J2 e x/o)
j1 = input('Qual o símbolo do jogador 1(x ou o)? ')
j2 = input('Qual o símbolo do jogador 2(x ou o)? ')

# Lista de jogadores 
j = [j1,j2]

# Condições para atribuição de símbolos à jogadores
# Nessas condições também é atribuida a indicação de primeira jogada 
if j == ['x','o']:
    print('\nJogada',c,'|','j1 =',j[0],'|','j2 =',j[1],'|','\nJogador 1')
if j == ['o','x']:
    print('\nJogada',c,'|','j1 =',j[0],'|','j2 =',j[1],'|','\nJogador 1')

# Inicio do jogo
while True:
    p1 = 0
    p2 = 0
    # escolha a posição que vc vai jogar(1 a 9)
    p = int(input('Digite a posição de jogada(1 - 9): ')) 
    if p <= 3: # posições de 1 a 3
        p1 = p - p
        p2 = p - 1
    elif 3 < p <= 6 : # posições de 4 a 6
        p1 = p//p
        p2 = p - 4
    else: # posições de 7 a 9
        p1 = (p + p)//p
        p2 = p - 7

    if True:
        # coloque o seu símbolo(x ou o) na posição escolhida
        pos[p1][p2] = input('Insira o símbolo na posição: ')
        print('\n',pos[0],'\n',pos[1],'\n',pos[2])
        # condições para indicar qual a jogada e o jogador da vez
        if c > 0 : # A jogada 1 já foi feita
            c += 1
            if c%2 == 0: # jogadas pares(2,4,6,8)
                print('\nJogada',c,'|','j1 =',j[0],'|','j2 =',j[1],'|','\nJogador 2')
            else: # jogadas impares(3,5,7,9)
                print('\nJogada',c,'|','j1 =',j[0],'|','j2 =',j[1],'|','\nJogador 1')

# Condições de vitória: jogadas na horizontal(linha)

            if pos[0] == ['x','x','x']:
                if j1 == 'x' :
                    print('\nj1 venceu.')
                else:
                    print('\nj2 venceu.')
                break
            if pos[0] == ['o','o','o']:
                if j1 == 'o' :
                    print('\nj1 venceu.')
                else:
                    print('\nj2 venceu.')
                break
            if pos[1] == ['x','x','x']:
                if j1 == 'x' :
                    print('\nj1 venceu.')
                else:
                    print('\nj2 venceu.')
                break
            if pos[1] == ['o','o','o']:
                if j1 == 'o' :
                    print('\nj1 venceu.')
                else:
                    print('\nj2 venceu.')
                break
            if pos[2] == ['x','x','x']:
                if j1 == 'x' :
                    print('\nj1 venceu.')
                else:
                    print('\nj2 venceu.')
                break
            if pos[2] == ['o','o','o']:
                if j1 == 'o' :
                    print('\nj1 venceu.')
                else:
                    print('\nj2 venceu.')
                break

# Condições de vitória : jogadas na vertical(coluna)

            if pos[0][0] == 'x' and pos[1][0] == 'x' and pos[2][0] == 'x':
                if j1 == 'x' : # Diz qual jogador
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][0] == 'o' and pos[1][0] == 'o' and pos[2][0] == 'o':
                if j1 == 'o' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][1] == 'x' and pos[1][1] == 'x' and pos[2][1] == 'x':
                if j1 == 'x' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][1] == 'o' and pos[1][1] == 'o' and pos[2][1] == 'o':
                if j1 == 'o' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][2] == 'x' and pos[1][2] == 'x' and pos[2][2] == 'x':
                if j1 == 'x' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][2] == 'o' and pos[1][2] == 'o' and pos[2][2] == 'o':
                if j1 == 'o' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break

# Condições de vitória: jogadas na diagonal

            if pos[0][0] == 'x' and pos[1][1] == 'x' and pos[2][2] == 'x':
                if j1 == 'x' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][0] == 'o' and pos[1][1] == 'o' and pos[2][2] == 'o':
                if j1 == 'o' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][2] == 'x' and pos[1][1] == 'x' and pos[2][0] == 'x':
                if j1 == 'x' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break
            if pos[0][2] == 'o' and pos[1][1] == 'o' and pos[2][0] == 'o':
                if j1 == 'o' :
                    print('\nj1 venceu.', j1)
                else:
                    print('\nj2 venceu.', j2)
                break

    if c > 9: # mais de 9 jogadas significa que ambos os jogadores não atingiram nenhuma das condições de vitória

        print('\nDeu empate!!!')
        # sugestão para testes de 2 tipos de empate :
        
        '''
        quando o j1 = o | quando o j1 = x

        ['o', 'x', 'o'] | ['x', 'o', 'x']  
        ['x', 'o', 'x'] | ['o', 'x', 'o']
        ['x', 'o', 'x'] | ['o', 'x', 'o']
        '''
        
        jn = input('\nQuer jogar novamente(yes/no)? ').lower()
        if jn == 'no':
            break
        else: # yes
            print('\nNovo jogo!!!')
            c = 1
            pos = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# Escolha do jogador e seu símbolo(J1/J2 e x/o)
            j1 = input('\nQual o símbolo do jogador 1(x ou o)? ')
            j2 = input('Qual o símbolo do jogador 2(x ou o)? ')

# Lista de jogadores 
            j = [j1,j2]

# Condições para atribuição de símbolos à jogadores 
            if j == ['x','o']:
                print('\nJogada',c,'|','j1 =',j[0],'|','j2 =',j[1],'|','\nJogador 1')
            if j == ['o','x']:
                print('\nJogada',c,'|','j1 =',j[0],'|','j2 =',j[1],'|','\nJogador 1')
                

