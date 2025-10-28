# TRABALHO-FINAL-FUP-2024.1
Trabalho final da disciplina de Fundamentos de programação I 2024.1, Ministrada pelo professor Miguel franklin

MODO INTERATIVO:
1. No modo interativo, o programa deverá ser executado tendo que ler um arquivo de configuração (em
modo texto) que contém a lista das pistas do jogo, podendo conter de 1 a 80 pistas, onde cada pista
deve seguir o seguinte formato:
<COL>,<LIN>: <NÚMERO>
<COL> representa a coluna da grade, em letras maiúsculas de “A” a “I”. <LIN> representa a linha da
grade, em algarismos de 1 a 9. E <NÚMERO> representa um número de 1 a 9 dado como pista para a
célula. O nome do arquivo texto a ser lido deverá ser informado como parâmetro ao programa
principal. Por exemplo, se o usuário digitar no prompt o comando seguinte, o Python irá executar o
programa sudoky.py e o arquivo de configuração que será lido será o arq_01_cfg.txt.
% python3 sudoku.py arq_01_cfg.txt

Após ler o arquivo de configuração das pistas, o programa deverá mostrar a grade do jogo, já
preenchida com as pistas fornecidas no arquivo de configuração. Por exemplo, considerando o
arquivo de configuração exemplificado abaixo:
A,3: 5
F,1: 3
D,8: 7
H,6: 5
F,4: 4
Para o arquivo de configuração exemplificado acima, o programa deverá mostrar a grade seguinte:

A B C D E F G H I
++---+---+---++---+---+---++---+---+---++
1|| | | || | | 3 || | | ||1
++---+---+---++---+---+---++---+---+---++
2|| | | || | | || | | ||2
++---+---+---++---+---+---++---+---+---++
3|| 5 | | || | | || | | ||3
++===+===+===++===+===+===++===+===+===++
4|| | | || | | 4 || | | ||4
++---+---+---++---+---+---++---+---+---++
5|| | | || | | || | | ||5
++---+---+---++---+---+---++---+---+---++
6|| | | || | | || | 5 | ||6
++===+===+===++===+===+===++===+===+===++
7|| | | || | | || | | ||7
++---+---+---++---+---+---++---+---+---++
8|| | | || 7 | | || | | ||8
++---+---+---++---+---+---++---+---+---++
9|| | | || | | || | | ||9
++---+---+---++---+---+---++---+---+---++
A B C D E F G H I

# COMO JOGAR?


