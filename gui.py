from termoMod import termo
import tkinter as tk


class guiTermo:
    def __init__(self):
        self.janela = tk.Tk()
        self.button = []
        self.entrys = []
        self.statusBotoes = [0, 0, 0, 0, 0]
        self.letras = []
        self.inputLetras = ['', '', '', '', '']
        self.submit = tk.Button()
        self.termoApi = termo()

    def submitCommand(self):
        for x in range (5):
            self.inputLetras[x] = self.entrys[x].get()
        for y in range (5):
            if(self.statusBotoes[y] == 2 and self.inputLetras[y] != ''):
                self.termoApi.inserirComPosicao(self.inputLetras[y], y)
            if(self.statusBotoes[y] == 1 and self.inputLetras[y] != ''):
                self.termoApi.inserirSemPosicao(self.inputLetras[y], y)
            if(self.statusBotoes[y] == 0 and self.inputLetras[y] != ''):
                self.termoApi.inserirNaoUsadas(self.inputLetras[y])
        print(self.inputLetras)
        self.termoApi.procurarPalavras()
        print(self.termoApi.possiveisPalavras)

    def color_change(self, botao):
        if(self.button[botao].cget('bg') == "grey"):
            self.button[botao].config(bg = "yellow")
            self.statusBotoes[botao] = 1
        elif(self.button[botao].cget('bg') == "yellow"):
            self.button[botao].config(bg = "green")      
            self.statusBotoes[botao] = 2    
        elif(self.button[botao].cget('bg') == "green"):
            self.button[botao].config(bg = "grey")  
            self.statusBotoes[botao] = 0
        print(self.statusBotoes)

    def caps(self,num):
        for x in range(5):
            self.letras[x].set(self.letras[x].get().upper())

    def configurarJanela(self):
        self.janela.geometry('600x600')
        for x in range(5):
            self.button.append(tk.Button(self.janela,command= lambda x1=x: self.color_change(x1),bg = 'grey')) 
            self.button[x].place(x = (x * 100) + 75, y = 100, width = 50, height = 50)
            variavel = tk.StringVar()
            self.letras.append(variavel)
            self.entrys.append(tk.Entry(self.janela, textvariable = self.letras[x], font = ('calibre', 10, 'bold'), justify = 'center'))
            self.entrys[x].bind('<KeyRelease>', self.caps)
            self.entrys[x].place(x = (x * 100) + 75, y = 50, width = 50, height = 50)
        self.submit = tk.Button(self.janela, text = "Finalizar rodada", command = self.submitCommand, font = ('calibre', 12, 'bold'), justify = 'center')
        self.submit.place(x = 200, y = 400, width = 200, height = 100)


    def main(self):
        self.configurarJanela()
        self.janela.mainloop()


termo = guiTermo()
termo.main()