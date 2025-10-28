# EQUIPE:

# ALUIZIO PEREIRA ALMENDRA NETO / 565068
# AMERICO VITOR MOREIRA BARBOSA / 571045
# ANNA LAYSSA GALDINO PAULO DE SOUSA / 566837


#bibliotecas utilizadas

import sys
import os


#Vai armazenar a quantidade de entradas no terminal
arquivos = sys.argv

#cores utilizadas
GREEN = "\033[32m"
RED = "\033[38;5;204m"
CYAN = "\033[36m"
LIGHT_BLUE = "\033[94m"
RESET = "\033[0m"
#nome sudoku
nomeSudoku = """  
╔═══════════════════════════════════════════╗
║                                           ║
║  .-----.--.--.--|  |.-----.|  |--.--.--.  ║
║  |__ --|  |  |  _  ||  _  ||    <|  |  |  ║
║  |_____|_____|_____||_____||__|__|_____|  ║
║                                           ║
╚═══════════════════════════════════════════╝
"""
# mensagem de parabens
Parabens = """
╔═══════════════════════════════════════════════════╗
║ _____                _                      _ _ _ ║
║|  __ \              | |                    | | | |║
║| |__) |_ _ _ __ __ _| |__   ___ _ __  ___  | | | |║
║|  ___/ _` | '__/ _` | '_ \ / _ \ '_ \/ __| | | | |║
║| |  | (_| | | | (_| | |_) |  __/ | | \__ \ |_|_|_|║
║|_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___/ (_|_|_)║
╚═══════════════════════════════════════════════════╝
"""


#-------------------------------------------------------------------------------
#SUBPROGRAMAS/FUNÇOES
#-------------------------------------------------------------------------------

#Função para escrever no centro do terminal o SUDOKU
def centroSudoku(texto):
    lar_ter = os.get_terminal_size().columns

    for linha in texto.split('\n'):
        texto_centro = linha.center(lar_ter)
        print(CYAN, texto_centro, RESET)

#Função para centralizar as linhas
def centroTexto(texto, ajuste):
    # ajuste é somada a variavel de largura do terminal para centralizar
    #fizemos isso por conta das cores adicionadas
    lar_ter = os.get_terminal_size().columns+ajuste
    print(texto.center(lar_ter))

#Funçao para limpar o terminal
def clear():
    os.system("clear")

#Funçao que recebe as dicas e retorna a matriz sudoku e a variavel erro
def configuraçao(dicas):
    sudoku=[]      #matriz sudoku
    erro= 0    #condiçao de erro
    for i in range(9):   #preenchimento da matriz
        sudoku.append([None]*9)
    for a in range(len(dicas)):
        cm = coluna(dicas[a][0])  #variavel que indica o indice da coluna
        if cm =="erro":  #condiçao em caso de coluna invalida
            erro = 1     #condiçao em caso de dica invalida(de acordo com o seu tamanho)
        elif len(dicas[a])!=6 and a==len(dicas)-1:
            erro = 1     #condiçao em caso de dica invalida
        elif (len(dicas[a])!=7 and a!=len(dicas)-1) or dicas[a][2]=="0" or dicas[a][5]=="0":
            erro = 1
        else:      #condiçao em caso de invalidaçao por ser uma celula ja preenchida
            if sudoku[int(dicas[a][2])-1][cm]!=None:
                if sudoku[int(dicas[a][2])-1][cm]!=int(dicas[a][5]):
                    erro=1
            else:          #condiçao em caso de dica invalidada por descumprir as regras basica do jogo
                sudoku[int(dicas[a][2])-1][cm] = int(dicas[a][5])
                if validaçao(sudoku, int(dicas[a][2])-1,cm)==False:
                    erro=1

    return sudoku, erro # se erro==0 valida, se nao invalidada


