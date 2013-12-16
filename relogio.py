import tkinter 
rel=tkinter.Label()
rel['text']='19:14:15'
rel.pack()
rel['font']='Helvetica 20 bold'
from time import strftime
def tic(): 
    rel['text']=strftime('%H:%M:%S') 
tic()
def tac():
    tic()
    rel.after(1000,tac)
