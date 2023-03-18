import tkinter as tk
import tkinter.messagebox
import GUI_gmae
import hashlib
import json

window=tk.Tk()
window.geometry("750x340")
window.title("Log in")

title_lab=tk.Label(window,text="Please Log In",bg="red",font=("Arial", 20))
title_lab.place(x=300,y=30)

userlab=tk.Label(window,text="User name",bg="red",font=("Arial", 20),width=8)
userlab.place(x=150,y=110)

user_entry=tk.Entry(window,width=15,bg="red",font=("Arial", 20))
user_entry.place(x=400,y=110)

sslab=tk.Label(window,text="Password",font=("Arial", 20),bg="red",width=8)
sslab.place(x=150,y=210)

ss_entry=tk.Entry(window,width=15,font=("Arial", 20),bg="red",show="*")
ss_entry.place(x=400,y=210)


def login():
    name=user_entry.get()
    password=hashlib.sha256(ss_entry.get().encode("utf-8")).hexdigest()
    with open("./password.json","r",encoding="utf-8") as f:
        password_list = json.loads(f.read())
        print(password)

    if str(password_list[name]) == str(password) :
        tkinter.messagebox.showinfo(message="Success")
        window.destroy()
        GUI_gmae.game()
    else:
        tkinter.messagebox.showerror(message="Failed")

button_OK=tk.Button(window,text="OK",command=login)
button_OK.place(x=350,y=280,width=100,height=50)

window.mainloop()