#    funçao de saida da grade, recebe a grade sudoko e a ultim+a jogada feita) ->
#    e sai de acordo com a configuraçao da tabela
def grade(x, ja):
    #Vai escrever o nome estilizado do Sudoku
    print(LIGHT_BLUE,nomeSudoku, RESET)
    if ja!="": #saida da ultima jogada feita
        print("{}Jogada anterior: {}{}".format(CYAN, ja.upper(), RESET))
        print("-"*60)
    for a in range(21):
        if a==0 or a==20: #utilizaçao de condicionais estrategicas para cada linha de saida
            print("    A   B   C    D   E   F    G   H   I    ")
        if a==7 or a==13:
            print(" ++===+===+===++===+===+===++===+===+===++ ")
        if a%2==0 and a!=0 and a!=20:
            print("{}|".format(int(a/2)), end="")
            for b in range(9):
                if x[int((a/2)-1)][b]!=None:
                    if b==2 or b==5 or b==8:
                        print("| {} |".format(x[int((a/2)-1)][b]), end="")
                    else:
                        print("| {} ".format(x[int((a/2)-1)][b]), end="")
                if x[int((a/2)-1)][b]==None:
                    if b==2 or b==5 or b==8:
                        print("|   |", end="")
                    else:
                        print("|   ", end="")
            print("|{}".format(int(a/2)))
        if a%2!=0 and a!=7 and a!=13:
            print(" ++---+---+---++---+---+---++---+---+---++ ")
    print("\n")
#retorna as saidas de acordo com a tabela proposta


#funçao que verifica se um certo espaço na grade é valido de acordo com as regras do jogo
def validaçao(inicial,i,j): #recebe a grade, alem da linha e coluna de uma determinada casa
    validade = True       #variavel validade
    for k in range(9):
        if inicial[i][j]==inicial[i][k] and j!=k:  #verifica a validade na coluna e linha de uma casa
            validade = False
        if inicial[i][j]==inicial[k][j] and k!=i:
            validade = False
    if validade== True:
        if i<=2:
            for l in range(3):
                if j<=2:                #verifica a validade no quadrante de casa
                    for m in range(3):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                if j>5:
                    for m in range(6,9):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
        if 5>=i>2:
            for l in range(3,6):
                if j<=2:
                    for m in range(3):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                if j>5:
                    for m in range(6,9):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
        if i>5:
            for l in range(6,9):
                if j<=2:
                    for m in range(3):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                if j>5:
                    for m in range(6,9):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
    return validade   # se a variavel validade for falsa, entao a jogada é invalida




#funçao define as possibilidasdes para uma determinada casa no jogo
def possibilidades(inicial,i,j): #    recebe a grade, alem da linha e coluna de uma determinada casa
    possib=[1,2,3,4,5,6,7,8,9] #     possibilidades do sudoku
    naoposs=[]   #    lista vazia que representa os numeros que nao podem preencher aquela casa(inicialmente vazia)
    for k in range(9):
        if inicial[i][k]!=None:             #    semelhante a funçao de validade, verifica quais os numeros presentes ->
            naoposs.append(inicial[i][k])   #    na coluna e linha da casa e adiciona a lista de nao possibilidades
        if inicial[k][j]!=None:
            naoposs.append(inicial[k][j])
        if i<=2:
            for l in range(3):
                if j<=2:
                    for m in range(3):
                        if inicial[l][m]!=None: #              semelhante a funçao de validade, verifica quais os numeros presentes ->
                            naoposs.append(inicial[l][m]) #    no quadrante da casa e adiciona a lista de nao possibilidades
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if j>5:
                    for m in range(6,9):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
        if 5>=i>2:
            for l in range(3,6):
                if j<=2:
                    for m in range(3):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if j>5:
                    for m in range(6,9):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
        if i>5:
            for l in range(6,9):
                if j<=2:
                    for m in range(3):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if j>5:
                    for m in range(6,9):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
    if len(naoposs)!=0:
        for k in naoposs: # estrutura que verifica quais os casos nao possiveis e remove da lista de possibilidades
            if k in possib:
                possib.remove(k)
    return possib #   retorna a lista com as possibilidades para determinada casa



#funçao para identificar em qual coluna esta o numero
def coluna(N): #   funçao recebe a letra correspondente a coluna e retorna o valor indexado(ex: "A" -> 0)
    colunas = [["A", 0,"a"], ["B", 1,"b"], ["C", 2,"c"], ["D", 3,"d"], ["E", 4,"e"], ["F", 5,"f"], ["G", 6, "g"], ["H", 7, "h"], ["I", 8,"i"]]
    x = "erro" #    lista acima contendo as letras e seus respectivos indicies
    for i in range(9):
        if N==colunas[i][0] or N==colunas[i][2]:
            x = i
    return x  #    em caso de uma string correspondente, retorna o indice. em caso contrario retorna a variavel como "erro"


