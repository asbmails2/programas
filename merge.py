from PyPDF2 import PdfMerger
import os
import tkinter as tk

"""
Criar uma programainha para dar merge em pdf com um simples interface gráfica
"""

class Janela:
    def __init__(self):

        self.janela = tk.Tk()
        self.janela.title("Calculadoria IR 1,2%")
        self.janela.Label(Janela, text="Hello World!").grid(column=0, row=0)
                
        self.label_texto = tk.Label(self.janela, text="Calculadoria IR 1,2%\nValor da nota")
        self.label_texto.pack()

        self.campo_texto = tk.Entry(self.janela)
        self.campo_texto.pack()

        self.botao_submit = tk.Button(self.janela, text="Submit", command=self.submit_postagem)
        self.botao_submit.pack()

        self.resposta = tk.Label(self.janela, text="Valor IRRF: \n Valor  Líq: ")
        self.resposta.pack()
        


    def submit_postagem(self):
        texto = self.campo_texto.get()
        texto = texto.replace(",",".")
        nota = round((float (texto)*0.012),2)
        liq = (float(texto)-nota)
        t = "Valor IRRF: R$ " + str(nota) + "\n Valor  Líq: R$ " + str(liq)
        t = t.replace(".",",")
        self.resposta.destroy()
        self.resposta = tk.Label(self.janela, text=t)
        self.resposta.pack()
      

    def iniciar(self):
        self.janela.mainloop()

        
#pdfs = ["Relatório Diário de Obra (RDO) n° 1 - 25-03-2022.pdf","Relatório Diário de Obra (RDO) n° 2 - 28-03-2022.pdf  ","Relatório Diário de Obra (RDO) n° 3 - 06-04-2022.pdf  ","Relatório Diário de Obra (RDO) n° 4 - 12-04-2022.pdf  ","Relatório Diário de Obra (RDO) n° 5 - 20-04-2022.pdf  ","Relatório Diário de Obra (RDO) n° 6 - 04-05-2022.pdf  ","Relatório Diário de Obra (RDO) n° 7 - 06-05-2022.pdf  ","Relatório Diário de Obra (RDO) n° 8 - 20-05-2022.pdf  ","Relatório Diário de Obra (RDO) n° 9 - 25-05-2022.pdf  ","Relatório Diário de Obra (RDO) n° 10 - 30-05-2022.pdf  ","Relatório Diário de Obra (RDO) n° 11 - 05-10-2022.pdf  ","Relatório Diário de Obra (RDO) n° 12 - 13-01-2023.pdf  ","Relatório Diário de Obra (RDO) n° 13 - 23-01-2023.pdf  ","Relatório Diário de Obra (RDO) n° 14 - 24-01-2023.pdf  ","Relatório Diário de Obra (RDO) n° 15 - 27-01-2023.pdf  ","Relatório Diário de Obra (RDO) n° 16 - 06-02-2023.pdf  ","Relatório Diário de Obra (RDO) n° 17 - 21-03-2023.pdf  ","Relatório Diário de Obra (RDO) n° 18 - 24-03-2023.pdf"]
pdfs = [os.path.join(".", f) for f in os.listdir(".") if f.endswith('.pdf')]

s = "ADEQUAÇÃO DO VESTIÁRIO DO CAMPO - CONTRATO N°13-2022"
print (s)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
merger.write(s+".pdf")
merger.close()