#Estudante: Eduardo Mendes Carbonera. Segundo período Noturno; turma U

'''
ENUNCIADO:
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações.
Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa:

1) a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro;

2) as linhas seguintes seguirão sempre o mesmo padrão de três linhas:
    2.1) a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano);
    2.2) a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas.

Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.

A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação.
No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir:

    União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}

Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos.
Em qualquer um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo de textos de entrada formatada segundo o exemplo de saída acima.
Observe as letras maiúsculas e minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.

Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um número diferente de operações, operações com dados diferentes, 
e operações em ordem diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github.

Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor.
'''

#Função para ler arquivo TXT, de forma dinâmica
def TXTReader(TXTname):
    with open(TXTname) as i:
        TXTContent = i.readlines()

    TXTContent = [x.strip('\n') for x in TXTContent]

    for lines in TXTContent:
        print (lines)
    print(f"Arquivo {TXTname} aberto com sucesso.")
    print()
    return TXTContent

#Funções para as operações de conjunto
def uniao(setA, setB):
    setC = set(setA).union(set(setB))
    return setC

def intersecao(setA, setB):
    setC = set(setA).intersection(set(setB))
    return setC

def diferenca(setA, setB):
    setC = set(setA).difference(set(setB))
    return setC

def cartesiano(setA, setB):
    setC = {(x, y) for x in setA for y in setB}
    return setC

#Processo principal
while True:
    TXTname = input("Insira o nome do arquivo.txt que deseja abrir:")
    try:
        TXTContent = TXTReader(TXTname)
        break
    except:
        print(f"O arquivo falhou em iniciar. | {TXTname} | não pode ser lido. Por favor, tente novamente.")

looping = int(TXTContent[0])
counter = 1

for i in range(looping):
    setOperation = TXTContent[counter]
    setA = TXTContent[counter + 1].split(', ')
    setB = TXTContent[counter + 2].split(', ')

    if setOperation == "U":
        resultante = uniao(setA, setB)
        Operation = "União"
    elif setOperation == "I":
        resultante = intersecao(setA, setB)
        Operation = "Interseção"
    elif setOperation == "D":
        resultante = diferenca(setA, setB)
        Operation = "Diferença"
    elif setOperation == "C":
        resultante = cartesiano(setA, setB)
        Operation = "Cartesiano"

    print(f"{Operation}: conjunto 1 {{{', '.join(setA)}}} conjunto 2 {{{', '.join(setB)}}}. Resultado: {resultante}")
    counter += 3

