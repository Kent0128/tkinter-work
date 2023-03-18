from tkinter import *
from tkinter import messagebox
from cal import calculator
from tictactoe import TicTacToe



#def openNewWindow():
#    root.withdraw()
#    newWindow = Toplevel(root)
#    newWindow.title("New Window")
#    newWindow.geometry("400x300")
#    Label(newWindow, text="Calculator").pack()
#    btn = Button(newWindow,
#                text="Close",
#                command=lambda:newWindowClose(newWindow))
#    btn.pack(pady=5)
def game():
    root=Tk()
    root.title("GUI Demo")
    root.geometry("500x250+200+100")
    
    def chess():
        root1=Tk()
        TicTacToe(root1)
        root1.mainloop()

    def CAL():
        root2=Tk()
        calculator(root2)
        root2.mainloop()

    def newWindowClose(self):
        root.deiconify()
        self.destroy()

    labl=Label(root,text="Please choose your ideal function")
    btn1=Button(root,
            text="Calculator",
            command=CAL)
    btn2=Button(root,
                text="TicTacToe",
                command=chess)
    btn3=Button(root,
                text="Close",
                command=lambda:newWindowClose(root))

    labl.pack(pady=10)
    btn1.pack(pady=10)
    btn2.pack(pady=10)
    btn3.pack(pady=10)

    root.mainloop()