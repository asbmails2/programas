import tkinter as tk

class JanelaCalculadoraIRRF:

    def __init__(self):
        self.postador = None
        
        self.aliquota = 1.2
        self.janela = tk.Tk()
        self.janela.title("Calculadoria IR retido na nota")
        
        self.label_texto = tk.Label(self.janela, text="Calculadoria IR de "+str(self.aliquota).replace('.',',')+"% \nValor da nota")
        self.label_texto.pack()

        self.campo_texto = tk.Entry(self.janela)
        self.campo_texto.pack()

        self.botao_ali = tk.Button(self.janela, text="Trocar Alíquota", command=self.change)
        self.botao_ali.bind("<Return>", lambda event: self.change())
        self.botao_ali.pack()


        self.botao_submit = tk.Button(self.janela, text="Submit", command=self.submit)
        self.botao_submit.bind("<Return>", lambda event: self.submit())
        self.botao_submit.pack()

        self.resposta = tk.Label(self.janela, text="Valor IRRF: \n Valor  Líq: ")
        self.resposta.pack()
        


    def submit(self):
        texto = self.campo_texto.get()
        texto = texto.replace(",",".")
        nota = round((float (texto)*self.aliquota/100),2)
        liq = round(float(texto)-nota,2)
        t = "Valor IRRF: R$ " + str(nota) + "\n Valor  Líq: R$ " + str(liq)
        t = t.replace(".",",")
        self.resposta.destroy()
        self.resposta = tk.Label(self.janela, text=t)
        self.resposta.pack()
    
    def resetView(self):
        self.label_texto.destroy()
        self.campo_texto.destroy()
        self.botao_ali.destroy()
        self.botao_submit.destroy()
        self.resposta.destroy()

        self.label_texto = tk.Label(self.janela, text="Calculadoria IR de "+str(self.aliquota).replace('.',',')+"% \nValor da nota")
        self.label_texto.pack()

        self.campo_texto = tk.Entry(self.janela)
        self.campo_texto.pack()

        self.botao_ali = tk.Button(self.janela, text="Trocar Alíquota", command=self.change)
        self.botao_ali.bind("<Return>", lambda event: self.change())
        self.botao_ali.pack()


        self.botao_submit = tk.Button(self.janela, text="Submit", command=self.submit)
        self.botao_submit.bind("<Return>", lambda event: self.submit())
        self.botao_submit.pack()

        self.resposta = tk.Label(self.janela, text="Valor IRRF: \n Valor  Líq: ")
        self.resposta.pack()
        


    def change(self):
        if(self.aliquota==1.2):
            self.aliquota = 2.4
        elif(self.aliquota==2.4):
            self.aliquota = 4.8
        elif(self.aliquota==4.8):
            self.aliquota = 0.24
        else:
            self.aliquota=1.2
        self.resetView()
             
    def iniciar(self):
        self.janela.mainloop()

janela_postagem = JanelaCalculadoraIRRF()
janela_postagem.iniciar()
