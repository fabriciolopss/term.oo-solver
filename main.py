import os



class termo():
    def __init__(self):
        self.possiveisPalavras = []
        self.letrasSemPos = ["", "", "", "", ""]
        self.letras = ["", "", "", "", ""]
        self.termo = ""

    def procurarPalavras(self):
        with open("dicionario5letras.txt", "r", encoding = "utf-8") as f:
           linhas = f.readlines()
           for linha in linhas:
                condLinha = False
                for x in range(len(self.letras)):
                    if(self.letras[x] == linha[x]):
                       pass
                    elif(self.letras[x] != ""):
                        condLinha = True
                if condLinha:
                    pass
                else:
                    self.possiveisPalavras.append(linha)



    
    def inserirComPosicao(self):
        fimLoop = False
        while(fimLoop == False):
            numLetra = int(input("Qual a posição da letra inserida? Escolha um número de 1 a 5:"))
            letraInserida = input("Qual a letra a ser inserida?")
            self.letras[numLetra - 1] = letraInserida.lower()
            if(int(input("Deseja inserir mais alguma letra que você sabe a posição? 1 = sim 2 = não: ")) == 1):
                pass
            else:
                self.procurarPalavras()
                fimLoop = True
            os.system("cls")
            print(self.letras)

    def inserirSemPosicao(self):
        pass

    def mainLoop(self):
        if(int(input("Você sabe a posição correta da letra inserida? 1 = sim 2 = não: ")) == 1):
            self.inserirComPosicao()
        else:
            self.inserirSemPosicao()
        print(self.possiveisPalavras)

palavra = termo()
palavra.mainLoop()