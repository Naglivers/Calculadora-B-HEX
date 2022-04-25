from tkinter import *
from tkinter import font

from setuptools import Command


#cores
cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja
cor6 = "#808080" #cinza2


janela = Tk()
janela.title("Binario")
janela.geometry("235x318")
janela.config(bg=cor1)

#frame
janela_frame = Frame(janela, width=235, height=50, bg = cor3)
janela_frame.grid(row=0, column=0 ) 

corpo_frame = Frame(janela, width=235, height=268)
corpo_frame.grid(row=1, column=0 ) 

#label

valor_text = StringVar()

app_label = Label(janela_frame, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'),bg=cor3)
app_label.place(x=0, y=0)

#variaveis

todos_valores = ''

#funcoes

def entrar_valores(event):

     global todos_valores
     
     todos_valores = todos_valores + str(event)

    #passando resultado pra tela
     valor_text.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_text.set(str(resultado))
    
def clean():
    global todos_valores
    todos_valores=""
    valor_text.set("")

#botao

b_C = Button(corpo_frame, command= clean, text='C', width=5, height=2, font=('Ivy 13 bold'), bg=cor5, relief=RAISED, overrelief=RIDGE)
b_C.place(x=0, y=0)
b_DEC = Button(corpo_frame, command= lambda: entrar_valores('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), bg=cor5, relief=RAISED, overrelief=RIDGE)
b_DEC.place(x=59, y=0)
b_BIN = Button(corpo_frame, command= lambda: entrar_valores('bin'), text='BIN', width=5, height=2, font=('Ivy 13 bold'), bg=cor5, relief=RAISED, overrelief=RIDGE)
b_BIN.place(x=118, y=0)
b_DEC = Button(corpo_frame, command= lambda: entrar_valores('0b'), text='DEC', width=5, height=2, font=('Ivy 13 bold'), bg=cor5, relief=RAISED, overrelief=RIDGE)
b_DEC.place(x=177, y=0)


b_9 = Button(corpo_frame, command= lambda: entrar_valores('9'), text='9', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=52)
b_8 = Button(corpo_frame, command= lambda: entrar_valores('8'), text='8', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
b_7 = Button(corpo_frame, command= lambda: entrar_valores('7'), text='7', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_7.place(x=118, y=52)
b_mais = Button(corpo_frame, command= lambda: entrar_valores('+'), text='+', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_mais.place(x=177, y=52)

b_6 = Button(corpo_frame, command= lambda: entrar_valores('6'), text='6', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_6.place(x=0, y=104)
b_5 = Button(corpo_frame, command= lambda: entrar_valores('5'), text='5', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
b_4 = Button(corpo_frame, command= lambda: entrar_valores('4'), text='4', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_4.place(x=118, y=104)
b_menos = Button(corpo_frame, command= lambda: entrar_valores('-'), text='-', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_menos.place(x=177, y=104)

b_3 = Button(corpo_frame, command= lambda: entrar_valores('3'), text='3', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_3.place(x=0, y=156)
b_2 = Button(corpo_frame, command= lambda: entrar_valores('2'), text='2', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)
b_1 = Button(corpo_frame, command= lambda: entrar_valores('1'), text='1', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_1.place(x=118, y=156)
b_igual = Button(corpo_frame, command= calcular, text='=', width=5, height=2, font=('Ivy 13 bold'), bg=cor4, relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=156)

b_0 = Button(corpo_frame, command= lambda: entrar_valores('0'), text='0', width=11, height=3, font=('Ivy 13 bold'), bg=cor6, relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)
b_chav1 = Button(corpo_frame, command= lambda: entrar_valores('('), text='(', width=5, height=3, font=('Ivy 13 bold'), bg=cor6, relief=RAISED, overrelief=RIDGE)
b_chav1.place(x=118, y=208)
b_chav2 = Button(corpo_frame, command= lambda: entrar_valores(')'), text=')', width=5, height=3, font=('Ivy 13 bold'), bg=cor6, relief=RAISED, overrelief=RIDGE)
b_chav2.place(x=177, y=208)

janela.mainloop()
