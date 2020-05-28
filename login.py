import BaseDatos
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox

class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Login System")
        self.window.config(bg = "#213c5e")
        self.window.geometry("800x500")
        self.window.maxsize(800,500)
        self.window.minsize(800,500)
        self.user = PhotoImage(file = "people.png")
        self.user = self.user.zoom(2)
        self.user = self.user.subsample(7)
        self.lock = PhotoImage(file = "lock.png")
        self.lock = self.lock.zoom(3)
        self.lock = self.lock.subsample(39)
        self.userlog = PhotoImage(file = "user.png")
        self.userlog = self.userlog.zoom(4)
        self.userlog = self.userlog.subsample(50)

        self.usName = StringVar()
        self.usPass = StringVar()

        
        title = tk.Label(self.window, text = "Iniciar Sesion", font = ("Times",40,"bold"), relief = GROOVE, bg = "#144d87")
        title.place(x = 0, y = 0, relwidth = 1)
        
        logFrame = tk.Frame(self.window, bg = "#AEC5EB")
        logFrame.place(x = 165, y = 93)
        logoLab = Label(logFrame, image = self.user, bd = 0).grid(row = 0, columnspan = 2, pady = 20)

        lblUser = tk.Label(logFrame, text = "Username", image = self.userlog, compound = LEFT, font = ("Times",20,"bold"), bg = "#144d87")
        lblUser.grid(row = 1, column = 0, padx = 20, pady = 10)
        userEntry = tk.Entry(logFrame, bd = 5, textvariable = self.usName, relief = GROOVE, font = ("",15), bg = 'white', fg = "black").grid(row = 1, column = 1, padx = 20)

        lbLock = tk.Label(logFrame, text = "Password", image = self.lock, compound = LEFT, font = ("Times",20,"bold"), bg = "#144d87")
        lbLock.grid(row = 2, column = 0, padx = 20, pady = 10)
        lockEntry = tk.Entry(logFrame, bd = 5, textvariable = self.usPass, relief = GROOVE, font = ("",15), show = "*", bg = "white", fg = "black")
        lockEntry.grid(row = 2, column = 1, padx = 20)

        button = tk.Button(logFrame, text = "Acceder", width = 15, command = lambda: fun(self.usName.get(), self.usPass.get()), font = ("Times",14,"bold"), bg = "#144d87", fg = "white")
        button.grid(row = 3, column = 1, pady = 10)



def fun(usName, usPass):
    if(usName == "" or usPass == ""):
        mBox.showerror("ERROR", "Debes de llenar todos los campos.")
    elif(usName == "Administrador" and usPass == "Password"):
        mBox.showinfo("BIENVENIDO", "BIENVENIDO A LA BASE DE DATOS")
        window.destroy()
        BaseDatos.start()
    else:
        mBox.showerror("ERROR", "Los datos son incorrectos")


if __name__ == "__main__":
    window = tk.Tk()

    w = 800
    h = 500
    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    obj = Login(window)
    window.mainloop()

