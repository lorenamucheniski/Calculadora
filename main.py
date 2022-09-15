#importando tkinter
from tkinter import *
from tkinter import ttk

#cores
cor1 = '#080808'    #preta/black
cor2 = '#fafcff'    #branco/white
cor3 = '#243663'    #azul
cor4 = '#797f82'    #cizenta
cor5 = '#f7570c'    #laranja/orange
cor6 = '#fa0505'    #red

janela = Tk()
janela.title('CALCULADORA')
janela.geometry('270x330')
janela.config(bg= cor1)

#criando frames
frame_tela = Frame(janela , width= 270, height= 50, bg= cor3)
frame_tela.grid(row= 0, column= 0)

frame_corpo = Frame(janela, width= 270, height=280)
frame_corpo.grid(row= 1, column= 0)

#criando botões
b1 = Button(frame_corpo, text = 'C', width= 18, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)    #botão Clean
b1.place(x= 0, y= 0)
b2 = Button(frame_corpo, text= '%', width= 6, height=2, bg= cor4, font = 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)    #botão do módulo
b2.place(x= 136, y=0 )
b3 = Button(frame_corpo, text= '/', width= 6, height=2, bg= cor5, fg= cor2, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #botão de divisão
b3.place(x= 202, y= 0)

b4 = Button(frame_corpo, text= '7', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 7
b4.place(x= 0, y= 52)
b5 = Button(frame_corpo, text= '8', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 8
b5.place(x= 70, y= 52)
b6 = Button(frame_corpo, text= '9', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 9
b6.place(x= 136, y= 52)
b7 = Button(frame_corpo, text= '*', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 9
b7.place(x= 202, y= 52)


janela.mainloop()
