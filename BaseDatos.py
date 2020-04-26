import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *
import mysql.connector as mysql

def main():
    hola()
    tableEmp()
    window.mainloop()

def OnClick(event):
    if(event==0):
        ShowAgregar(0)
        display.config(bg="#04517D")
        labelDisplay.pack_forget()
    if(event==1):
        labelDisplay.pack(side='top')
        ShowAgregar(1)
        display.config(bg='#2ECC71')
    if(event==2):
        labelDisplay.pack(side='top')
        ShowAgregar(2)
        display.config(bg='#0781F4')
    if(event==3):
        labelDisplay.pack(side='top')
        ShowAgregar(3)
        display.config(bg='#FF8F00')
    if(event==4):
        labelDisplay.pack(side='top')
        ShowAgregar(4)
        display.config(bg='#F50052')
    if(event==5):
        labelDisplay.pack(side='top')
        ShowAgregar(5)
        display.config(bg='#ffa751')
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
            agregar_frames[x].config(bg='#080808')
        x+=1
    interface_agregar[index].pack(fill=tk.BOTH, expand=True,  padx=5, pady=5)
    agregar_frames[index].config(bg='#0781F4')
    
def hola():
    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute( "SELECT * FROM employee" )
    for id,nombre,apPat,apMat, rfc, fechaNac, fechaIng, lugarNac,ciudad,estado, pais, calle, colonia, cp, telefono, sueldo in operacion.fetchall():
        print(id,nombre,apPat,apMat, rfc, fechaNac, fechaIng, lugarNac, ciudad,
            estado, pais, calle, colonia, cp, telefono, sueldo)
    conexion.close()

window = tk.Tk()
window.title('Base de datos')
window.minsize(1080, 700)

w = 1080 # width for the Tk root
h = 700 # height for the Tk root

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
labelDisplay.pack_forget()
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

for x in range(6):
    interface_agregar.append(tk.Frame(display))


#*****************************************Inicio*********************************
interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[0].configure(bg='#04517D')
interface_agregar[0].pack_forget()

#---------------------------------------->Empleado<-------------------------------------
interface_agregar[1].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[1].configure(bg='white')
interface_agregar[1].pack_forget()

