import os



class termo():
    def __init__(self):
        self.possiveisPalavras = []
        self.letrasSemPos = []
        self.letras = ["", "", "", "", ""]
        self.termo = ""

    def procurarPalavras(self):
        with open("dicionario5letras.txt", "r", encoding = "utf-8") as f:
           linhas = f.readlines()
           for linha in linhas:
                condLinha = False
                linhaParaChecar = list(linha)
                for x in range(len(self.letras)):
                    if(self.letras[x] == linhaParaChecar[x]):
                        linhaParaChecar[x] = '-'
                        pass
                    elif(self.letras[x] != ""):
                        condLinha = True
                for x in self.letrasSemPos:
                    if(x in linhaParaChecar):
                        pass
                    else:
                        condLinha = True
                if condLinha:
                    pass
                else:
                    self.possiveisPalavras.append(linha)

    def removerDuplicatas(self, letra):
        for y in self.letrasSemPos:
            if(y == letra):
                self.letrasSemPos.remove(y)

    def imprimirResultados(self):
        os.system("cls")
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

    def inserirComPosicao(self):
        fimLoop = False
        while(fimLoop == False):
            numLetra = int(input("Qual a posição da letra inserida? Escolha um número de 1 a 5:"))
            letraInserida = input("Qual a letra a ser inserida?")
            self.removerDuplicatas(letraInserida)
            self.letras[numLetra - 1] = letraInserida.lower()
            if(int(input("Deseja inserir mais alguma letra que você sabe a posição? 1 = sim 2 = não: ")) == 1):
                pass
            else:
                fimLoop = True
            self.imprimirResultados()


    def inserirSemPosicao(self):
        fimLoop = False
        while(fimLoop == False):
            letraInserida = input("Qual letra a ser inserida?")
            self.letrasSemPos.append(letraInserida)
            if(int(input("Deseja inserir mais alguma letra que você não sabe a posição")) == 1):
                pass
            else:
                fimLoop = True
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

palavra = termo()
palavra.mainLoop()