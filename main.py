#importando tkinter
from tkinter import *
from tkinter import ttk

#cores
cor1 = '#080808'    #preta/black
cor2 = '#fafcff'    #branco/white
cor3 = '#32b2fc'    #azul
cor4 = '#797f82'    #cizenta
cor5 = '#f7570c'    #laranja/orange

janela = Tk()
janela.title('CALCULADORA')
janela.geometry('270x330')
janela.config(bg= cor1)

#criando frames
frame_tela = Frame(janela , width= 270, height= 50, bg= cor3)
frame_tela.grid(row= 0, column= 0)

frame_corpo = Frame(janela, width= 270, height=280)
frame_corpo.grid(row= 1, column= 0)

janela.mainloop()
