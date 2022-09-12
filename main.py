from tkinter import *
from tkinter import ttk

#cores
cor1 = '#080808'    #preta

janela = Tk()
janela.title('CALCULADORA')
janela.geometry('270x330')
janela.config(bg= cor1)


frame_tela = Frame(janela , width= 270, height= 50)
frame_tela.grid(row= 0, column= 0)

janela.mainloop()