LabelEmployee = tk.Label(interface_agregar[1], background = 'white', image = employeeImg)
LabelEmployee.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[1], text="   REGISTRO DE EMPLEADO     ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[1], text="ID:", font=("Fixedsys", 16), background='white').grid(row=2, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Nombre:", font=("Fixedsys", 16),  background='white').grid(row=4, column=1, pady=2)
ttk.Label(interface_agregar[1], text="RFC:", font=("Fixedsys", 16),  background='white').grid(row=6, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Fecha Nacimiento:", font=("Fixedsys", 16),  background='white').grid(row=8, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Fecha Ingreso:", font=("Fixedsys", 16),  background='white').grid(row=10, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Lugar Nacimiento:", font=("Fixedsys", 16),  background='white').grid(row=12, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Ciudad:", font=("Fixedsys", 16),  background='white').grid(row=14, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Estado:", font=("Fixedsys", 16),  background='white').grid(row=16, column=1, pady=2)
ttk.Label(interface_agregar[1], text="País:", font=("Fixedsys", 16),  background='white').grid(row=18, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Dirección:", font=("Fixedsys", 16),  background='white').grid(row=20, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Calle:", font=("Fixedsys", 16),  background='white').grid(row=22, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Colonia:", font=("Fixedsys", 16),  background='white').grid(row=24, column=1, pady=2)
ttk.Label(interface_agregar[1], text="CP:", font=("Fixedsys", 16),  background='white').grid(row=26, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Teléfono:", font=("Fixedsys", 16),  background='white').grid(row=28, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Sueldo:", font=("Fixedsys", 16),  background='white').grid(row=30, column=1, pady=2)


aidi = ttk.Entry(interface_agregar[1], width=15)
aidi.grid(row=2, column=2, pady=2)

nombreEmp = ttk.Entry(interface_agregar[1], width = 15)
nombreEmp.grid(row = 4, column = 2, pady=2)

rfcEmp = ttk.Entry(interface_agregar[1], width = 15)
rfcEmp.grid(row = 6, column = 2, pady=2)

fechaNacEmp = ttk.Entry(interface_agregar[1], width = 15)
fechaNacEmp.grid(row = 8, column = 2, pady=2) 

fechaIngresoEmp = ttk.Entry(interface_agregar[1], width = 15)
fechaIngresoEmp.grid(row = 10, column = 2, pady=2)

lugNacEmp = ttk.Entry(interface_agregar[1], width = 15)
lugNacEmp.grid(row = 12, column = 2, pady=2)

ciudadEmp = ttk.Entry(interface_agregar[1], width = 15)
ciudadEmp.grid(row = 14, column = 2, pady=2)

estadoEmp = ttk.Entry(interface_agregar[1], width = 15)
estadoEmp.grid(row = 16, column = 2, pady=2)

paisEmp = ttk.Entry(interface_agregar[1], width = 15)
paisEmp.grid(row = 18, column = 2, pady=2)

direccEmp = ttk.Entry(interface_agregar[1], width = 15)
direccEmp.grid(row = 20, column = 2, pady=2)

calleEmp = ttk.Entry(interface_agregar[1], width = 15)
calleEmp.grid(row = 22, column = 2, pady=2)

coloniaEmp = ttk.Entry(interface_agregar[1], width = 15)
coloniaEmp.grid(row = 24, column = 2, pady=2)

cpEmp = ttk.Entry(interface_agregar[1], width = 15)
cpEmp.grid(row = 26, column = 2, pady=2)

telEmp = ttk.Entry(interface_agregar[1], width = 15)
telEmp.grid(row = 28, column = 2, pady=2)

sueldoEmp = ttk.Entry(interface_agregar[1], width = 15)
sueldoEmp.grid(row = 30, column = 2, pady=2)

submitEmp=tk.Button(interface_agregar[1], text="Ingresar", background='#2ECC71', fg='white',relief=tk.FLAT)
submitEmp.grid(row=32, column=2, pady=2)
#*****************************************************************************

#************************************************Proveedor******************************************
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].configure(bg='white')
interface_agregar[2].pack_forget()

labelSupplier = tk.Label(interface_agregar[2], background = 'white', image = supplierImg)
labelSupplier.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[2], text="      REGISTRO DE PROVEEDOR     ", 
font=("Times", 20), background='white').grid(row=2, column=2)
ttk.Label(interface_agregar[2], text="Clave:",font=("Fixedsys", 16), background='white').grid(row=4, column=1, pady=5)
ttk.Label(interface_agregar[2], text="Nombre:",font=("Fixedsys", 16), background='white').grid(row=6, column=1,pady=5)
ttk.Label(interface_agregar[2], text="RFC:",font=("Fixedsys", 16), background='white').grid(row=8, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Nombre Empresa:",font=("Fixedsys", 16), background='white').grid(row=10, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Ciudad:",font=("Fixedsys", 16), background='white').grid(row=12, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Calle:",font=("Fixedsys", 16), background='white').grid(row=14, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Colonia:",font=("Fixedsys", 16), background='white').grid(row=16, column=1,pady=5)
ttk.Label(interface_agregar[2], text="CP:",font=("Fixedsys", 16), background='white').grid(row=18, column=1,pady=5)

claveProv = ttk.Entry(interface_agregar[2], width = 15)
claveProv.grid(row = 4, column = 2,pady=5)

nombreProv = ttk.Entry(interface_agregar[2], width = 15)
nombreProv.grid(row = 6, column = 2,pady=5)

rfcProv = ttk.Entry(interface_agregar[2], width = 15)
rfcProv.grid(row = 8, column = 2,pady=5)

empresaProv = ttk.Entry(interface_agregar[2], width = 15)
empresaProv.grid(row = 10, column = 2,pady=5)

ciudadProv = ttk.Entry(interface_agregar[2], width = 15)
ciudadProv.grid(row = 12, column = 2,pady=5)

calleProv = ttk.Entry(interface_agregar[2], width = 15)
calleProv.grid(row = 14, column = 2,pady=5)

coloniaProv = ttk.Entry(interface_agregar[2], width = 15)
coloniaProv.grid(row = 16, column = 2,pady=5)

cpProv = ttk.Entry(interface_agregar[2], width = 15)
cpProv.grid(row = 18, column = 2,pady=5)

submitProv=tk.Button(interface_agregar[2], text="Ingresar", background='#0781F4', fg='white',relief=tk.FLAT)
submitProv.grid(row=22, column=2,pady=5)
#************************************************************************


