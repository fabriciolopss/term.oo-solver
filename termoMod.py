import os
from unidecode import unidecode

class termo():
    def __init__(self):
        self.possiveisPalavras = []
        self.letrasSemPos = []
        self.letras = ["", "", "", "", ""]
        self.letrasNao = []
        self.termo = ""

    def procurarPalavras(self):
        self.possiveisPalavras = []
        with open("dicionario5letras.txt", "r", encoding = "utf-8") as f:
           print(self.letras)
           linhas = f.readlines()
           for linha in linhas:
                linhaParaChecar = list(linha)
                AdicionarPalavra = True
                for x in range(len(self.letras)):
                    if(self.letras[x] == ""):
                        pass
                    elif(unidecode(self.letras[x]) == unidecode(linhaParaChecar[x])):
                        pass
                    else:
                        AdicionarPalavra = False
                if(AdicionarPalavra):
                    self.possiveisPalavras.append(linha)


    def removerDuplicatas(self, letra):
        for y in self.letrasSemPos:
            if(y == letra):
                self.letrasSemPos.remove(y)

    def imprimirResultados(self):
        imprimirLetras = False
        for x in self.letras:
            if(x != ""):
                imprimirLetras = True
        if(imprimirLetras == True):
            print("Letras conhecidas em suas respectivas posições: {} ".format(self.letras))
        else:
            print("Ainda não foram introduzidas letras em suas respectivas posições!")

        if(len(self.letrasSemPos) > 0):
            print("Letras conhecidas fora de posição: {}".format(self.letrasSemPos))
        else:
            print("Ainda não foram introduzidas letras sem posição")      

    def inserirNaoUsadas(self, letraInserida):
        self.letrasNao.append(letraInserida)
        print(self.letrasNao)


    def inserirComPosicao(self, letraInserida, numLetra):
            self.removerDuplicatas(letraInserida)
            self.letras[numLetra] = letraInserida.lower()
            self.imprimirResultados()


    def inserirSemPosicao(self, letraInserida, posicao):
            self.letrasSemPos.append(letraInserida)
            self.imprimirResultados()


    def mainLoop(self):
        condicao = 0
        while(condicao != 4):
            condicao = int(input("Você sabe a posição correta da letra inserida? 1 = sim 2 = não 3 = possiveis_palavras 4 = finalizar: "))
            if(condicao == 1):
                self.inserirComPosicao()
            elif(condicao == 2):
                self.inserirSemPosicao()
            elif(condicao == 3):
                self.possiveisPalavras = []
                self.procurarPalavras()
                try:
                    if (len(self.possiveisPalavras) > 1):
                        print("Essas são as possiveis palavras: \n")
                        for x in self.possiveisPalavras:
                            print(x)
                    else:
                        self.termo = self.possiveisPalavras[0]
                        print("A palavra é {}".format(self.termo))
                except:
                    print("Erro, nenhuma palavra foi encontrada!")
