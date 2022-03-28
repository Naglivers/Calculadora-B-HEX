from tkinter import *


#cores
cor1 = "#1e1f1e" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja


janela = Tk()
janela.title("Binario")
janela.geometry("235x318")
janela.config(bg=cor1)

#frame
janela_frame = Frame(janela, width=235, height=50, bg = cor3)
janela_frame.grid(row=0, column=0 ) 

corpo_frame = Frame(janela, width=235, height=268)
corpo_frame.grid(row=1, column=0 ) 

#botao

b_1 = Button(corpo_frame, text='1', width=11, height=2, bg=cor5)
b_1.place(x=0, y=0)


# https://www.youtube.com/watch?v=i24MxljM-Bw
# base pra janela

janela.mainloop()
