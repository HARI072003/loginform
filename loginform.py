from tkinter import *
from tkinter import messagebox
def login():
    username=entry1.get()
    password=entry2.get()
    if (username==""and password==""):
        messagebox.showinfo("","Blank not aloowed")
    elif (username=="Hari1916"and password=="hp1916"):
        messagebox.showinfo("","login succesfull completed")
    else:
        messagebox.showinfo("","incorrect username and password")
root=Tk()
root.title("Login Form")
root.geometry("900x680")

global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)
entry1=Entry(root,bd=5,bg="light blue")
entry1.place(x=140,y=20)
entry2=Entry(root,bd=5,bg="light blue")
entry2.place(x=140,y=70)
Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)
root.mainloop()
