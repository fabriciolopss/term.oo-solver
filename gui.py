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
        self.listaResposta = tk.Listbox()
        self.scrollBar = tk.Scrollbar(self.listaResposta)

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
        with open("listaCompletaPossiveisPalavras.txt", "w", encoding="utf-8") as f:
            for x in self.termoApi.possiveisPalavras:
                f.write(x)
        self.listaResposta.delete(0, tk.END)
        for palavras in self.termoApi.possiveisPalavras:
            self.listaResposta.insert(tk.END, palavras)
        

    def color_change(self, botao):
        if(self.button[botao].cget('bg') == "#d0d0d0"):
            self.button[botao].config(bg = "#FFE61B")
            self.statusBotoes[botao] = 1
        elif(self.button[botao].cget('bg') == "#FFE61B"):#yellow
            self.button[botao].config(bg = "#B5FE83")      
            self.statusBotoes[botao] = 2    
        elif(self.button[botao].cget('bg') == "#B5FE83"): #green
            self.button[botao].config(bg = "#d0d0d0")  #grey
            self.statusBotoes[botao] = 0
        print(self.statusBotoes)

    def caps(self,num):
        for x in range(5):
            self.letras[x].set(self.letras[x].get().upper())

    def configurarJanela(self):
        self.janela.iconbitmap('password_security_icon_154431.ico')
        self.janela['background'] = '#F7F7F7'
        self.janela.title("Resolvedor de Termos")
        self.janela.geometry('600x600')
        for x in range(5):
            self.button.append(tk.Button(self.janela,command= lambda x1=x: self.color_change(x1),bg = '#d0d0d0')) 
            self.button[x].place(x = (x * 100) + 75, y = 110, width = 50, height = 50)
            variavel = tk.StringVar()
            self.letras.append(variavel)
            self.entrys.append(tk.Entry(self.janela, textvariable = self.letras[x], font = ('calibre', 10, 'bold'), justify = 'center'))
            self.entrys[x].bind('<KeyRelease>', self.caps)
            self.entrys[x].place(x = (x * 100) + 75, y = 50, width = 50, height = 50)
        self.submit = tk.Button(self.janela, text = "FINALIZAR RODADA", command = self.submitCommand, font = ('calibre', 12, 'bold'), justify = 'center',
         bg = '#ececec', activebackground = '#B5FE83')
        self.submit.place(x = 200, y = 200, width = 200, height = 100)
        self.scrollBar.pack(side = tk.RIGHT, fill = tk.Y)
        self.listaResposta = tk.Listbox(self.janela, yscrollcommand= self.scrollBar.set, font = ('calibre', 10, 'bold'))
        self.listaResposta.place(x = 100, y = 350, width = 400, height = 200)


    def main(self):
        self.configurarJanela()
        self.janela.mainloop()


termo = guiTermo()
termo.main()