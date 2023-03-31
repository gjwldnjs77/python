import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("BMI 계산기")
window.geometry("640x400+300+300")
window.resizable(False, False)

he = tkinter.StringVar()
we = tkinter.StringVar()

def btn_click() :
    h_value = float(he.get())
    w_value = float(we.get())
    h_value = h_value * 0.01
    result = w_value / (h_value * h_value)
    tkinter.messagebox.shwinfo("결과", result)

titLabel = tkinter.Label(window, text="체질량질수 계산기")
titLabel.config(font=("Arial", 25))
titLabel.config(fg="red")
titLabel.pack()

heightLavel = tkinter.Label(window, text="신장")
heightLavel.config(font=("Arial", 24))
heightLavel.place(x=30, y=70)

heightEntry = tkinter.Entry(window, textvariable=he)
heightEntry.place(x=120, y=82)

weightLabel = tkinter.Label(window, text="체중")
weightLabel.config(font=("Arial", 24))
weightLabel.place(x=30, y=120)

weightEntry = tkinter.Entry(window, textvariable=he)
weightEntry.place(x=120, y=132)               

btn = tkinter.Button(window, text="확인", command=btn_click)
btn.place(x=30, y=250)

window.mainloop
