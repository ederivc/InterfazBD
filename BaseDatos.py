import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *

def main():
    window.mainloop()


def OnDoubleClick(event):
    if(event==0):
        ShowAgregar(0)
    if(event==1):
        ShowAgregar(1)
    if(event==2):
        ShowAgregar(2)
    if(event==3):
        ShowAgregar(3)
    return

def LabelEnter(event):
    print(event)
    empleado.config(background='#FFFFFF')

def LabelLeave(event):
    empleado.config(background='#A4A4A4')

def ShowAgregar(index):
    x=0
    while(x<len(interface_agregar)):
        if x!=index:
            interface_agregar[x].pack_forget()
        x+=1
    interface_agregar[index].pack(fill=tk.BOTH, expand=True)



window = tk.Tk()
window.title('Base de datos')
window.minsize(1080, 600)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=4)



options= tk.Frame(window, bg="#080808")
options.grid(row=0,column=0, sticky='NSWE')
options.columnconfigure(0, weight=1)

display=tk.Frame(window, bg="#04517D")
display.grid(row=0,column=1, sticky='NSWE')


interface_agregar= []

for x in range(4):
    interface_agregar.append(tk.Frame(display))


#Empleado
interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[0].configure(bg='purple')
interface_agregar[0].pack_forget()

ttk.Label(interface_agregar[0], text="ID:").grid(row=0, column=0)
ttk.Label(interface_agregar[0], text="Nombre:").grid(row=2, column=0)
ttk.Label(interface_agregar[0], text="RFC:").grid(row=4, column=0)
ttk.Label(interface_agregar[0], text="Fecha de nacimiento:").grid(row=6, column=0)
ttk.Label(interface_agregar[0], text="Fecha de Ingreso:").grid(row=8, column=0)
ttk.Label(interface_agregar[0], text="Lugar de nacimiento").grid(row=10, column=0)
ttk.Label(interface_agregar[0], text="Ciudad:").grid(row=12, column=0)
ttk.Label(interface_agregar[0], text="Estado:").grid(row=14, column=0)
ttk.Label(interface_agregar[0], text="País:").grid(row=16, column=0)
ttk.Label(interface_agregar[0], text="Dirección:").grid(row=18, column=0)
ttk.Label(interface_agregar[0], text="Calle:").grid(row=20, column=0)
ttk.Label(interface_agregar[0], text="Colonia:").grid(row=22, column=0)
ttk.Label(interface_agregar[0], text="CP:").grid(row=24, column=0)
ttk.Label(interface_agregar[0], text="Ciudad:").grid(row=26, column=0)
ttk.Label(interface_agregar[0], text="Teléfono:").grid(row=28, column=0)
ttk.Label(interface_agregar[0], text="Sueldo:").grid(row=30, column=0)

id_ = tk.StringVar()
nombreCapturado = ttk.Entry(interface_agregar[0], width=12, textvariable=id_)
nombreCapturado.grid(row=0, column=1)


#Proveedor
interface_agregar[1].pack(fill=tk.BOTH, expand=True)
interface_agregar[1].configure(bg='red')
interface_agregar[1].pack_forget()

#Producto
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].configure(bg='blue')
interface_agregar[2].pack_forget()


#Venta
interface_agregar[3].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].configure(bg='green')
interface_agregar[3].pack_forget()

#Agregar
titulo=ttk.Label(options, text="titulo", anchor=tk.CENTER, background='yellow', foreground='black')
titulo.grid(row=1, column=0, sticky='NWSE', pady=5)

agregar=ttk.Label(options, text="AGREGAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
agregar.grid(row=2, column=0, sticky='NWSE', pady=5)

empleado=ttk.Label(options, text="EMPLEADO", anchor=tk.CENTER, background='#E0E0E0')
empleado.grid(row=3, column=0, sticky='NWSE', pady=2, padx=10)
empleado.bind("<Button-1>", lambda x: OnDoubleClick(0))
empleado.bind("<Enter>", LabelEnter)
empleado.bind("<Leave>", LabelLeave)


proveedor=ttk.Label(options, text="PROVEEDOR", anchor=tk.CENTER)
proveedor.grid(row=4, column=0, sticky='NWSE', pady=2, padx=10)
proveedor.bind("<Button-1>", lambda x: OnDoubleClick(1))

producto=ttk.Label(options, text="PRODUCTO", anchor=tk.CENTER)
producto.grid(row=5, column=0, sticky='NWSE', pady=2, padx=10)
producto.bind("<Button-1>", lambda x: OnDoubleClick(2))

categoria=ttk.Label(options, text="CATEGORIA", anchor=tk.CENTER)
categoria.grid(row=6, column=0, sticky='NWSE', pady=2, padx=10)
categoria.bind("<Button-1>", lambda x: OnDoubleClick(3))


#Tables

main()
