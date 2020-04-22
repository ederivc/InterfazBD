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
ttk.Label(interface_agregar[0], text="Teléfono:").grid(row=26, column=0)
ttk.Label(interface_agregar[0], text="Sueldo:").grid(row=38, column=0)

id_ = tk.StringVar()
aidi = ttk.Entry(interface_agregar[0], width=15, textvariable=id_)
aidi.grid(row=0, column=1)

nombreEmp = ttk.Entry(interface_agregar[0], width = 15)
nombreEmp.grid(row = 2, column = 1)

rfcEmp = ttk.Entry(interface_agregar[0], width = 15)
rfcEmp.grid(row = 4, column = 1)

fechaNacEmp = ttk.Entry(interface_agregar[0], width = 15)
fechaNacEmp.grid(row = 6, column = 1) 

fechaIngresoEmp = ttk.Entry(interface_agregar[0], width = 15)
fechaIngresoEmp.grid(row = 8, column = 1)

lugNacEmp = ttk.Entry(interface_agregar[0], width = 15)
lugNacEmp.grid(row = 10, column = 1)

ciudadEmp = ttk.Entry(interface_agregar[0], width = 15)
ciudadEmp.grid(row = 12, column = 1)

estadoEmp = ttk.Entry(interface_agregar[0], width = 15)
estadoEmp.grid(row = 14, column = 1)

paisEmp = ttk.Entry(interface_agregar[0], width = 15)
paisEmp.grid(row = 16, column = 1)

direccEmp = ttk.Entry(interface_agregar[0], width = 15)
direccEmp.grid(row = 18, column = 1)

calleEmp = ttk.Entry(interface_agregar[0], width = 15)
calleEmp.grid(row = 20, column = 1)

coloniaEmp = ttk.Entry(interface_agregar[0], width = 15)
coloniaEmp.grid(row = 22, column = 1)

cpEmp = ttk.Entry(interface_agregar[0], width = 15)
cpEmp.grid(row = 24, column = 1)

telEmp = ttk.Entry(interface_agregar[0], width = 15)
telEmp.grid(row = 26, column = 1)

sueldoEmp = ttk.Entry(interface_agregar[0], width = 15)
sueldoEmp.grid(row = 28, column = 1)
#*****************************************************************************

#Proveedor
interface_agregar[1].pack(fill=tk.BOTH, expand=True)
interface_agregar[1].configure(bg='red')
interface_agregar[1].pack_forget()

ttk.Label(interface_agregar[1], text="Clave:").grid(row=0, column=0)
ttk.Label(interface_agregar[1], text="Nombre:").grid(row=2, column=0)
ttk.Label(interface_agregar[1], text="RFC:").grid(row=4, column=0)
ttk.Label(interface_agregar[1], text="Nombre Empresa:").grid(row=6, column=0)
ttk.Label(interface_agregar[1], text="Ciudad:").grid(row=8, column=0)
ttk.Label(interface_agregar[1], text="Calle:").grid(row=10, column=0)
ttk.Label(interface_agregar[1], text="Colonia:").grid(row=12, column=0)
ttk.Label(interface_agregar[1], text="CP:").grid(row=14, column=0)

claveProv = ttk.Entry(interface_agregar[1], width = 15)
claveProv.grid(row = 0, column = 1)

nombreProv = ttk.Entry(interface_agregar[1], width = 15)
nombreProv.grid(row = 2, column = 1)

rfcProv = ttk.Entry(interface_agregar[1], width = 15)
rfcProv.grid(row = 4, column = 1)

empresaProv = ttk.Entry(interface_agregar[1], width = 15)
empresaProv.grid(row = 6, column = 1)

ciudadProv = ttk.Entry(interface_agregar[1], width = 15)
ciudadProv.grid(row = 8, column = 1)

calleProv = ttk.Entry(interface_agregar[1], width = 15)
calleProv.grid(row = 10, column = 1)

coloniaProv = ttk.Entry(interface_agregar[1], width = 15)
coloniaProv.grid(row = 12, column = 1)

cpProv = ttk.Entry(interface_agregar[1], width = 15)
cpProv.grid(row = 14, column = 1)
#************************************************************************

#Producto
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].configure(bg='blue')
interface_agregar[2].pack_forget()

ttk.Label(interface_agregar[2], text="Codigo de barras:").grid(row=0, column=0)
ttk.Label(interface_agregar[2], text="Nombre:").grid(row=2, column=0)
ttk.Label(interface_agregar[2], text="Marca:").grid(row=4, column=0)
ttk.Label(interface_agregar[2], text="Existencia:").grid(row=6, column=0)
ttk.Label(interface_agregar[2], text="Costo:").grid(row=8, column=0)
ttk.Label(interface_agregar[2], text="Proveedor:").grid(row=10, column=0)

codigoProd = ttk.Entry(interface_agregar[2], width = 15)
codigoProd.grid(row = 0, column = 1)

nombreProd = ttk.Entry(interface_agregar[2], width = 15)
nombreProd.grid(row = 2, column = 1)

marcaProd = ttk.Entry(interface_agregar[2], width = 15)
marcaProd.grid(row = 4, column = 1)

existProd = ttk.Entry(interface_agregar[2], width = 15)
existProd.grid(row = 6, column = 1)

costoProd = ttk.Entry(interface_agregar[2], width = 15)
costoProd.grid(row = 8, column = 1)

provedorProd = ttk.Entry(interface_agregar[2], width = 15)
provedorProd.grid(row = 10, column = 1)
#**************************************************************************

#Venta
interface_agregar[3].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].configure(bg='green')
interface_agregar[3].pack_forget()

#Agregar
title = tk.Frame(options)
title.grid(row=0, column=0, sticky='NWSE', pady=5)
title.config(bg = 'yellow', height = 400)

labelTitle = ttk.Label(title, text = '     TIENDA DE \n    CONVENIENCIA', width = 18)
labelTitle.pack(side = TOP, anchor = 'center')
labelTitle.config(font=("Courier", 15))

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
mostrar = ttk.Label(options, text="MOSTRAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
mostrar.grid(row=20, column=0, sticky='NWSE', pady=5)
main()
