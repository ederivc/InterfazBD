import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *

def main():
    window.mainloop()


def OnClick(event):
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
    event.widget.config(background='#7f7f7f')

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

w = 1080 # width for the Tk root
h = 600 # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=4)
window.config(bg='#282828')

options= tk.Frame(window, bg="#080808")
options.grid(row=0,column=0, sticky='NSWE')
options.columnconfigure(0, weight=1)

display=tk.Frame(window, bg="#04517D")
display.grid(row=0,column=1, sticky='NSWE', padx=7, pady=7)

marketImg = PhotoImage(file = "market.png")
marketImg = marketImg.zoom(2)
marketImg = marketImg.subsample(6)

labelDisplay = tk.Label(display, bg = '#eee6b8', image = marketImg)
labelDisplay.pack()
#********************************** IMAGES ********************************************
employeeImg = PhotoImage(file = "employee.png")
employeeImg = employeeImg.zoom(2)
employeeImg = employeeImg.subsample(6)

supplierImg = PhotoImage(file = "supplier.png")
supplierImg = supplierImg.zoom(2)
supplierImg = supplierImg.subsample(6)

boxImg = PhotoImage(file = "box.png")
boxImg = boxImg.zoom(2)
boxImg = boxImg.subsample(6)

#*************************************** LABELS ****************************************
interface_agregar= []

for x in range(5):
    interface_agregar.append(tk.Frame(display))


#*****************************************Inicio*********************************
interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[0].configure(bg='#04517D')
interface_agregar[0].pack_forget()

#---------------------------------------->Empleado<-------------------------------------
interface_agregar[1].pack(fill=tk.BOTH, expand=True)
interface_agregar[1].configure(bg='white')
interface_agregar[1].pack_forget()

LabelEmployee = tk.Label(interface_agregar[1], background = 'white', image = employeeImg)
LabelEmployee.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[1], text="   REGISTRO DE EMPLEADO     ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[1], text="ID:", font=("Fixedsys", 16), background='white').grid(row=2, column=1)
ttk.Label(interface_agregar[1], text="Nombre:", font=("Fixedsys", 16),  background='white').grid(row=4, column=1)
ttk.Label(interface_agregar[1], text="RFC:", font=("Fixedsys", 16),  background='white').grid(row=6, column=1)
ttk.Label(interface_agregar[1], text="Fecha Nacimiento:", font=("Fixedsys", 16),  background='white').grid(row=8, column=1)
ttk.Label(interface_agregar[1], text="Fecha Ingreso:", font=("Fixedsys", 16),  background='white').grid(row=10, column=1)
ttk.Label(interface_agregar[1], text="Lugar Nacimiento:", font=("Fixedsys", 16),  background='white').grid(row=12, column=1)
ttk.Label(interface_agregar[1], text="Ciudad:", font=("Fixedsys", 16),  background='white').grid(row=14, column=1)
ttk.Label(interface_agregar[1], text="Estado:", font=("Fixedsys", 16),  background='white').grid(row=16, column=1)
ttk.Label(interface_agregar[1], text="País:", font=("Fixedsys", 16),  background='white').grid(row=18, column=1)
ttk.Label(interface_agregar[1], text="Dirección:", font=("Fixedsys", 16),  background='white').grid(row=20, column=1)
ttk.Label(interface_agregar[1], text="Calle:", font=("Fixedsys", 16),  background='white').grid(row=22, column=1)
ttk.Label(interface_agregar[1], text="Colonia:", font=("Fixedsys", 16),  background='white').grid(row=24, column=1)
ttk.Label(interface_agregar[1], text="CP:", font=("Fixedsys", 16),  background='white').grid(row=26, column=1)
ttk.Label(interface_agregar[1], text="Teléfono:", font=("Fixedsys", 16),  background='white').grid(row=28, column=1)
ttk.Label(interface_agregar[1], text="Sueldo:", font=("Fixedsys", 16),  background='white').grid(row=30, column=1)


aidi = ttk.Entry(interface_agregar[1], width=15)
aidi.grid(row=2, column=2)

nombreEmp = ttk.Entry(interface_agregar[1], width = 15)
nombreEmp.grid(row = 4, column = 2)

rfcEmp = ttk.Entry(interface_agregar[1], width = 15)
rfcEmp.grid(row = 6, column = 2)

fechaNacEmp = ttk.Entry(interface_agregar[1], width = 15)
fechaNacEmp.grid(row = 8, column = 2) 

