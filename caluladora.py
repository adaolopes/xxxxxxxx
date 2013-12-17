from tkinter import *
from random import*
import time
from math import*
global b

root = Tk()
root.title ("Calculadora - Adão")
root.resizable(width=False, height=False)
def matriz():
    import matriz
    matriz.menu()
def hora():
    import relogio
    relogio.tac()
def sair():
    print("sair")
    root.destroy()

def inseresub():
     b.insert(INSERT,"-")
def inseresoma():
     b.insert(INSERT,"+")
def inseremult():
     b.insert(INSERT,"*")
def inserediv():
    b.insert(INSERT,"/")
def insere0():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"0")
    else:
        b.insert(INSERT,"0")
def insere1():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"1")
    else:
        b.insert(INSERT,"1")
def insere2():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"2")
    else:
        b.insert(INSERT,"2")
def insere3():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"3")
    else:
        b.insert(INSERT,"3")
def insere4():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"4")
    else:
        b.insert(INSERT,"4")
def insere5():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"5")
    else:
        b.insert(INSERT,"5")
def insere6():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"6")
    else:
        b.insert(INSERT,"6")
def insere7():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"7")
    else:
        b.insert(INSERT,"7")
def insere8():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"8")
    else:
        b.insert(INSERT,"8")
def insere9():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"9")
    else:
        b.insert(INSERT,"9")
def inser():
    b.insert(INSERT,".")
def pare():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"(")
    else:
        b.insert(INSERT,"(")

def pare2():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,")")
    else:
        b.insert(INSERT,")")
def insere_exp():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"exp(")
    else:
        b.insert(INSERT,"exp(")
def inserir_log():
    x=b.get()
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,"log10(")
    else:
        b.insert(INSERT,"log10(")
def especial():
    y=b.get() 
    import funcao_especial
    res=funcao_especial.funcao(float(y))
    print(valor.set(res))
def desenhar():
    global b,valor
    Label(root).pack(side=TOP, padx=1, pady=0)
    valor = StringVar()
    b=Entry(root,textvariable=valor,justify=RIGHT,font="Arial 10", width=34, bg="white", fg="red",relief="groove", borderwidth=15)
    b.pack(padx=1)
    iframe1 = Frame(root, relief=SUNKEN)
    v=IntVar()
    Radiobutton(iframe1, text='Graus', variable=v,value=3).pack(side=RIGHT, anchor=W)
    Radiobutton(iframe1, text='Radianos', variable=v,value=2).pack(side=RIGHT, anchor=W)
    iframe1.pack( pady=1, padx=1)
    print(v)
    fm = Frame(root)
    compute=Button(fm, text='sin', command=seno).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='cos', command=coseno).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='tan', command=tangente).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='mod').pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='log', command=logaritimo).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='exp', command=exponencial).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='(',command=pare).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text=')',command=pare2).pack(side=LEFT,padx=3,  pady=3)
    Button(fm, text='1/x').pack(side=LEFT,padx=2,  pady=3)    
    fm.pack(fill=BOTH, expand=YES)
    fm.config(cursor='gumby')
 
    fm1 = Frame(root)
    Button(fm1, text='7',fg="red",command=insere7).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='8',fg="red",command=insere8).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='9',fg="red",command=insere9).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='/',fg="blue",command=inserediv).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='e',command=e).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='π',command=pi).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='√x',command=quadrado).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text=' inserir exponencial',command=insere_exp).pack(side=LEFT,padx=2,  pady=3)
    fm1.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='4',fg="red",command=insere4).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='5',fg="red",command=insere5).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='6',fg="red",command=insere6).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='*',fg="blue",command=inseremult).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='+',command=inseresoma,fg="blue").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='inserir logaritimo',command=inserir_log).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='n!',command=factorial).pack(side=LEFT,padx=2,  pady=3)
    
    Button(fm2, text='x^2').pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='1',fg="red",command=insere1).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='2',fg="red",command=insere2).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='3',fg="red",command=insere3).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='-',fg="blue",command=inseresub).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text=' função especial ',command=especial).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='x^y').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='%').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='%').pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='=',command=calcular).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='0',command=insere0,fg="red").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='.',command=inser).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='+',fg="blue").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='limpar',command=limpar).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='exp').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='mod').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='log').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='log').pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)
def limpar():
    b.delete(0, END)    
def calcular():
    try:
        result = eval(b.get())
        print (b.get(), "=>", result, type(result))
        print(valor.set(result))      
    except:
        valor.set("Error")

def seno():
    import math
    try:
        graus = float(b.get())
        angulo = graus * 2 * math.pi / 360.0
        valor.set(math.sin(angulo))
    except:
        valor.set("Error")   
def coseno():
    import math
    try:
        print(valor.set(math.cos(float(b.get()))))
    except:
        valor.set("Error")
def tangente():
    import math
    try:
        print(valor.set(math.tan(float(b.get()))))
    except:
        valor.set("Error")
def logaritimo():#certo
    import math
    try:
       print(valor.set(math.log10(float(b.get()))))
    except:
        valor.set("Error")
def exponencial():#certo
    import math
    try:
        print(valor.set(math.exp(float(b.get()))))
    except:
        valor.set("Error")
def quadrado():#certo
    import math
    try:
        print(valor.set(math.sqrt(float(b.get()))))
    except:
        valor.set("Error")
def pi():
    x=b.get()
    import math
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,math.pi)
    else:
        b.insert(INSERT,math.pi)
def e():
    x=b.get()
    import math
    if(x=="Error"):
        b.delete(0, END)  
        b.insert(INSERT,math.e)
    else:
        b.insert(INSERT,math.e)
def factorial():    
    try:
        import math
        print(valor.set(math.factorial(int(b.get()))))
    except:
        valor.set("Error")
def menu_principal():
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="Ver", menu=filemenu)
    filemenu.add_command(label="Equações")
    filemenu.add_command(label="Matrizes", command=matriz)
    filemenu.add_command(label="Conversor")
    filemenu.add_separator()
    filemenu.add_command(label="Sair", command=sair)
    menu.add_cascade(label="Hora", command=hora)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Ajuda", menu=helpmenu)
    helpmenu.add_command(label="Acerca da Calculadora")
    desenhar()
menu_principal()
root.mainloop()
mainloop()
