from tkinter import *
from random import*
from numpy import *
import time
from math import*

root = Tk()
root.title ("Matrizes - Adão")
root.resizable(width=False, height=False)
def callback():
    print ("called the callback!")
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
def especial():
    y=b.get() 
    import funcao_especial
    res=funcao_especial.funcao(float(y))
    print(valor.set(res))
  
def matriz_identidade():
    global linha, coluna
    x=int(valor1.get())
    z=int(valor2.get())
    radio=(int(v.get()))
    y = eye(x,z)
    if(radio==1):
        a.set(repr(y))
    if(radio==2):
        b.set(repr(y))
def nans(shape, dtype=float):
    a = empty(shape, dtype)
    a.fill(1)
    return a
def matriz_uns():
    global linha, coluna
    x=int(valor1.get())
    z=int(valor2.get())
    radio=(int(v.get()))
    y = ones((x,z))
    if(radio==1):
        a.set(repr(y))
    if(radio==2):
        b.set(repr(y))

def matriz_zero():
    global linha, coluna
    x=int(valor1.get())
    z=int(valor2.get())
    radio=(int(v.get()))
    y = zeros((x,z))
    if(radio==1):
        a.set(repr(y))
    if(radio==2):
        b.set(repr(y))
        
    
def result(n):
    final=8
    
def desenha():
    global valor1, valor2,a,b,escala,num
    b = StringVar()
    a = StringVar()
    num = IntVar()
    escala = IntVar()
    valor1 = IntVar()
    valor2 = IntVar()
    iframe1 = Frame(root, relief=SUNKEN)
    fm = Frame(root)
    fm2 = Frame(root)
    Label(fm, text="Linha",width=9, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    Label(fm, text="Coluna",width=10, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    Label(fm, text="Escalar",width=10, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    Label(fm, text="Número",width=11, bg="blue").pack(side=LEFT,padx=1,  pady=3)
    fm.pack(fill=BOTH, expand=YES)
    fm.config(cursor='gumby')
    global linha, coluna
    fm1 = Frame(root)
    global final, label1,escalar,v,numero
    final=StringVar()    
    linha=Entry(fm1,textvariable=valor1,font="Arial 10", width=9, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=3)
    coluna=Entry(fm1,textvariable=valor2,font="Arial 10", width=11, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=3)
    escalar=Entry(fm1,textvariable=escala,font="Arial 10", width=10, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=3)
    numero=Entry(fm1,textvariable=num,font="Arial 10", width=11, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=3)
    fm1.pack(fill=BOTH, expand=YES)

    Label(fm2, text="Matriz A:",width=8, bg="red").pack(side=LEFT,padx=2,  pady=3)
    v = IntVar()
    Radiobutton(fm2, variable=v, value=1).pack(side=LEFT,  pady=3)
    matriza=Entry(fm2,textvariable=a,font="Arial 10", width=31, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=4)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Label(fm2, text="Matriz B:",width=8, bg="red").pack(side=LEFT,padx=2,  pady=3)
    Radiobutton(fm2, variable=v, value=2).pack(side=LEFT,  pady=3)
    matrizb=Entry(fm2,textvariable=b,font="Arial 10", width=31, bg="white", fg="red").pack(side=LEFT,anchor=N,padx=2,  pady=4)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='Zeros',command=matriz_zero).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Identidade',command=matriz_identidade).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Uns',command=matriz_uns).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Multiplicação Matriz',command=multiplicacao).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Soma',command=soma).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)
    
    fm2 = Frame(root)
    Button(fm2, text='Transposta',command=transposta).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Exponencial',command=exponencial).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Determinante',command=matriz_uns).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Inversa',command=inversa).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='Multiplicação Escalar',command=escalar_mult).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Trocar linha',command=trocar_linha).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    resultado =Label(fm2, text="Resultado:",width=8,height=6, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    label1 =Label(fm2, textvariable=final, width=26, height=6, bg="green").pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='  Utilizar  ',command=utilizar).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

def trocar_linha():
    x=eval(a.get())
    y=eval(b.get())
    radio=(int(v.get()))
    linha1=int(escala.get())
    linha2=int(num.get())
    if(radio==1):
        x[linha1], x[linha2] = x[linha1], x[linha2]
        final.set(x)
    if(radio==2):
        y[linha1], y[linha2] = y[linha1], y[linha2]
        final.set(y)
def utilizar():
    radio=(int(v.get()))
    if(radio==1):
        a.set(eval(final.get()))
    if(radio==2):
        b.set(eval(final.get()))
def exponencial():
    x=eval(a.get())
    y=eval(b.get())
    z=int(num.get())
    print(z)
    print(x)
    radio=(int(v.get()))
    if(radio==1):
        print(dot(x,x))
        for i in range(0, z):
            dot(x,x)
            z +=1
        final.set(x)
    if(radio==2):
        for i in range(0, z):
            y=(dot(y,y))
            z +=1

        final.set(x)
from numpy import *
def inversa():
    
    x=eval(a.get())
    y=eval(b.get()) 
    radio=(int(v.get()))
    if(radio==1):
        print(x.I)
       
        """final.set((x.I))"""
    if(radio==2):
        """final.set((y.I))"""
def multiplicacao():
    x=eval(a.get())
    y=eval(b.get())    
    z=(dot(x,y))
    final.set(repr(z))
def transposta():
    x=eval(a.get())
    y=eval(b.get()) 
    radio=(int(v.get()))
    if(radio==1):
        final.set(x.T)
    if(radio==2):
        final.set(y.T)
def soma():
    x=eval(a.get())
    y=eval(b.get()) 
    radio=(int(v.get()))
    if(radio==1):
        final.set(x+y)
    if(radio==2):
        final.set(x+y)
def escalar_mult():
    z=int(escala.get())
    radio=(int(v.get()))
    if(radio==1):
        x=eval(a.get())
        final.set(x*z)
    if(radio==2):
        y=eval(b.get())
        final.set(y*z)
def apagar():
    b.delete(0, END )
def apagarum():
    b.delete(0)

e = Entry(root, width=60, state="readonly")
e.insert(0,"...")
def menu():     
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="Ver", menu=filemenu)
    filemenu.add_command(label="Equações", command=callback)
    filemenu.add_command(label="Matrizes", command=callback)
    filemenu.add_command(label="Conversor", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="Sair", command=callback)
    menu.add_cascade(label="Hora")
    helpmenu = Menu(menu)
    menu.add_cascade(label="Ajuda", menu=helpmenu)
menu()
desenha()
root.mainloop()
mainloop()