#**************************************************Producto*****************************************
interface_agregar[3].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].configure(bg='white')
interface_agregar[3].pack_forget()

labelBox = tk.Label(interface_agregar[3], background = 'white', image = boxImg)
labelBox.grid(row = 4, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[3], text="   REGISTRO DE PRODUCTOS     ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[3], text="Código de barras:",font=("Fixedsys", 16), background='white').grid(row=2, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Nombre:",font=("Fixedsys", 16), background='white').grid(row=4, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Marca:",font=("Fixedsys", 16), background='white').grid(row=6, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Existencia:",font=("Fixedsys", 16), background='white').grid(row=8, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Costo:",font=("Fixedsys", 16), background='white').grid(row=10, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Proveedor:",font=("Fixedsys", 16), background='white').grid(row=12, column=1, pady=5)

codigoProd = ttk.Entry(interface_agregar[3], width = 15)
codigoProd.grid(row = 2, column = 2, pady=5)

nombreProd = ttk.Entry(interface_agregar[3], width = 15)
nombreProd.grid(row = 4, column = 2, pady=5)

marcaProd = ttk.Entry(interface_agregar[3], width = 15)
marcaProd.grid(row = 6, column = 2, pady=5)

existProd = ttk.Entry(interface_agregar[3], width = 15)
existProd.grid(row = 8, column = 2, pady=5)

costoProd = ttk.Entry(interface_agregar[3], width = 15)
costoProd.grid(row = 10, column = 2, pady=5)

provedorProd = ttk.Entry(interface_agregar[3], width = 15)
provedorProd.grid(row = 12, column = 2, pady=5)

submitProd=tk.Button(interface_agregar[3], text="Ingresar", background='#FF8F00', fg='white',relief=tk.FLAT)
submitProd.grid(row=14, column=2, pady=5)
#**************************************************************************

#**************************************** INGRESAR ****************************************
interface_agregar[4].pack(fill=tk.BOTH, expand=True)
interface_agregar[4].configure(bg='white')
interface_agregar[4].pack_forget()

ttk.Label(interface_agregar[4], text="que va aqui xd?",font=("Fixedsys", 16), background='white').grid(row=0, column=0)

submitVenta=tk.Button(interface_agregar[4], text="Ingresar", background='#F50052', fg='white',relief=tk.FLAT)
submitVenta.grid(row=1, column=1)

#Option -> Agregar
agregar_frames= []

for x in range(6):
    agregar_frames.append(tk.Frame(options))


title = tk.Frame(options, bg = '#005ea5')
title.grid(row=0, column=0, sticky='NWSE', pady=5)
labelTitle = ttk.Label(title, text = '     TIENDA DE \n    CONVENIENCIA', width = 18, background = '#446b75')
labelTitle.pack(side = tk.TOP, anchor = 'center')
labelTitle.config(font=("Courier", 15))
labelTitle.bind("<Button-1>", lambda x: OnClick(0))

