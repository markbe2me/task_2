import tkinter as tkt
import math

def calc(oper):
    global goo
    if oper == 'C':
        goo = '0'
    elif oper == '=':
        goo = str(eval(goo))
    elif oper == 'sin':
        goo = str(math.sin(float(goo)))
    elif oper == 'cos':
        goo = str(math.cos(float(goo)))
    elif oper == 'tan':
        goo = str(math.tan(float(goo)))
    elif oper == 'ctg':
        goo = str(math.log1p(float(goo)))
    elif oper == 'log':
        goo = str(math.log10(float(goo)))
    elif oper == 'ln':
        goo = str(math.log(float(goo)))
    elif oper == 'Bin':
        goo = str(bin(int(goo)))
    else:
        if goo == '0':
            goo = ''
        goo += oper
    label_txt.configure(text=goo)
    
wd =tkt.Tk()
wd.title('Калькулятор')
wd.geometry('500x650')
wd.configure(bg = 'green')
buts= ['C','-', '+', '=',
       '1','2','3', '/','4','5','6','*',
       '7','8','9','0','sin','cos','tan',
       'ctg','log','ln','%','Bin',]
x = 18
y = 140
for button in buts:
    get_lbl = lambda x=button: calc(x)
    tkt.Button(text= button, bg = 'yellow', font=('Times New Roman', 20), command = get_lbl).place(x =x , y=y, width = 115, height = 80)
    x+= 120
    if x> 400:
        x= 20
        y+= 85
goo = '0'
label_txt= tkt.Label(text= goo, font = ('Times New Roman',35, 'bold'), bg = 'grey',fg = 'white')
label_txt.place(x = 11, y = 50)
wd.mainloop()
