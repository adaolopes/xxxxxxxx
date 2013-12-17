import tkinter 
rel=tkinter.Label()
def fechar():
    rel.pack_forget()
    b.pack_forget()
b=tkinter.Button(fg="red",command=fechar)
b['text']='Fechar'
rel.pack()
b.pack()
rel['font']='Helvetica 20 bold'
from time import strftime
def tic(): 
    rel['text']=strftime('%H:%M:%S') 
tic()
def tac():
    tic()
    rel.after(1000,tac)


