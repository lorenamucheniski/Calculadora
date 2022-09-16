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
janela.geometry('280x310')
janela.config(bg= cor1)

#criando frames
frame_tela = Frame(janela , width= 280, height= 50, bg= cor3)
frame_tela.grid(row= 0, column= 0)

frame_corpo = Frame(janela, width= 280, height=280)
frame_corpo.grid(row= 1, column= 0)

#criando label
app_label = Label(frame_tela, text= '123456789', width= 18, height=2, padx= 7, relief= FLAT, anchor= 'e', justify= RIGHT, font= 'Ivy 19', bg= cor3, fg= cor2)
app_label.place(x= 0, y= 0)

#criando botões
b1 = Button(frame_corpo, text = 'C', width= 13, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)    #botão Clean
b1.place(x= 0, y= 0)
b2 = Button(frame_corpo, text= '%', width= 6, height=2, bg= cor4, font = 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)    #botão do módulo
b2.place(x= 140, y=0 )
b3 = Button(frame_corpo, text= '/', width= 6, height=2, bg= cor5, fg= cor2, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #botão de divisão
b3.place(x= 210, y= 0)

b4 = Button(frame_corpo, text= '7', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 7
b4.place(x= 0, y= 52)
b5 = Button(frame_corpo, text= '8', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 8
b5.place(x= 70, y= 52)
b6 = Button(frame_corpo, text= '9', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #número 9
b6.place(x= 140, y= 52)
b7 = Button(frame_corpo, text= '*', width= 6, height= 2, bg= cor5, fg= cor2, font= 'Ivy 13 bold', relief= RAISED, overrelief=  RIDGE)     #sinal de multiplicação
b7.place(x= 210, y= 52)

b8 = Button(frame_corpo, text= '4', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)      #número 4
b8.place(x= 0, y= 104)
b9= Button(frame_corpo, text= '5', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)       #número 5
b9.place(x=70, y=104 )
b10 = Button(frame_corpo, text= '6', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 6
b10.place(x= 140, y=104)
b11 = Button(frame_corpo, text= '-', width= 6, height= 2, bg= cor5, fg= cor2, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)       #sinal de subtração
b11.place(x= 210, y=104)

b12 = Button(frame_corpo, text= '1', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 1
b12.place(x=0, y=156)
b13 = Button(frame_corpo, text= '2', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 2
b13.place(x= 70, y= 156)
b14 = Button(frame_corpo, text= '3', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 3
b14.place(x= 140, y= 156)
b15 = Button(frame_corpo, text= '+', width= 6, height= 2, bg= cor5, fg= cor2, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)       #sinal de adição
b15.place(x= 210, y= 156)

b16 = Button(frame_corpo, text= '0', width= 13, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 0
b16.place(x=0, y=208)
b17 = Button(frame_corpo, text= '.', width= 6, height= 2, bg= cor4, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 2
b17.place(x= 140, y= 208)
b18 = Button(frame_corpo, text= '=', width= 6, height= 2, bg= cor5, fg= cor2, font= 'Ivy 13 bold', relief= RAISED, overrelief= RIDGE)     #número 3
b18.place(x= 210, y= 208)


janela.mainloop()
