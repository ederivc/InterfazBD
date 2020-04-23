import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox


def main():
    window.mainloop()


def OnDoubleClick(event):
    if(event==0):
        ShowAgregar(0)
        display.config(bg="#04517D")
    if(event==1):
        ShowAgregar(1)
        display.config(bg='#2ECC71')
    if(event==2):
        ShowAgregar(2)
        display.config(bg='#0781F4')
    if(event==3):
        ShowAgregar(3)
        display.config(bg='#FF8F00')
    if(event==4):
        ShowAgregar(4)
        display.config(bg='#F50052')
    return

def LabelEnter(event):
    event.widget.config(background='#FFFFFF')

def LabelLeave(event):
    event.widget.config(background='#E0E0E0')
 
def ShowAgregar(index):
    x=0
    while(x<len(interface_agregar)):
        if x!=index:
            interface_agregar[x].pack_forget()
        x+=1
    interface_agregar[index].pack(fill=tk.BOTH, expand=True,  padx=5, pady=5)



window = tk.Tk()
window.title('Base de datos')
window.minsize(1080, 600)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=4)
window.config(bg='#282828')



options= tk.Frame(window, bg="#080808")
options.grid(row=0,column=0, sticky='NSWE')
options.columnconfigure(0, weight=1)

display=tk.Frame(window, bg="#04517D")
display.grid(row=0,column=1, sticky='NSWE', padx=7, pady=7)


interface_agregar= []

for x in range(5):
    interface_agregar.append(tk.Frame(display))


#Inicio
interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[0].configure(bg='#04517D')
interface_agregar[0].pack_forget()

#Empleado
interface_agregar[1].pack(fill=tk.BOTH, expand=True)
interface_agregar[1].configure(bg='white')
interface_agregar[1].pack_forget()

ttk.Label(interface_agregar[1], text="ID:").grid(row=0, column=0, padx=50)
ttk.Label(interface_agregar[1], text="Nombre:").grid(row=2, column=0, padx=50)



#Proveedor
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].configure(bg='white')
interface_agregar[2].pack_forget()

#Producto
interface_agregar[3].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].configure(bg='white')
interface_agregar[3].pack_forget()


#Venta
interface_agregar[4].pack(fill=tk.BOTH, expand=True)
interface_agregar[4].configure(bg='white')
interface_agregar[4].pack_forget()





#Option -> Agregar
titulo = tk.Frame(options)
titulo.grid(row=0, column=0,sticky='NWSE', pady=5)
logo_texto=ttk.Label(titulo, text='BASE DE DATOS', background='white', anchor=tk.CENTER)
logo_texto.pack(side=tk.RIGHT, fill=tk.BOTH,expand=1)
logo_texto.bind("<Button-1>", lambda x: OnDoubleClick(0))

agregar=ttk.Label(options, text="AGREGAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
agregar.grid(row=1, column=0, sticky='NWSE', pady=5)

empleado=ttk.Label(options, text="EMPLEADO", anchor=tk.CENTER, background='#E0E0E0')
empleado.grid(row=2, column=0, sticky='NWSE', pady=2, padx=10)
empleado.bind("<Button-1>", lambda x: OnDoubleClick(1))
empleado.bind("<Enter>", LabelEnter)
empleado.bind("<Leave>", LabelLeave)


proveedor=ttk.Label(options, text="PROVEEDOR", anchor=tk.CENTER, background='#E0E0E0')
proveedor.grid(row=3, column=0, sticky='NWSE', pady=2, padx=10)
proveedor.bind("<Button-1>", lambda x: OnDoubleClick(2))
proveedor.bind("<Enter>", LabelEnter)
proveedor.bind("<Leave>", LabelLeave)

producto=ttk.Label(options, text="PRODUCTO", anchor=tk.CENTER, background='#E0E0E0')
producto.grid(row=4, column=0, sticky='NWSE', pady=2, padx=10)
producto.bind("<Button-1>", lambda x: OnDoubleClick(3))
producto.bind("<Enter>", LabelEnter)
producto.bind("<Leave>", LabelLeave)

categoria=ttk.Label(options, text="CATEGORIA", anchor=tk.CENTER, background='#E0E0E0') 
categoria.grid(row=5, column=0, sticky='NWSE', pady=2, padx=10)
categoria.bind("<Button-1>", lambda x: OnDoubleClick(4))
categoria.bind("<Enter>", LabelEnter)
categoria.bind("<Leave>", LabelLeave)


#Tables

main()
