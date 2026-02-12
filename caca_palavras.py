#1- fazer um programa em python de caça palavras usando informações aprendidas ao longo da disciplina de sistemas operacionais.
#Exigências:
#Tem que ser em python. 
#Subir para o Github - repositório e tal - para o final da disciplina 
#Gere vários caça palavras 
#"PROCESSOS" : ["#ESCALONAMENTO","#PRIORIDADE","PCB","REGISTRADORES","#TIMESHARING","#TEMPO","#PROCESSO"]
# HARDWARE: ["GABINETE", "DISCO", "PROCESSADOR", "PLACA", "COOLER", "MOUSE","MONITOR","PC"],
#GERAÇÕES :["VÁLVULA","TRANSISTOR","CHIP","CIRCUITO","MAINFRAME","MICROCHIP","ENIAK","MULTIPROGRAMAÇÃO"],
#SISTEMA O SIST. :["KERNEL", "SHELL", "PROCESSO", "THREAD","DRIVER","ARQUIVO","INTERFACE","USUÁRIO","BATCH","MEMORIA"],
#SISTEMAS OPERACIONAIS:  ["LINUX", "WINDOWS", "ANDROID","EMBARCADO","UNIX","MULTITAREFA", "MOBILE",],

#Débora — vou ser bem direta com você, mas também muito honesta: o problema aqui NÃO é falta de lógica.
#Na verdade, você já está pensando como programadora. O que está te travando é transformar uma ideia abstrata em passos extremamente pequenos.Meu problema nao é de raciocinio é de estrutura.

import random
import string

linhas = 18
colunas = 20
tamanho = linhas, colunas

temas = {
"GERACOES": ["VALVULA","TRANSISTOR","CHIP","CIRCUITO","MAINFRAME","MICROCHIP","ENIAC","MULTIPROGRAMACAO","COMANDOS"],

"SISTEMA": ["KERNEL", "SHELL", "PROCESSO", "THREAD","DRIVER","ARQUIVO","INTERFACE","USUARIO","BATCH","MEMORIA"],

"SISTEMAS_OPERACIONAIS": ["LINUX", "WINDOWS", "ANDROID","EMBARCADO","UNIX","MULTITAREFA", "MOBILE"],

"PROCESSOS": ["ESCALONAMENTO","PRIORIDADE","PCB","REGISTRADORES","TIMESHARING","TEMPO","PROCESSO"]

}

def gerar_matriz():
  matriz = []

 #cria 15 linhas 
  for i in range(linhas):
      linha = []
     
      #cria 15 colunas
      for j in range(colunas):
        linha.append(" ")

      matriz.append(linha) #vai adicionar as linhas " " na matriz. pegue essa linha que acabei de montar , linhas.append(" ")-> [" ", " "] e joque no tabuleiro

  return matriz #para usa-la dentro de outras defs

def tentar_adicionar_palavras(matriz,palavras,linhas,colunas):
  #direcao , posicao , validacao
 
  linha_atual = 0 #comaça na linha 0
  for item in palavras:
     escrita = False
     tentativas = 0
     while not escrita and tentativas< 100:

         tentativas +=1

         direcao = random.choice(["horizontal","vertical"])

         #escolhe posicao segura
         if direcao == "horizontal":
          if len(item) > colunas:
           continue
          

          linha = random.randint(0, linhas - 1)
          coluna = random.randint(0, colunas - len(item))

         else: #vertical
           if len(item) > linhas:
                    continue

           linha = random.randint(0, linhas - len(item))
           coluna = random.randint(0, colunas - 1)

          #valida espaço

         if pode_escrever(matriz, item,linha,coluna,direcao):
         
          for i in range(len(item)):# pega palavra desmiuça e joga na matriz
            if direcao == "horizontal":
                        matriz[linha][coluna + i] = item[i]

            else:  # vertical
                  matriz[linha + i][coluna] = item[i]

          escrita = True
  return matriz

#matriz = gerar_matriz()
#matriz = tentar_adicionar_palavras(matriz)
#print (matriz)
def  escolher_posicao(item,linhas,colunas):  
 #linha aleatoria ,coluna segura
 #calcula  o limite seguro da coluna
 #exemplo: 15 colunas - palavra de 7 letras = só pode começar até a coluna 8

 limite_coluna = colunas - item

 #sorteia uma linha aleatoria

 linha = random.randint(0, linhas -1)

 #escolhe uma coluna que não vai estourar a matriz
 coluna = random.randint(0, limite_coluna)

 #ela so sabe : tamanho , linhas colunas
 return linha,coluna
 

def pode_escrever(matriz,palavra, linha, coluna,direcao):
   #Ela só verifica se o espaço está vazio ou tem a mesma letra.
   for i in range(len(palavra)):

      if direcao == "horizontal":
      #se nao for vazio e for diferente da letra
        if matriz[linha][coluna + i] != " " and matriz[linha][coluna+i] !=palavra[i]:
         return False
      else:
         #vertical
         if matriz[linha+i][coluna]!=" " and matriz[linha+i][coluna] != palavra[i]:
          return False
         
   return True      
      

def gerar_caca_palavras(quantidade,item):
   lista = []

   for _ in range(quantidade):

      matriz = gerar_matriz()
      matriz = tentar_adicionar_palavras(matriz,item, linhas,colunas)
      matriz = preencher_letras(matriz)
      lista.append(matriz)
   return lista



def preencher_letras(matriz):

    for i in range(linhas):
        for j in range(colunas):

            if matriz[i][j] == " ":
                matriz[i][j] = random.choice(string.ascii_uppercase)

    return matriz
def escolher_tema():

    print("TEMAS DISPONIVEIS:\n")

    for tema in temas:
        print("-", tema)

    escolha = input("\nDigite um tema: ").upper()

    while escolha not in temas:
        escolha = input("Tema invalido. Digite novamente: ").upper()

    return temas[escolha]

#chamada seria:
#palavras_escolhidas = escolher_tema()

#jogos = gerar_caca_palavras(5, palavras_escolhidas)

#for linha in jogos[0]:
   # print(" ".join(linha))
