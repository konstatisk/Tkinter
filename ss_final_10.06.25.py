from tkinter import Tk, Label
from tkinter import *

window=Tk()
window.geometry("300x500")
window.title("Программа для перевода чисел в различные С.С")
window.config(background="white")
window.resizable(False, False)

expression=""

result=StringVar()
vod=Entry(textvariable=result)
vod.grid(columnspan=4,ipadx=70)


def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def press_ss(num):
    global expression
    num=num.replace("0x","")
    num = num.replace("0b","")
    num = num.replace("0o","")
    expression += str(num)
    result.set(num)

def clear():
    vod.delete("0",END)
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = ""
    except:
        result.set("error")
        expression = total


btn1=Button(text="1",height=1,width=7,command=lambda: press_num(1))
btn1.grid(row=2,column=0)

btn2=Button(text="2",height=1,width=7,command=lambda: press_num(2))
btn2.grid(row=2,column=1)

btn3=Button(text="3",height=1,width=7,command=lambda: press_num(3))
btn3.grid(row=2,column=2)

btn4=Button(text="4",height=1,width=7,command=lambda: press_num(4))
btn4.grid(row=3,column=0)

btn5=Button(text="5",height=1,width=7,command=lambda: press_num(5))
btn5.grid(row=3,column=1)

btn6=Button(text="6",height=1,width=7,command=lambda: press_num(6))
btn6.grid(row=3,column=2)

btn7=Button(text="7",height=1,width=7,command=lambda: press_num(7))
btn7.grid(row=4,column=0)

btn8=Button(text="8",height=1,width=7,command=lambda: press_num(8))
btn8.grid(row=4,column=1)

btn9=Button(text="9",height=1,width=7,command=lambda: press_num(9))
btn9.grid(row=4,column=2)

btn0=Button(text="0",height=1,width=7,command=lambda: press_num(0))
btn0.grid(row=5,column=1)

btn_hex=Button(text="16 C.C", height=1,width=7,command=lambda: press_ss(hex(int(result.get()))))
btn_hex.grid(row=5,column=0)

btn_oct=Button(text="8 C.C", height=1,width=7,command=lambda: press_ss(oct(int(result.get()))))
btn_oct.grid(row=5,column=2)

btn_bin = Button(text="2 C.C", height=1, width=7, command=lambda: press_ss(bin(int(result.get()))))
btn_bin.grid(row=6,column=1)

btn_clear = Button(text="Очистить",height=1,width=7,command=clear)
btn_clear.grid(row=6,column=2)

window.mainloop()
