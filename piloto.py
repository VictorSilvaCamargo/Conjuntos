#Victor Silva Camargo BCC

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
#linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de 
#operações que serão realizadas entre dois conjuntos de dados.  
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
#operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas 
#seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da 
#operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e 
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo 
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
#4 
#U 
#3, 5, 67, 7 
#1, 2, 3, 4  
#I 
#1, 2, 3, 4, 5 
#4, 5 
#D 
#1, A, C, 34 
#A, C, D, 23 
#C 
#3, 4, 5, 5, A, B, R 
#1, B, C, D, 1 
#Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um 
#produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e 
#{𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).  
#A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados 
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter 
#a informação e a formatação mostrada a seguir:    
#União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}   
#Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer 
#um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo 
#de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e 
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.  
#No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e 
#pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, 
#implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento. 
#Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
#contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
#diferentes.  Os  arquivos  de  entrada  criados  para  os  seus  testes  devem  estar  disponíveis  tanto  no 
#ambiente repl.it quanto no ambiente Github.  
#Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, 
#no mínimo um arquivo de testes criado pelo próprio professor.

texto = open('teste.txt')
arquivo = texto.readlines()
arquivo = [x.rstrip('\n') for x in arquivo]
virgula=','
lista=['U','I','D','C']             #Codigo para abrir o arquivo txt, retirar o caractere de pular linha"\n"
                                    #A variável vírgula é para fazer a remoção da vírgula para ela não ser contada como um
                                    #caractere e não participar das operações,o vetor lista é para detectar que tipo de operação
                                    #será realizada

for i in range(len(arquivo)):
    if arquivo[i][0] in lista:
        conjunto = arquivo[i][0]    #Laço de repetição para percorrer todo o arquivo e adicionar um caractere de cada vez a uma variável
        if conjunto == 'U':         #Detectar a letra para realizar as operações
            vetu1=[]                #Vetores para armazenar os conjuntos e o resultado final
            vetu2=[]
            vetu3=[]
            for valor in arquivo[i+1].split(','):   #Laço de repetição para adicionar os caracteres do arquivo nos vetores
                vetu1.append(valor)                 #e impedir que o código separe os caracteres que tenham dois digitos ou mais
            for valor in arquivo[i+2].split(','):   #através do "split"
                vetu2.append(valor)
            while virgula in vetu1:                 #Laço de repetição para retirar as vírgulas que foram inseridas nos vetores como 
                vetu1.remove(virgula)               #caracteres
            while virgula in vetu2:
                vetu2.remove(virgula)
            for i in vetu1:
                if i not in vetu3:                  #Laço de repetição para inserir os caracteres em um único vetor
                    vetu3.append(i)                 #sem haver repetições de caracteres
            for i in vetu2:
                if i not in vetu3:
                    vetu3.append(i)
            print("União: conjunto 1 {",vetu1,"}"", conjunto 2 {",vetu2,"}."" Resultado: {",vetu3,"}")
            
        elif conjunto == 'I':                       #Mesma logica do algorítimico da União
            veti1=[]
            veti2=[]
            veti3=[]
            for valor in arquivo[i+1].split(','):
                veti1.append(valor)
            for valor in arquivo[i+2].split(','):
                veti2.append(valor)
            while virgula in veti1:
                veti1.remove(virgula)
            while virgula in veti2:
                veti2.remove(virgula)
            for i in veti1:                         #Laço de repetição para detectar caracteres que se repetem e inserir no vetor resposta
                if i in veti1 and i in veti2:
                    veti3.append(i)
            print("Interseção: conjunto 1 {",veti1,"}"", conjunto 2 {",veti2,"}."" Resultado: {",veti3,"}")
            
        elif conjunto == 'D':                       #Mesma lógica do conjunto União
            vetd1=[]
            vetd2=[]
            vetd3=[]
            for valor in arquivo[i+1].split(','):
                vetd1.append(valor)
            for valor in arquivo[i+2].split(','):
                vetd2.append(valor)
            while virgula in vetd1:
                vetd1.remove(virgula)
            while virgula in vetd2:
                vetd2.remove(virgula)
            for i in vetd1:                             #Laço de repetição para comparar os dois vetores e inserir os que não se repetem
                if i in vetd1 and i not in vetd2:       #no vetor resposta
                    vetd3.append(i)
            for i in vetd2:
                if i in vetd2 and i not in vetd1 and i not in vetd3:
                    vetd3.append(i)
            print("Diferença: conjunto 1 {",vetd1,"}"", conjunto 2 {",vetd2,"}."" Resultado: {",vetd3,"}")
            
        elif conjunto == 'C':                           #Mesa lógica do conjunto União
            vetc1=[]
            vetc2=[]
            vetc3=[]
            for valor in arquivo[i+1].split(','):
                vetc1.append(valor)
            for valor in arquivo[i+2].split(','):
                vetc2.append(valor)
            while virgula in vetc1:
                vetc1.remove(virgula)
            while virgula in vetc2:
                vetc2.remove(virgula)
            for l in range(0,len(vetc1)):               #Laço de repetição para criar uma matriz e fazer todas as combinações possíveis
                vetc3.append([])
                for c in range(0,len(vetc2)):
                    num= vetc1[l],vetc2[c]
                    vetc3[l].append(num)
            print("Cartesiano: conjunto 1 {",vetc1,"}"", conjunto 2 {",vetc2,"}."" Resultado: {",vetc3,"}")