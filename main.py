from tkinter import *
import os

def connect():
    # Use a breakpoint in the code line below to debug your script.
    os.system('plink -v ' + txtfld2.get() + '@' + txtfld.get() + ' -pw ' + txtfld3.get())
    window.destroy()

filin = open("data.txt", "r")
lignes = filin.readlines()

window = Tk()
window.iconbitmap("pi.ico")

window.configure(bg='#edf9e8')

photo = PhotoImage(file="pi.png")
label = Label(window, image=photo, bg='#edf9e8')
label.place(x=116, y=10)

lbl = Label(window, text="Raspberry pi API", fg='#bd0840', bg='#edf9e8', font=("Segoe UI", 16))
lbl.place(x=73, y=90)

txtfld = Entry(window, justify='center', fg='#750427')
txtfld.insert(0, lignes[0].rstrip())
txtfld.place(x=87, y=150)

txtfld2 = Entry(window, justify='center', fg='#750427')
txtfld2.insert(0, lignes[1].rstrip())
txtfld2.place(x=87, y=180)

txtfld3 = Entry(window, justify='center', fg='#750427')
txtfld3.insert(0, lignes[2].rstrip())
txtfld3.place(x=87, y=210)

ButtonCalcul = Button(window, text="Log in", fg='#bd0840', bg='#edf9e8', borderwidth=1, relief="ridge", width=10, font=("Segoe UI", 10))
ButtonCalcul.pack()

ButtonCalcul.config(command=connect)
ButtonCalcul.place(x=111, y=245)

window.title('Raspberry pi')
window.geometry("300x320+10+10")
window.mainloop()