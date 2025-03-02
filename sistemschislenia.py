import tkinter as tk
from tkinter import *
from tkinter import messagebox
def show_result():
    number = entry.get()
    num = int(number)
    a=bin(num)
    b=oct(num)
    c=hex(num)
    g=[a,b,c]
    label_result.config(text=f"Результат: {g}")
   
   
   
window=tk.Tk()
window.title("Программа для перевода чисел в различные С.С")
window.geometry('500x550')

lbl=Label(window, text='Введите число:')
lbl.grid(column=0,row=0)

entry=tk.Entry(window)
entry.grid(column=1,row=1)


       
btn=Button(window,text="Нажмите после ввода значения",command=show_result)
btn.grid(column=3,row=1)

label_result =  tk.Label(window,text="Результат: ")
label_result.grid(column=3,row=3)
