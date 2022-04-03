from distutils.log import info
from email import message
from tkinter import *
from tkinter import messagebox
from turtle import title

root = Tk()

def btn_click():
  print('refd')

root['bg'] = '#fafafa'
root.title('генератор интересных фактов')
root.wm_attributes('-alpha', 1)
root.geometry('500x500')

canvas = Canvas(root, height=500, width=500)
canvas.pack()

frame = Frame(root, bg='green')
frame.place(relx=0.2, rely=0.2, relwidth=0.5, relheight=0.5)

title = Label(frame, text='Генератор интересных фактов', bg='yellow', font=20)
title.place(relheight=0.2, relwidth=0.2)
title.pack()
btn = Button(frame, text='Новый факт', bg='grey', command=btn_click)
btn.place(relx=0.7, rely=-0.7, relheight=0.3, relwidth=0.3)
btn.pack()


root.mainloop()