#funçao para validar o formato de uma entrada
def entrada(N): #     a funçao recebe a entrada ja com a retirada dos espaços
    erro = 0  #    variavel erro
    if len(N)==4:     #    verifica o tamanho em caso de formato equivalente a uma entrada de exclusao ou possibilidade de uma casa
        if N[0]!="?" and N[0]!="!":
            erro=1
        else:       #      condicionais para verificar se a formataçao segue o padrao
            if coluna(N[1])=="erro":
                erro=1
            else:
                if N[2]!=",":
                    erro=1
                else:
                    if N[3]=="0":
                        erro=1
    elif len(N)==5:     # verifica o tamnho em caso de formato equivalente a uma entrada de adiçao de valor a uma casa
        if coluna(N[0])=="erro":
            erro=1
        else:
            if N[1]!=",":  #condicionais para verificar se a formataçao segue o padrao
                erro=1
            else:
                if N[2]=="0":
                    erro=1
                else:
                    if N[3]!=":":
                        erro=1
                    else:
                        if N[4]=="0":
                            erro=1
    else:
        erro=1
    return erro # em caso de erro=0, entao a entrada segue o formato padrao, caso erro=1, entrada com formato invalido







#-------------------------------------------------------------------------------
#PROGRAMAS/MODOS DE JOGO
#-------------------------------------------------------------------------------

