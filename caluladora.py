from tkinter import *
from random import*
import time
from math import*
global b

root = Tk()
root.title ("Calculadora - Adão")
root.resizable(width=False, height=False)
def callback():
    import matriz
    matriz.menu()
def relogio():
    import time
    gmt = time.gmtime(time.time())
    fmt = '%a, %d %b %Y %H:%M:%S GMT'
    str = time.strftime(fmt, gmt)
    hdr = 'Date: ' + str
    print (hdr)
def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text=curtime)
    clock.after(200, tick)
def inseresub():
     b.insert(INSERT,"-")
def inseresoma():
     b.insert(INSERT,"+")
def inseremult():
     b.insert(INSERT,"*")
def inserediv():
    b.insert(INSERT,"/")
def insere0():
     b.insert(INSERT,"0")
def insere1():
     b.insert(INSERT,"1")
def insere2():
    b.insert(INSERT,"2")
def insere3():
    b.insert(INSERT,"3")
def insere4():
    b.insert(INSERT,"4")
def insere5():
    b.insert(INSERT,"5")
def insere6():
    b.insert(INSERT,"6")
def insere7():
    b.insert(INSERT,"7")
def insere8():
    b.insert(INSERT,"8")
def insere9():
    b.insert(INSERT,"9")
   
def desenhar():
    global b,valor
    
    Label(root).pack(side=TOP, padx=1, pady=0)
    valor = StringVar()
    b=Entry(root,textvariable=valor,justify=RIGHT,font="Arial 10", width=35, bg="white", fg="red",relief="groove", borderwidth=15)
    b.pack(padx=1)
    iframe1 = Frame(root, relief=SUNKEN)
    v=IntVar()
    Radiobutton(iframe1, text='Graus', variable=v,value=3).pack(side=RIGHT, anchor=W)
    Radiobutton(iframe1, text='Radianos', variable=v,value=2).pack(side=RIGHT, anchor=W)
    iframe1.pack( pady=1, padx=1)
    print(str(v))
    fm = Frame(root)
    compute=Button(fm, text='sin', command=seno).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='cos', command=coseno).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='tan', command=tangente).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='mod').pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='log', command=logaritimo).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='exp', command=exponencial).pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='(').pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text=')').pack(side=LEFT,padx=2,  pady=3)
    Button(fm, text='1/x').pack(side=LEFT,padx=2,  pady=3)    
    fm.pack(fill=BOTH, expand=YES)
    fm.config(cursor='gumby')
 
    fm1 = Frame(root)
    Button(fm1, text='7',fg="red",command=insere7).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='8',fg="red",command=insere8).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='9',fg="red",command=insere9).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='/',fg="blue",command=inserediv).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='x^2').pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='π',command=pi).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='√x').pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='n!',command=factorial).pack(side=LEFT,padx=2,  pady=3)
    Button(fm1, text='exp').pack(side=LEFT,padx=2,  pady=3)
    fm1.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='4',fg="red",command=insere4).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='5',fg="red",command=insere5).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='6',fg="red",command=insere6).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='*',fg="blue",command=inseremult).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='+',command=inseresoma,fg="blue").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='%').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='mod').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='log').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='exp').pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='1',fg="red",command=insere1).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='2',fg="red",command=insere2).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='3',fg="red",command=insere3).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='-',fg="blue",command=inseresub).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='x^y').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='exp').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='mod').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='log').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='exp').pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='=',command=calcular).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='0',command=insere0,fg="red").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='.').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='+',fg="blue").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='limpar').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='exp').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='mod').pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='log').pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)
    
def calcular():
    result = eval(b.get())
    print (b.get(), "=>", result, type(result))
    print(valor.set(result))
def seno():
    import math
    graus = float(b.get())
    angulo = graus * 2 * math.pi / 360.0
    print(valor.set(math.sin(angulo)))
def coseno():
    import math
    print(valor.set('%g' % math.cos(float(b.get()))))
def tangente():
    import math
    print(valor.set('%g' % math.tan(float(b.get()))))
def logaritimo():#certo
    import math
    print(valor.set(math.log10(float(b.get()))))
def exponencial():#certo
    import math
    print(valor.set('%g' % math.exp(float(b.get()))))
def pi():
    import math
    print(valor.set('%g' % math.pi(float(b.get()))))
def factorial():
    import math
    n=float(b.get())
    if n == 0 :
        print(valor.set(1))
    else:
        while(i<=n):
            fact*=i
            i+=1
        return fact
        print(valor.set(fact))

    

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Ver", menu=filemenu)
filemenu.add_command(label="Equações")
filemenu.add_command(label="Matrizes", command=callback)
filemenu.add_command(label="Conversor")
filemenu.add_separator()
filemenu.add_command(label="Sair", command=callback)
menu.add_cascade(label="Hora")
helpmenu = Menu(menu)
menu.add_cascade(label="Ajuda", menu=helpmenu)
helpmenu.add_command(label="Acerca da Calculadora")
desenhar()
relogio()
Nao_Redimensiona(root)
Tamanhos_Limite(root)
root.mainloop()
mainloop()
