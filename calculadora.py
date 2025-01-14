from tkinter import *
from tkinter import ttk

cor1= "#1e1f1e"
cor2= "#feffff"
cor3= "#38576b"
cor4= "#ECEFF1"
cor5= "#FFAB40"


janela =Tk()
janela.title("calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)


frame_tela= Frame(janela, width=235, height=50, bg= cor3)
frame_tela.grid(row=0, column=0)

frame_corpo= Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

Valor_texto= StringVar()

def entrada(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    
    Valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    Valor_texto.set(str(resultado))

def limpar():
    global todos_valores
    todos_valores = ""
    Valor_texto.set("")






App_label = Label(frame_tela, textvariable= Valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
App_label.place(x=0,y=0)


btn_1= Button(frame_corpo,command= limpar, text="C", width=11,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_1.place(x=0,y=0)
btn_2= Button(frame_corpo,command= lambda: entrada('%'), text="%", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_2.place(x=118,y=0)
btn_3= Button(frame_corpo, command= lambda: entrada('/'), text="/", width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_3.place(x=177,y=0)

btn_4= Button(frame_corpo,command= lambda: entrada('7'), text="7", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_4.place(x=0,y=52)
btn_5= Button(frame_corpo,command= lambda: entrada('8'), text="8", width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_5.place(x=59,y=52)
btn_6= Button(frame_corpo,command= lambda: entrada('9'), text="9", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_6.place(x=118,y=52)
btn_7= Button(frame_corpo,command= lambda: entrada('*'), text="X", width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_7.place(x=177,y=52)

btn_8= Button(frame_corpo,command= lambda: entrada('4'), text="4", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_8.place(x=0,y=104)
btn_9= Button(frame_corpo,command= lambda: entrada('5'), text="5", width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_9.place(x=59,y=104)
btn_10= Button(frame_corpo,command= lambda: entrada('6'), text="6", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_10.place(x=118,y=104)
btn_11= Button(frame_corpo,command= lambda: entrada('-'), text="-", width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_11.place(x=177,y=104)

btn_12= Button(frame_corpo,command= lambda: entrada('1'), text="1", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_12.place(x=0,y=156)
btn_13= Button(frame_corpo,command= lambda: entrada('2'), text="2", width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_13.place(x=59,y=156)
btn_14= Button(frame_corpo,command= lambda: entrada('3'), text="3", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_14.place(x=118,y=156)
btn_15= Button(frame_corpo,command= lambda: entrada('+'), text="+", width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_15.place(x=177,y=156)

btn_16= Button(frame_corpo,command= lambda: entrada('0'), text="0", width=11,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_16.place(x=0,y=208)
btn_17= Button(frame_corpo,command= lambda: entrada('.'), text=".", width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_17.place(x=118,y=208)
btn_18= Button(frame_corpo,command= calcular, text="=", width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_18.place(x=177,y=208)





janela.mainloop()