#funçao que roda o modo interativo
def interativo(dicas):
    sudoku= configuraçao(dicas)[0]   #grade do jogo
    jogada_anterior = ""       # variavel  correspondente a jogada anterior
    if len(dicas)>80:
        print(f"{RED}QUANTIDADE DE DICAS ACIMA DO LIMITE!{RESET}")    # condicional em caso de invalidaçao pela quantidade de dicas
    else:
        if configuraçao(dicas)[1]==1:
            print(f"{RED}CONFIGURAÇAO INICIAL INVALIDA!{RESET}")   # condicional em caso de invalidaçao por configuraçao inicial invalida
        else:
            grade(sudoku, jogada_anterior)  # saida da grade
            parada = 0    #     variavel de parada(quantidade de casa preenchidas)
            for i in range(9):
                for j in range(9):  #     estrutura para identificar a quantidade de casas preenchidas
                    if sudoku[i][j]!=None:
                        parada+=1
            while parada<81:  #     repetiçao enquanto a grade nao for totalmente preenchida
                N = input("NOVA JOGADA: ").split()  #   entrada da jogada
                N = "".join(N)
                if entrada(N)==1:   #        condicional para verificar a validade da entrada
                    print(f"{RED}JOGADA INVALIDA!!{RESET}")
                else:
                    jogada_anterior = N  #     guardando na memoria a jogada
                    if N[0]=="?":        #       condiçao em caso de entrada pedindo as possibilidades
                        Nj=coluna(N[1]) # variavel coluna
                        Ni=int(N[3])-1 # variavel linha
                        if sudoku[Ni][Nj]!=None:  #   condiçao em caso de casa ja preenchida
                            print(f"{RED}CASA PREENCHIDA!{RESET}")
                        else:
                            possibilidade = possibilidades(sudoku, Ni, Nj) #  estrura para sair as possibilidades
                            print(f"{CYAN}AS POSSIBILIDADES PARA ESSA CASA SAO: {RESET}")
                            for i in range(len(possibilidade)):
                                print(possibilidade[i], end=" ")
                            print("\n")
                    elif N[0]=="!":  # condiçao em caso de entrada para excluir uma casa
                        Nj=coluna(N[1])   # variavel coluna
                        Ni=int(N[3])-1   # variavel linha
                        if sudoku[Ni][Nj]!=None:
                            erro = 0         #   estrutura para identificar se a posiçao corresponde a uma dica
                            for i in range(len(dicas)):
                                if Nj==coluna(dicas[i][0]):
                                    if Ni+1==int(dicas[i][2]):
                                        erro=1
                            if erro==1:      #    saida em caso da casa ser de uma dica
                                print(f"{RED}POSIÇAO CORRESPONDENTE A UMA DICA!{RESET}")
                            else:             #     saida em caso de remoçao validada
                                sudoku[Ni][Nj]=None
                                parada-=1
                                clear()
                                grade(sudoku, jogada_anterior)
                        else:                 #         saida em caso da casa nao ter nenhum numero
                            print(f"{RED}POSIÇAO INFORMADA NAO TEM UM NUMERO!{RESET}")
                    else:         #           condiçao em caso de entrada para adicionar uma casa
                        N = N.split(":")
                        N[0] = N[0].split(",")
                        Nj= coluna(N[0][0])  #    variavel coluna
                        Ni= int(N[0][1])-1  #    variavel linha
                        Nv= int(N[1][0])    # variavel do numero a ser colocado na casa
                        erro = 0 #     estrutura para identificar se a casa pertence a uma dica
                        for i in range(len(dicas)):
                            if Nj==coluna(dicas[i][0]):
                                if Ni+1==int(dicas[i][2]):
                                    erro=1
                        if erro==1:   #     condiçao em caso da casa pertencer a uma dica
                            print(f"{RED}JOGADA INVALIDA(CASA PERTENCE A UMA DICA)!!{RESET}")
                        else:
                            if sudoku[Ni][Nj]!=None: #     condiçao em caso da casa ja esta preenchida(e nao ser uma dica)
                                print("ESPAÇO PREENCHIDO! deseja sobrescrever com essa entrada?")
                                print("Responda com S para sim, e N para nao")   #  saida para perguntar ao jogador qual o proximo movimento
                                resposta = 0
                                while resposta==0:
                                    R = input().upper()   # entrada resposta
                                    if R=="S":  #  condiçao caso o jogador queira sobrescrever na casa em questao
                                        K = sudoku[Ni][Nj]
                                        sudoku[Ni][Nj]=Nv
                                        if validaçao(sudoku, Ni, Nj)==False: #  condiçao em caso de  entrada invalida
                                            print(f"{RED}JOGADA INVALIDA!!{RESET}")
                                            sudoku[Ni][Nj] = K
                                        else:    #    condiçao em caso de entrada valida
                                            clear()
                                            grade(sudoku, jogada_anterior)
                                        resposta = 1
                                    elif R=="N":  #   condiçao em caso do jogador nao queira sobrescrever a casa
                                        resposta = 1
                                    else:   #         condiçao em caso do jogador nao ter digitado uma das opçoes acima
                                        print(f"{RED}RESPOSTA INCORRETA! TENTE NOVAMENTE{RESET}")
                            else:          #         condiçao em caso da casa estar vazia
                                sudoku[Ni][Nj]=Nv
                                if validaçao(sudoku, Ni, Nj)==False: #  estrutura para validar a entrada
                                    print(f"{RED}JOGADA INVALIDA!!{RESET}")   # saida em caso de invalida
                                    sudoku[Ni][Nj]=None
                                else:              #  saida em caso de valida
                                    parada+=1
                                    clear()
                                    grade(sudoku, jogada_anterior)
            print(GREEN, Parabens, RESET)    # saida apos completar o jogo (FIM DO MODO INTERATIVO)