agregar_frames[0]=tk.Frame(options)
agregar_frames[0].grid(row=1,column=0,sticky='NWSE', pady=2)
agregar=ttk.Label(agregar_frames[0], text="AGREGAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
agregar.pack(side='right', fill='both', expand=1)

agregar_frames[1]=tk.Frame(options, bg = '#080808')
agregar_frames[1].grid(row=2,column=0,sticky='NWSE', pady=2, padx=10)
empleado=ttk.Label(agregar_frames[1], text="EMPLEADO", anchor=tk.CENTER, background='#E0E0E0')
empleado.pack(side='right', fill='both', expand=1, padx=5, pady=1)
empleado.bind("<Button-1>", lambda x: OnClick(1))
empleado.bind("<Enter>", LabelEnter)
empleado.bind("<Leave>", LabelLeave)


agregar_frames[2]=tk.Frame(options, bg = '#080808')
agregar_frames[2].grid(row=3,column=0,sticky='NWSE', pady=2, padx=10)
proveedor=ttk.Label(agregar_frames[2], text="PROVEEDOR", anchor=tk.CENTER, background='#E0E0E0')
proveedor.pack(side='right', fill='both', expand=1, padx=5, pady=1)
proveedor.bind("<Button-1>", lambda x: OnClick(2))
proveedor.bind("<Enter>", LabelEnter)
proveedor.bind("<Leave>", LabelLeave)

agregar_frames[3]=tk.Frame(options, bg = '#080808')
agregar_frames[3].grid(row=4,column=0,sticky='NWSE', pady=2, padx=10)
producto=ttk.Label(agregar_frames[3], text="PRODUCTO", anchor=tk.CENTER, background='#E0E0E0')
producto.pack(side='right', fill='both', expand=1, padx=5, pady=1)
producto.bind("<Button-1>", lambda x: OnClick(3))
producto.bind("<Enter>", LabelEnter)
producto.bind("<Leave>", LabelLeave)

agregar_frames[4]=tk.Frame(options, bg = '#080808')
agregar_frames[4].grid(row=5,column=0,sticky='NWSE', pady=2, padx=10)
categoria=ttk.Label(agregar_frames[4], text="CATEGORIA", anchor=tk.CENTER, background='#E0E0E0')
categoria.pack(side='right', fill='both', expand=1, padx=5, pady=1)
categoria.bind("<Button-1>", lambda x: OnClick(4))
categoria.bind("<Enter>", LabelEnter)
categoria.bind("<Leave>", LabelLeave)


#**************************************** MOSTRAR ************************************

show = ttk.Label(options, text="MOSTRAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
show.grid(row=6, column=0, sticky='NWSE', pady=5)

interface_agregar[5].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[5].configure(bg='white')
interface_agregar[5].rowconfigure(0, weight=1)
interface_agregar[5].rowconfigure(2, weight=1)
interface_agregar[5].pack_forget()

ttk.Label(interface_agregar[5], text="        LISTA DE EMPLEADOS     ", 
font=("Times", 20), background='white').grid(row=0, column=0, sticky='NEWS')

agregar_frames[5]=tk.Frame(options, bg = '#ffa751')
agregar_frames[5].grid(row=7,column=0,sticky='NWSE', pady=2, padx=10)
employeeShow=ttk.Label(agregar_frames[5], text="EMPLEADO", anchor=tk.CENTER, background='#E0E0E0')
employeeShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
employeeShow.bind("<Button-1>", lambda x: OnClick(5))
employeeShow.bind("<Enter>", LabelEnter)
employeeShow.bind("<Leave>", LabelLeave)

employeeTable = ttk.Treeview(interface_agregar[5])
employeeTable.grid(row=2, column=0,sticky='NEWS')
employeeTable['columns'] = (
                             'nombre','apellidoP','apellidoM','rfc','fechaNac',
                             'fechaIng','lugarNac','ciudad','estado','pais','calle',
                             'colonia','cp','telefono','sueldo'
                            )

def tableEmp():
    employeeTable.heading("#0", text='ay di', anchor='center')
    employeeTable.column("#0", anchor="w",width=80)
    employeeTable.heading('nombre', text='Nombre')
    employeeTable.column('nombre', anchor='center', width=80)
    employeeTable.heading('apellidoP', text='Apellido P')
    employeeTable.column('apellidoP', anchor='center', width=80)
    employeeTable.heading('apellidoM', text='Apelldio M')
    employeeTable.column('apellidoM', anchor='center', width=80)
    employeeTable.heading('rfc', text='RFC')
    employeeTable.column('rfc', anchor='center', width=80)
    employeeTable.heading('fechaNac', text='FechaNac')
    employeeTable.column('fechaNac', anchor='center', width=80)
    employeeTable.heading('fechaIng', text='FechaIng')
    employeeTable.column('fechaIng', anchor='center', width=80)
    employeeTable.heading('lugarNac', text='LugarNac')
    employeeTable.column('lugarNac', anchor='center', width=80)
    employeeTable.heading('ciudad', text='Ciudad')
    employeeTable.column('ciudad', anchor='center', width=80)
    employeeTable.heading('estado', text='Estado')
    employeeTable.column('estado', anchor='center', width=80)
    employeeTable.heading('pais', text='Pais')
    employeeTable.column('pais', anchor='center', width=80)
    employeeTable.heading('calle', text='Calle')
    employeeTable.column('calle', anchor='center', width=80)
    employeeTable.heading('colonia', text='Colonia')
    employeeTable.column('colonia', anchor='center', width=80)
    employeeTable.heading('cp', text='CP')
    employeeTable.column('cp', anchor='center', width=80)
    employeeTable.heading('telefono', text='Tel')
    employeeTable.column('telefono', anchor='center', width=80)
    employeeTable.heading('sueldo', text='Sueldo')
    employeeTable.column('sueldo', anchor='center', width=80)


main()