fechaIngresoEmp = ttk.Entry(interface_agregar[1], width = 15)
fechaIngresoEmp.grid(row = 10, column = 2)

lugNacEmp = ttk.Entry(interface_agregar[1], width = 15)
lugNacEmp.grid(row = 12, column = 2)

ciudadEmp = ttk.Entry(interface_agregar[1], width = 15)
ciudadEmp.grid(row = 14, column = 2)

estadoEmp = ttk.Entry(interface_agregar[1], width = 15)
estadoEmp.grid(row = 16, column = 2)

paisEmp = ttk.Entry(interface_agregar[1], width = 15)
paisEmp.grid(row = 18, column = 2)

direccEmp = ttk.Entry(interface_agregar[1], width = 15)
direccEmp.grid(row = 20, column = 2)

calleEmp = ttk.Entry(interface_agregar[1], width = 15)
calleEmp.grid(row = 22, column = 2)

coloniaEmp = ttk.Entry(interface_agregar[1], width = 15)
coloniaEmp.grid(row = 24, column = 2)

cpEmp = ttk.Entry(interface_agregar[1], width = 15)
cpEmp.grid(row = 26, column = 2)

telEmp = ttk.Entry(interface_agregar[1], width = 15)
telEmp.grid(row = 28, column = 2)

sueldoEmp = ttk.Entry(interface_agregar[1], width = 15)
sueldoEmp.grid(row = 30, column = 2)

submitEmp=tk.Button(interface_agregar[1], text="Ingresar", background='#2ECC71', fg='white',relief=tk.FLAT)
submitEmp.grid(row=32, column=2)
#*****************************************************************************

#************************************************Proveedor******************************************
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].configure(bg='white')
interface_agregar[2].pack_forget()

labelSupplier = tk.Label(interface_agregar[2], background = 'white', image = supplierImg)
labelSupplier.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[2], text="      REGISTRO DE PROVEEDOR     ", 
font=("Times", 20), background='white').grid(row=2, column=2)
ttk.Label(interface_agregar[2], text="Clave:",font=("Fixedsys", 16), background='white').grid(row=4, column=1)
ttk.Label(interface_agregar[2], text="Nombre:",font=("Fixedsys", 16), background='white').grid(row=6, column=1)
ttk.Label(interface_agregar[2], text="RFC:",font=("Fixedsys", 16), background='white').grid(row=8, column=1)
ttk.Label(interface_agregar[2], text="Nombre Empresa:",font=("Fixedsys", 16), background='white').grid(row=10, column=1)
ttk.Label(interface_agregar[2], text="Ciudad:",font=("Fixedsys", 16), background='white').grid(row=12, column=1)
ttk.Label(interface_agregar[2], text="Calle:",font=("Fixedsys", 16), background='white').grid(row=14, column=1)
ttk.Label(interface_agregar[2], text="Colonia:",font=("Fixedsys", 16), background='white').grid(row=16, column=1)
ttk.Label(interface_agregar[2], text="CP:",font=("Fixedsys", 16), background='white').grid(row=18, column=1)

claveProv = ttk.Entry(interface_agregar[2], width = 15)
claveProv.grid(row = 4, column = 2)

nombreProv = ttk.Entry(interface_agregar[2], width = 15)
nombreProv.grid(row = 6, column = 2)

rfcProv = ttk.Entry(interface_agregar[2], width = 15)
rfcProv.grid(row = 8, column = 2)

empresaProv = ttk.Entry(interface_agregar[2], width = 15)
empresaProv.grid(row = 10, column = 2)

ciudadProv = ttk.Entry(interface_agregar[2], width = 15)
ciudadProv.grid(row = 12, column = 2)

calleProv = ttk.Entry(interface_agregar[2], width = 15)
calleProv.grid(row = 14, column = 2)

coloniaProv = ttk.Entry(interface_agregar[2], width = 15)
coloniaProv.grid(row = 16, column = 2)

cpProv = ttk.Entry(interface_agregar[2], width = 15)
cpProv.grid(row = 18, column = 2)

submitProv=tk.Button(interface_agregar[2], text="Ingresar", background='#0781F4', fg='white',relief=tk.FLAT)
submitProv.grid(row=22, column=2)
#************************************************************************


#**************************************************Producto*****************************************
interface_agregar[3].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].configure(bg='white')
interface_agregar[3].pack_forget()