def batch(dicas, jogadas):
    sudoku = (configuraçao(dicas))[0]#  Serve para configurar as dicas

    #Faz com que as jogadas iguais da lista tornem-se 1 elemento só
    jogadas_unicas = list(set(jogadas))

    if configuraçao(dicas)[1]==1:
        print("Configuracao de dicas invalida") #   Confere se o retorno das diccas é inválido
    else:
        qtd_dicas = 0
        parada = 0
        for i in range(9):
            for j in range(9):
                if sudoku[i][j]!=None:
                    parada+=1
                    qtd_dicas+=1
        if qtd_dicas==81:
            print("Configuracao de dicas invalida")    #    Validação de quantas dicas foram colocadas no .txt
        else:

            for jogada in jogadas_unicas:    #      Vamos agora analisar o documento de jogadas e valida-las
                erro = 0
                jogada = jogada.split()
                jogada = "".join(jogada)
                #Caso a jogada tenha mais de 5 elementos(Fora do padrão) Ex.: A,45:1
                if len(jogada) != 5:
                    erro = 1

                #Obtem a jogada anterior
                JA = jogada

                jogada = jogada.split(":")
                jogada[0] = jogada[0].split(",")

                #Confere a coluna e a função retorna um erro
                if coluna(jogada[0][0]) == "erro" or erro == 1:
                    print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
                #Adiciona a jogada
                else:
                    Nj= coluna(jogada[0][0])
                    Ni= int(jogada[0][1])-1
                    Nv= int(jogada[1][0])

                    #Para as jogadas invalidas
                    if Ni>8 or Ni<0:
                        print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
                    else:
                        erro = 0
                        for i in range(len(dicas)):
                            if Nj==coluna(dicas[i][0]):
                                if Ni+1==int(dicas[i][2]):
                                    erro=1
                        if erro==1:
                            print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
                        else:
                            if sudoku[Ni][Nj]!=None:
                                print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
                            else:
                                sudoku[Ni][Nj]=Nv
                                #Valida as jogadas
                                if validaçao(sudoku, Ni, Nj)==False:
                                    print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
                                    sudoku[Ni][Nj]=None
                                #Se a validação der certo, conta +1 celula
                                if validaçao(sudoku, Ni,Nj)==True:
                                    parada += 1

            #Confere se foram 81 celulas preenchidas para dizer se a grade está ou não preenchida
            if parada == 81:
                print("A grade foi preenchida com sucesso!")
            else:
                print("A grade nao foi preenchida!")





def main():
    #Limpa o terminal
    clear()
    #Vai verificar quantos arquivos vão ser lidos, caso seja 2 executa o INTERATIVO, caso seja 3, executa o BATCH

    #Roda o MODO INTERATIVO
    if len(arquivos) == 2:
        with open(arquivos[1], "r") as dicas:
            dicas = dicas.readlines()
        interativo(dicas)

    #Roda o modo Batch
    elif len(arquivos) == 3:
        with open(arquivos[1], "r") as dicas:
            dicas = dicas.readlines()
        with open(arquivos[2], "r") as jogadas:
            jogadas = jogadas.readlines()
        batch(dicas, jogadas)

    else:
        print(f"{RED}ERRO COM O NÚMERO DE ARQUIVOS INSERIDOS{RESET}")



#-------------------------------------------------------------------------------
#RODANDO O CODIGO
#-------------------------------------------------------------------------------


#Menu inicial
Resp = 5
terminar = False

#Testa se é o modo interativo para iniciar com o menu
if len(arquivos) == 2:
    while Resp != 1 and Resp != 3:
        clear()
        centroSudoku(nomeSudoku)
        centroTexto("======================================",0)
        centroTexto("Digite 1 para iniciar",0)
        centroTexto("Digite 2 para instruções",0)
        centroTexto("Digite 3 para encerrar o programa",0)
        centroTexto("======================================",0)


        Resp = int(input())

        #Inciar
        if Resp == 1:
            clear()
            terminar = False

        #Instruções
        elif Resp == 2:
            Veri = True
            while Veri:
                clear()
                centroSudoku(nomeSudoku)
                centroTexto("======================================",0)
                centroTexto(" Jogadas:",0)
                centroTexto("----------",0)
                centroTexto(f"{GREEN}<Linha>{RESET},{GREEN}<Coluna>{RESET} : {GREEN}<Numero>{RESET} -> Para fazer sua jogada",27)
                centroTexto(f"?{GREEN}<Linha>{RESET},{GREEN}<Coluna>{RESET} : {GREEN}<Numero>{RESET} -> Obtém as jogadas possíveis para a celula",27)
                centroTexto(f"!{GREEN}<Linha>{RESET},{GREEN}<Coluna>{RESET} : {GREEN}<Numero>{RESET} -> Exclui uma jogada realizada anteriormente",27)
                centroTexto(f"{RED}OBS.: Não eh possivel excluir dicas{RESET}",15)
                centroTexto("----------",0)
                centroTexto("Nao eh possivel jogar um numero na mesma que ja esteja na mesma linha ou coluna ou quadrante\n",0)
                centroTexto("Digite 1 para retornar ao inicio",0)
                Ret = int(input())

                if Ret == 1:
                    Veri = False
                else:
                    Veri = True

        #Encerrar
        elif Resp == 3:
            terminar = True


#Se for modo Batch ele entra aqui de cara
if terminar == False:
    main()