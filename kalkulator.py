from tkinter import *

window = Tk()
window.geometry("250x400")
window.title("Калькулятор")
window.config(background="white")

expression=""



result=StringVar()
vod=Entry(textvariable=result)
vod.grid(columnspan=4,ipadx=70)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression=""
    except:
        result.set("error")
        expression= total

def converter():
    actual_coin=list_of_coins.get(list_of_coins.curselection())
    umn=1
    if actual_coin =="Rub to Dollar":
        umn=0.01
    elif actual_coin =="Dollar to Rub":
        umn=88
    elif actual_coin == "Rub to Euro":
        umn=0.01
    elif actual_coin =="Euro to Rub":
        umn=92

    global expression
    total = str(eval(expression) * umn)
    result.set(total)
    expression= total







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

plus = Button(text="+",height=1,width=7,command=lambda: press_num("+"))
plus.grid(row=5,column=0)

minus = Button(text="-",height=1,width=7,command=lambda: press_num("-"))
minus.grid(row=5,column=2)

equal = Button(text="=",height=1,width=7,command=equalpress)
equal.grid(row=6,column=1)

umn = Button(text="*",height=1,width=7,command=lambda : press_num("*"))
umn.grid(row=6,column=2)

dele = Button(text="/",height=1,width=7,command=lambda : press_num("/"))
dele.grid(row=6,column=0)


coins=["Rub to Dollar","Dollar to Rub","Rub to Euro","Euro to Rub"]
list_of_coins = Listbox(width=15,height=5)
list_of_coins.grid(row=7,column=1)
for coin in coins:
    list_of_coins.insert(0, coin)

convert = Button(text="convert",height=1,width=7,command=converter)
convert.grid(row=8,column=1)


window.mainloop()