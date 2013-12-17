from tkinter import *
from random import*
from numpy import *
import time
from math import*

root = Tk()
root.title ("Matrizes - Adão")
root.resizable(width=False, height=False)

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
    global valor1, valor2,a,b,escala,num,uso
    uso=StringVar() 
    b = StringVar()
    a = StringVar()
    num = StringVar()
    escala = StringVar()
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
    Button(fm2, text='Determinante',command=determinante).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Inversa',command=inversa).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='Matriz * Escalar',command=escalar_mult).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Trocar linha',command=trocar_linha).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Linha de Matriz * Escalar ',command=linha_escalar).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    Button(fm2, text='Subistituir Linha',command=substituir_linha).pack(side=LEFT,padx=2,  pady=3)
    Button(fm2, text='Matriz Quadrada',command=quadrada).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    fm2 = Frame(root)
    resultado =Label(fm2, text="Resultado:",width=8,height=6, bg="blue").pack(side=LEFT,padx=2,  pady=3)
    label1 =Label(fm2, textvariable=final, width=26, height=6, bg="green").pack(side=LEFT,padx=2,  pady=3)
    label1 =Label(fm2, textvariable=uso, width=26, height=6, bg="green")
    Button(fm2, text='  Usar  ',command=utilizar).pack(side=LEFT,padx=2,  pady=3)
    fm2.pack(fill=BOTH, expand=YES)

    
def  substituir_linha():
    escalar=float(escala.get())
    linha=str(num.get())
    l=[]
    x=linha.split(' ')
    for i in range (len(x)):
        y=int(x[i])
        l.append(y)
    aa=eval(a.get())
    bb=eval(b.get())
    radio=(int(v.get()))
    if(radio==1):
        aa[l[0]]=(escalar*(aa[l[1]])+aa[l[0]])
        final.set(aa)
    if(radio==2):
        bb[l[0]]=(escalar*(bb[l[1]]+aa[l[0]]))
        final.set(bb)
def quadrada():
    x=eval(a.get())
    y=eval(b.get())
    radio=(int(v.get()))
    if(radio==1):
        z=sqrt(x)
        final.set(z)
    if(radio==2):
        p=sqrt(y)
        final.set(p)    
    
def determinante():
    x=eval(a.get())
    y=eval(b.get())
    radio=(int(v.get()))
    if(radio==1):
        z=int(linalg.det(x))
        final.set(z)
    if(radio==2):
        p=int(linalg.det(y))
        final.set(p)
def linha_escalar():
    x=eval(a.get())
    y=eval(b.get())
    radio=(int(v.get()))
    escalar=int(escala.get())
    linha=int(num.get())
    if(radio==1):
        valores=x[linha]
        x[linha]=x[linha]*escalar
        final.set(x)
        uso.set(repr(x))
    if(radio==2):
        valores=y[linha]
        y[linha]=y[linha]*escalar
        final.set(y)
        uso.set(repr(y))
def trocar_linha():
    x=eval(a.get())
    y=eval(b.get())
    lista=eval(a.get())
    lista1=eval(b.get())
    radio=(int(v.get()))
    linha1=int(escala.get())
    linha2=int(num.get())
    if(radio==1):
        valores1=x[linha1]
        valores2=x[linha2]
        lista[linha2]=valores1
        lista[linha1]=valores2
        final.set(lista)
        uso.set(repr(lista))
    if(radio==2):
        valores12=y[linha1]
        valores21=y[linha2]
        lista1[linha2]=valores12
        lista1[linha1]=valores21
        final.set(lista1)
        uso.set(repr(lista1))
    print (lista)
def utilizar():
    radio=(int(v.get()))
    if(radio==1):
        a.set(eval(repr(uso.get())))
    if(radio==2):
        b.set(eval(repr(uso.get())))
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
        z=linalg.inv(x)
        final.set(z)
        uso.set(repr(z))
    if(radio==2):
        z=linalg.inv(y)
        final.set(z)
        uso.set(repr(z))
def multiplicacao():
    x=eval(a.get())
    y=eval(b.get())    
    z=(dot(x,y))
    final.set(z)
    uso.set(repr(z))
def transposta():
    x=eval(a.get())
    y=eval(b.get()) 
    radio=(int(v.get()))
    if(radio==1):
        final.set(x.T)
        uso.set(repr(x.T))
    if(radio==2):
        final.set(y.T)
        uso.set(repr(y.T))
def soma():
    x=eval(a.get())
    y=eval(b.get()) 
    radio=(int(v.get()))
    z=(x+y)
    final.set(z)
    uso.set(repr(z))

def escalar_mult():
    z=int(escala.get())
    radio=(int(v.get()))
    if(radio==1):
        x=eval(a.get())
        final.set(x*z)
        uso.set(repr(x*z))
    if(radio==2):
        y=eval(b.get())
        final.set(y*z)
        uso.set(repr(y*z))
def apagar():
    b.delete(0, END )
def apagarum():
    b.delete(0)

e = Entry(root, width=60, state="readonly")
e.insert(0,"...")
def callback():
    print("Não esta pronto");
def hora():
    import relogio
    relogio.tac()
def sair():
    print("sair")
    root.destroy()
def menu():     
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="Ver", menu=filemenu)
    filemenu.add_command(label="Equações", command=callback)
    filemenu.add_command(label="Conversor", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="Sair", command=sair)
    menu.add_cascade(label="Hora", command=hora)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Ajuda", menu=helpmenu)
menu()
desenha()
root.mainloop()
mainloop()