labelBox = tk.Label(interface_agregar[3], background = 'white', image = boxImg)
labelBox.grid(row = 4, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[3], text="   REGISTRO DE PRODUCTOS     ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[3], text="Código de barras:",font=("Fixedsys", 16), background='white').grid(row=2, column=1)
ttk.Label(interface_agregar[3], text="Nombre:",font=("Fixedsys", 16), background='white').grid(row=4, column=1)
ttk.Label(interface_agregar[3], text="Marca:",font=("Fixedsys", 16), background='white').grid(row=6, column=1)
ttk.Label(interface_agregar[3], text="Existencia:",font=("Fixedsys", 16), background='white').grid(row=8, column=1)
ttk.Label(interface_agregar[3], text="Costo:",font=("Fixedsys", 16), background='white').grid(row=10, column=1)
ttk.Label(interface_agregar[3], text="Proveedor:",font=("Fixedsys", 16), background='white').grid(row=12, column=1)

codigoProd = ttk.Entry(interface_agregar[3], width = 15)
codigoProd.grid(row = 2, column = 2)

nombreProd = ttk.Entry(interface_agregar[3], width = 15)
nombreProd.grid(row = 4, column = 2)

marcaProd = ttk.Entry(interface_agregar[3], width = 15)
marcaProd.grid(row = 6, column = 2)

existProd = ttk.Entry(interface_agregar[3], width = 15)
existProd.grid(row = 8, column = 2)

costoProd = ttk.Entry(interface_agregar[3], width = 15)
costoProd.grid(row = 10, column = 2)

provedorProd = ttk.Entry(interface_agregar[3], width = 15)
provedorProd.grid(row = 12, column = 2)

submitProd=tk.Button(interface_agregar[3], text="Ingresar", background='#FF8F00', fg='white',relief=tk.FLAT)
submitProd.grid(row=14, column=2)
#**************************************************************************

#Venta
interface_agregar[4].pack(fill=tk.BOTH, expand=True)
interface_agregar[4].configure(bg='white')
interface_agregar[4].pack_forget()

ttk.Label(interface_agregar[4], text="que va aqui xd?",font=("Fixedsys", 16), background='white').grid(row=0, column=0)

submitVenta=tk.Button(interface_agregar[4], text="Ingresar", background='#F50052', fg='white',relief=tk.FLAT)
submitVenta.grid(row=1, column=1)


#Option -> Agregar
title = tk.Frame(options, bg = '#005ea5')
title.grid(row=0, column=0, sticky='NWSE', pady=5)
labelTitle = ttk.Label(title, text = '     TIENDA DE \n    CONVENIENCIA', width = 18, background = '#446b75')
labelTitle.pack(side = tk.TOP, anchor = 'center')
labelTitle.config(font=("Courier", 15))
labelTitle.bind("<Button-1>", lambda x: OnClick(0))

agregar=ttk.Label(options, text="AGREGAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
agregar.grid(row=1, column=0, sticky='NWSE', pady=5)

empleado=ttk.Label(options, text="EMPLEADO", anchor=tk.CENTER, background='#E0E0E0')
empleado.grid(row=2, column=0, sticky='NWSE', pady=2, padx=10)
empleado.bind("<Button-1>", lambda x: OnClick(1))
empleado.bind("<Enter>", LabelEnter)
empleado.bind("<Leave>", LabelLeave)


proveedor=ttk.Label(options, text="PROVEEDOR", anchor=tk.CENTER, background='#E0E0E0')
proveedor.grid(row=3, column=0, sticky='NWSE', pady=2, padx=10)
proveedor.bind("<Button-1>", lambda x: OnClick(2))
proveedor.bind("<Enter>", LabelEnter)
proveedor.bind("<Leave>", LabelLeave)

producto=ttk.Label(options, text="PRODUCTO", anchor=tk.CENTER, background='#E0E0E0')
producto.grid(row=4, column=0, sticky='NWSE', pady=2, padx=10)
producto.bind("<Button-1>", lambda x: OnClick(3))
producto.bind("<Enter>", LabelEnter)
producto.bind("<Leave>", LabelLeave)

categoria=ttk.Label(options, text="CATEGORIA", anchor=tk.CENTER, background='#E0E0E0') 
categoria.grid(row=5, column=0, sticky='NWSE', pady=2, padx=10)
categoria.bind("<Button-1>", lambda x: OnClick(4))
categoria.bind("<Enter>", LabelEnter)
categoria.bind("<Leave>", LabelLeave)


#Tables

show = ttk.Label(options, text="MOSTRAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
show.grid(row=20, column=0, sticky='NWSE', pady=5)


main()
