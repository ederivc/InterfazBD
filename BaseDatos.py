import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
import mysql.connector as mysql

class MyDateEntry(DateEntry):
    def __init__(self, master, **kw):
        DateEntry.__init__(self, master, **kw)
        # add black border around drop-down calendar
        self._top_cal.configure(bg='black', bd=1)
        # add label displaying today's date below
        tk.Label(self._top_cal, bg='gray90', anchor='w', width=35,
                 text='Today: %s' % date.today().strftime('%x')).pack()

def main():
    showEmployee(employeeTable)
    showSupplier(supplierTable)
    showProduct(productTable)
    showSale(saleTable)
    tableEmp()
    tableSupplier()
    tableProduct()
    tableCatPago()
    tableCatProd()
    tableSale()
    window.mainloop()

def OnClick(event):
    if(event==0):
        ShowAgregar(0)
        display.config(bg="#18191A")
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
        showEmployee(employeeTable)
        labelDisplay.pack(side='top')
        ShowAgregar(4)
        display.config(bg='#F50052')
    if(event==5):
        showSupplier(supplierTable)
        labelDisplay.pack(side='top')
        ShowAgregar(5)
        display.config(bg='#ffa751')
    if(event == 6):
        showProduct(productTable)
        labelDisplay.pack(side='top')
        ShowAgregar(6)
        display.config(bg='#6f3eab')
    if(event == 7):
        showSale(saleTable)
        labelDisplay.pack(side='top')
        ShowAgregar(7)
        display.config(bg='#3EBD5E')  
    if(event == 8):
        labelDisplay.pack(side='top')
        ShowAgregar(8)
        display.config(bg='#3EBD5E')    
    if(event == 9):
        labelDisplay.pack(side='top')
        ShowAgregar(9)
        display.config(bg='#3EBD5E') 
    if(event == 10):
        labelDisplay.pack(side='top')
        ShowAgregar(10)
        display.config(bg='#3EBD5E')          
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
  
def regEmp(aidi, nombreEmp, apPatEmp, apMatEmp, rfcEmp, fechaNacEmp, fechaIngresoEmp,
ciudadEmp, estadoEmp, paisEmp, calleEmp, coloniaEmp, cpEmp, telEmp, sueldoEmp):
    try:
        ide = int(aidi)
        sueldo = float(sueldoEmp)
        connection = mysql.connect(host='localhost',
                    user='root',
                    passwd='',
                    database='registration')         
        mySql_insert_query  =f"""INSERT INTO employee VALUES ({ide}, '{nombreEmp}', '{apPatEmp}',
        '{apMatEmp}', '{rfcEmp}', '{fechaNacEmp}', '{fechaIngresoEmp}', '{ciudadEmp}', 
        '{estadoEmp}', '{paisEmp}', '{calleEmp}', '{coloniaEmp}', '{cpEmp}', '{telEmp}','{sueldo}')"""
        
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        mBox.showinfo("EMPLEADOS", "El usuario: " + str(aidi) + " ha sido"+
        " agregado correctamente")
        cursor.close()

    except Exception as e:
        mBox.showerror("ERROR", "No se pudo registrar al empleado, verifique sus "+
        "datos.")
        print("Failed to insert record into Employee table {}".format(e))   

def hola(aidi):
    aidi.delete(0,END)

def regProv(cveProv, nombreProv, rfcProv, telefonoProv, empresaProv, 
ciudadProv, calleProv, coloniaProv, cpProv):
    try:
        connection = mysql.connect(host='localhost',
                    user='root',
                    passwd='',
                    database='registration')
        mySql_insert_query  =f"""INSERT INTO supplier VALUES ({cveProv}, '{nombreProv}', '{rfcProv}', 
        '{telefonoProv}','{empresaProv}', '{ciudadProv}', '{calleProv}', 
        '{coloniaProv}', '{cpProv}')"""

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        mBox.showinfo("PROVEEDORES", "El proveedor: " + str(cveProv) + " ha sido"+
        " agregado correctamente")
        cursor.close()
        showSupplier(supplierTable)

    except Exception as e:
        mBox.showerror("ERROR", "No se pudo registrar al proveedor, verifique sus "+
        "datos.")
        print("Failed to insert record into Supplier table {}".format(e))


def regProd(codigoProd, nombreProd, marcaProd, existProd, costoProd, 
reordenProd,provedorProd, categProd):
    codP = int(codigoProd)
    exProd = int(existProd)
    cosProd = float(costoProd)
    try:
        connection = mysql.connect(host='localhost',
                    user='root',
                    passwd='',
                    database='registration')
        mySql_insert_query  =f"""INSERT INTO product VALUES ({codP}, '{nombreProd}', '{marcaProd}', 
        '{exProd}', '{cosProd}', '{reordenProd}','{provedorProd}', '{categProd}')"""

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        mBox.showinfo("PRODUCTOS", "El producto: " + str(codP) + " ha sido"+
        " agregado correctamente")
        cursor.close()
    except Exception as e:
        mBox.showerror("ERROR", "No se pudo registrar el producto, verifique sus "+
        "datos.")
        print("Failed to insert record into Product table {}".format(e))

def regVenta(claveVenta, codigoProd, cantidad, precioUnit, importe,
fechaVent, formaPago, idEmp):
    while TRUE:
        try:
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')
            mySql_insert_query  =f"""INSERT INTO sales VALUES ({claveVenta}, '{codigoProd}', '{cantidad}', 
            '{precioUnit}', '{importe}', '{fechaVent}', '{formaPago}', '{idEmp}')"""

            i = verifica(codigoProd, cantidad)
            if(i == FALSE):
                mBox.showerror("ERROR", "Excediste el limite de compra, intenta de nuevo.")
                break

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            mBox.showinfo("VENTAS", "La venta: " + str(claveVenta) + " ha sido"+
            " relizada")
            elimina(codigoProd, cantidad)
            verificaReo(codigoProd)
            cursor.close()
            break
        except Exception as e:
            mBox.showerror("ERROR", "No se pudo realizar la venta, verifique sus "+
            "datos.")
            print("Failed to insert record into Sales table {}".format(e))
            break

def showEmployee(employeeTable):
    for i in employeeTable.get_children():
        employeeTable.delete(i)

    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute( "SELECT * FROM employee" )
    for id, nombreEmp, apPatEmp, apMatEmp, rfcEmp, fechaNacEmp, fechaIngresoEmp, ciudadEmp, estadoEmp, paisEmp, calleEmp, coloniaEmp, cpEmp, telEmp, sueldoEmp in operacion.fetchall():
        employeeTable.insert('', 'end', text = id, values=(nombreEmp, apPatEmp, apMatEmp, 
        rfcEmp, fechaNacEmp, fechaIngresoEmp, ciudadEmp, estadoEmp, 
        paisEmp, calleEmp, coloniaEmp, cpEmp, telEmp, sueldoEmp))
    conexion.close()

def showSupplier(supplierTable):
    for i in supplierTable.get_children():
        supplierTable.delete(i)

    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute( "SELECT * FROM supplier" )
    for claveProv, nombreProv,rfcProv,telefonoProv,empresaProv,ciudadProv,calleProv,coloniaProv,cpProv in operacion.fetchall():
        supplierTable.insert('', 'end', text = claveProv, values=(nombreProv, rfcProv, 
        telefonoProv, empresaProv,ciudadProv, calleProv, coloniaProv, cpProv))
    conexion.close()

def showProduct(productTable):
    for i in productTable.get_children():
        productTable.delete(i)

    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute( "SELECT * FROM product" )
    for codigoProd,nombreProd,marcaProd,existProd,costoProd,reordenProd,provedorProd,categProd in operacion.fetchall():
        productTable.insert('', 'end', text = codigoProd, values=(nombreProd,marcaProd,existProd,
        costoProd,reordenProd,provedorProd,categProd))
    conexion.close()

def showSale(saleTable):
    for i in saleTable.get_children():
        saleTable.delete(i)

    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute( "SELECT * FROM sales" )
    for clave,codigoProd,cantidad,precioUni,importe,fecha,fPago, claveEmp in operacion.fetchall():
        saleTable.insert('', 'end', text = clave, values=(codigoProd,cantidad,precioUni,
        importe,fecha,fPago,claveEmp))
    conexion.close()

def verifica(codigo, cantidad):
    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute("SELECT existencia FROM product WHERE codigoProd = %s",(codigo,)) 
    valor = operacion.fetchone()
    if(int(cantidad) >= int(valor[0])):
        return FALSE
    conexion.close()

def elimina(codigo, cantidad):
    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute("SELECT existencia FROM product WHERE codigoProd = %s",(codigo,))
    real = operacion.fetchone()
    total = int(real[0]) - int(cantidad)
    operacion.execute("UPDATE product SET existencia = %s WHERE codigoProd = %s",(total, codigo))
    conexion.commit()
    conexion.close()

def verificaReo(codigo):
    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
    operacion = conexion.cursor()
    operacion.execute("SELECT existencia FROM product WHERE codigoProd = %s",(codigo,))
    exis = operacion.fetchone() 
    operacion.execute("SELECT reordenProd FROM product WHERE codigoProd = %s",(codigo,))
    reo = operacion.fetchone()
    if(int(exis[0]) <= int(reo[0])):
        nuevo = int(exis[0]) + 50
        operacion.execute("UPDATE product SET existencia = %s WHERE codigoProd = %s",(nuevo, codigo))
    conexion.commit()
    conexion.close()

window = tk.Tk()
window.title('Base de datos')
window.minsize(1140, 700)

w = 1140 # width for the Tk root
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

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=4)
window.config(bg='#282828')

options= tk.Frame(window, bg="#8c95f1")
options.grid(row=0,column=0, sticky='NSWE')
options.columnconfigure(0, weight=1)

display = tk.Frame(window, bg="#18191A")
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

saleImg = PhotoImage(file = "sale.png")
saleImg = saleImg.zoom(2)
saleImg = saleImg.subsample(6)

stockImg = PhotoImage(file = "stock_2.png")
soundImg = PhotoImage(file = "sound-wave.png")


#*************************************** LABELS ****************************************
interface_agregar= []

for x in range(11):
    interface_agregar.append(tk.Frame(display))


#*****************************************Inicio*********************************
interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[0].configure(bg='#18191A')

canvas = Canvas(interface_agregar[0], bg='#9f01fc', width=250, height=h,bd=0, relief='flat',highlightthickness=0)
canvas.create_image(0,0, anchor='nw', image=stockImg)
canvas.pack(side='right', fill=BOTH)

canvas2 = Canvas(interface_agregar[0], bg='#9f01fc', width=w, height=100,bd=0, relief='flat',highlightthickness=0)
canvas2.create_image(0,0, anchor='nw', image=soundImg)
canvas2.pack(side='bottom', fill=BOTH)

home_page=tk.Frame(interface_agregar[0])
home_page.pack(side='left', fill=BOTH)
home_page.configure(bg='#18191A')
home_page.columnconfigure(1,weight=2)
home_page.columnconfigure(0,weight=1)
ttk.Label(home_page, text="BIENVENIDO", font=("Times", 50, 'bold'), background='#18191A', foreground='white',).grid(row=0, column=0,padx=50,pady=20, columnspan=2)
ttk.Label(home_page, text="BASE DE \n\tDATOS", font=("Times", 30, 'bold'), background='#18191A', foreground='#3A3939').grid(row=1, column=1)

agregarHome=ttk.Label(home_page, text="\n\n⮞ Agregar", font=("Arial", 12, 'bold'), background='#18191A', foreground='white')
agregarHome.grid(row=2, column=0,padx=10)
agregarHome.bind("<Button-1>", lambda x: OnClick(1))

mostrarHome=ttk.Label(home_page, text="\n\n⮞ Mostrar", font=("Arial", 12, 'bold'), background='#18191A', foreground='white')
mostrarHome.grid(row=3, column=0,padx=10)
mostrarHome.bind("<Button-1>", lambda x: OnClick(4))

categoriasHome=ttk.Label(home_page, text="\n\n⮞ Categorías", font=("Arial", 12, 'bold'), background='#18191A', foreground='white')
categoriasHome.grid(row=4, column=0,padx=10)
categoriasHome.bind("<Button-1>", lambda x: OnClick(8))

ventasHome=ttk.Label(home_page, text="\n\n⮞ Ventas", font=("Arial", 12, 'bold'), background='#18191A', foreground='white')
ventasHome.grid(row=5, column=0,padx=10)
ventasHome.bind("<Button-1>", lambda x: OnClick(10))

#---------------------------------------->Empleado<-------------------------------------
interface_agregar[1].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[1].configure(bg='white')
interface_agregar[1].pack_forget()

LabelEmployee = tk.Label(interface_agregar[1], background = 'white', image = employeeImg)
LabelEmployee.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[1], text="   REGISTRO DE EMPLEADO     ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[1], text="ID:", font=("Fixedsys", 9), background='white').grid(row=2, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Nombre:", font=("Fixedsys", 9),  background='white').grid(row=4, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Apellido Paterno:", font=("Fixedsys", 9),  background='white').grid(row=6, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Apellido Materno:", font=("Fixedsys", 9),  background='white').grid(row=8, column=1, pady=2)
ttk.Label(interface_agregar[1], text="RFC:", font=("Fixedsys", 9),  background='white').grid(row=10, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Fecha Nacimiento:", font=("Fixedsys", 9),  background='white').grid(row=12, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Fecha Ingreso:", font=("Fixedsys", 9),  background='white').grid(row=14, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Ciudad:", font=("Fixedsys", 9),  background='white').grid(row=16, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Estado:", font=("Fixedsys", 9),  background='white').grid(row=18, column=1, pady=2)
ttk.Label(interface_agregar[1], text="País:", font=("Fixedsys", 9),  background='white').grid(row=20, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Calle:", font=("Fixedsys", 9),  background='white').grid(row=22, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Colonia:", font=("Fixedsys", 9),  background='white').grid(row=24, column=1, pady=2)
ttk.Label(interface_agregar[1], text="CP:", font=("Fixedsys", 9),  background='white').grid(row=26, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Teléfono:", font=("Fixedsys", 9),  background='white').grid(row=28, column=1, pady=2)
ttk.Label(interface_agregar[1], text="Sueldo:", font=("Fixedsys", 9),  background='white').grid(row=30, column=1, pady=2)


aidi = ttk.Entry(interface_agregar[1], width=30)
aidi.grid(row=2, column=2, pady=2)

nombreEmp = ttk.Entry(interface_agregar[1], width = 30)
nombreEmp.grid(row = 4, column = 2, pady=2)

apPatEmp = ttk.Entry(interface_agregar[1], width = 30)
apPatEmp.grid(row = 6, column = 2)

apMatEmp = ttk.Entry(interface_agregar[1], width = 30)
apMatEmp.grid(row = 8, column = 2)

rfcEmp = ttk.Entry(interface_agregar[1], width = 30)
rfcEmp.grid(row = 10, column = 2, pady=2)

fechaNacEmp = MyDateEntry(interface_agregar[1],
                 width=28,
                 justify='center',
                 selectbackground='gray80',
                 selectforeground='black',
                 normalbackground='white',
                 normalforeground='black',
                 background='gray90',
                 foreground='black',
                 bordercolor='gray90',
                 othermonthforeground='gray50',
                 othermonthbackground='white',
                 othermonthweforeground='gray50',
                 othermonthwebackground='white',
                 weekendbackground='white',
                 weekendforeground='black',
                 headersbackground='white',
                 headersforeground='gray70')
                 
fechaNacEmp.grid(row = 12, column = 2, pady=2) 

fechaIngresoEmp = MyDateEntry(interface_agregar[1],
                 width=28,
                 justify='center',
                 selectbackground='gray80',
                 selectforeground='black',
                 normalbackground='white',
                 normalforeground='black',
                 background='gray90',
                 foreground='black',
                 bordercolor='gray90',
                 othermonthforeground='gray50',
                 othermonthbackground='white',
                 othermonthweforeground='gray50',
                 othermonthwebackground='white',
                 weekendbackground='white',
                 weekendforeground='black',
                 headersbackground='white',
                 headersforeground='gray70')

fechaIngresoEmp.grid(row = 14, column = 2, pady=2)

ciudadEmp = ttk.Entry(interface_agregar[1], width = 30)
ciudadEmp.grid(row = 16, column = 2, pady=2)

estadoEmp = ttk.Entry(interface_agregar[1], width = 30)
estadoEmp.grid(row = 18, column = 2, pady=2)

paisEmp = ttk.Entry(interface_agregar[1], width = 30)
paisEmp.grid(row = 20, column = 2, pady=2)

calleEmp = ttk.Entry(interface_agregar[1], width = 30)
calleEmp.grid(row = 22, column = 2, pady=2)

coloniaEmp = ttk.Entry(interface_agregar[1], width = 30)
coloniaEmp.grid(row = 24, column = 2, pady=2)

cpEmp = ttk.Entry(interface_agregar[1], width = 30)
cpEmp.grid(row = 26, column = 2, pady=2)

telEmp = ttk.Entry(interface_agregar[1], width = 30)
telEmp.grid(row = 28, column = 2, pady=2)

sueldoEmp = ttk.Entry(interface_agregar[1], width = 30)
sueldoEmp.grid(row = 30, column = 2, pady=2)

submitEmp=tk.Button(interface_agregar[1], text="Ingresar", background='#2ECC71', fg='white',
relief=tk.FLAT, command = lambda: regEmp(aidi.get(), nombreEmp.get(), apPatEmp.get(), 
apMatEmp.get(), rfcEmp.get(), fechaNacEmp.get(), fechaIngresoEmp.get(), ciudadEmp.get(),
estadoEmp.get(), paisEmp.get(), calleEmp.get(), coloniaEmp.get(), 
cpEmp.get(), telEmp.get(), sueldoEmp.get()))
submitEmp.grid(row=34, column=2, pady=2)
#*****************************************************************************

#************************************************PROVEEDOR******************************************
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].configure(bg='white')
interface_agregar[2].pack_forget()

labelSupplier = tk.Label(interface_agregar[2], background = 'white', image = supplierImg)
labelSupplier.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[2], text="      REGISTRO DE PROVEEDOR     ", 
font=("Times", 20), background='white').grid(row=2, column=2)
ttk.Label(interface_agregar[2], text="Clave:",font=("Fixedsys", 9), background='white').grid(row=4, column=1, pady=5)
ttk.Label(interface_agregar[2], text="Nombre:",font=("Fixedsys", 9), background='white').grid(row=6, column=1,pady=5)
ttk.Label(interface_agregar[2], text="RFC:",font=("Fixedsys", 9), background='white').grid(row=8, column=1,pady=5)
ttk.Label(interface_agregar[2], text ="Telefono:", font=("Fixedsys", 9), background = 'white').grid(row=10,column = 1,pady=5)
ttk.Label(interface_agregar[2], text="Nombre Empresa:",font=("Fixedsys", 9), background='white').grid(row=12, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Ciudad:",font=("Fixedsys", 9), background='white').grid(row=14, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Calle:",font=("Fixedsys", 9), background='white').grid(row=16, column=1,pady=5)
ttk.Label(interface_agregar[2], text="Colonia:",font=("Fixedsys", 9), background='white').grid(row=18, column=1,pady=5)
ttk.Label(interface_agregar[2], text="CP:",font=("Fixedsys", 9), background='white').grid(row=20, column=1,pady=5)

claveProv = ttk.Entry(interface_agregar[2], width = 15)
claveProv.grid(row = 4, column = 2,pady=5)

nombreProv = ttk.Entry(interface_agregar[2], width = 15)
nombreProv.grid(row = 6, column = 2,pady=5)

rfcProv = ttk.Entry(interface_agregar[2], width = 15)
rfcProv.grid(row = 8, column = 2,pady=5)

telProv = ttk.Entry(interface_agregar[2], width = 15)
telProv.grid(row = 10, column = 2,pady=5)

empresaProv = ttk.Entry(interface_agregar[2], width = 15)
empresaProv.grid(row = 12, column = 2,pady=5)

ciudadProv = ttk.Entry(interface_agregar[2], width = 15)
ciudadProv.grid(row = 14, column = 2,pady=5)

calleProv = ttk.Entry(interface_agregar[2], width = 15)
calleProv.grid(row = 16, column = 2,pady=5)

coloniaProv = ttk.Entry(interface_agregar[2], width = 15)
coloniaProv.grid(row = 18, column = 2,pady=5)

cpProv = ttk.Entry(interface_agregar[2], width = 15)
cpProv.grid(row = 20, column = 2,pady=5)

submitProv=tk.Button(interface_agregar[2], text="Registrar", background='#0781F4', fg='white',
relief=tk.FLAT, command = lambda: regProv(claveProv.get(), nombreProv.get(), rfcProv.get(), 
telProv.get(),empresaProv.get(),ciudadProv.get(), calleProv.get(), coloniaProv.get(), cpProv.get()))
submitProv.grid(row=24, column=2,pady=5)
#************************************************************************


#**************************************************Producto*****************************************
interface_agregar[3].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].configure(bg='white')
interface_agregar[3].pack_forget()

labelBox = tk.Label(interface_agregar[3], background = 'white', image = boxImg)
labelBox.grid(row = 4, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[3], text="   REGISTRO DE PRODUCTOS     ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[3], text="Código de barras:",font=("Fixedsys", 9), background='white').grid(row=2, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Nombre:",font=("Fixedsys", 9), background='white').grid(row=4, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Marca:",font=("Fixedsys", 9), background='white').grid(row=6, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Existencia:",font=("Fixedsys", 9), background='white').grid(row=8, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Costo:",font=("Fixedsys", 9), background='white').grid(row=10, column=1, pady=5)
ttk.Label(interface_agregar[3], text ="Punto de Reorden:",font=("Fixedsys", 9), background='white').grid(row = 12,column=1, pady=5)
ttk.Label(interface_agregar[3], text="Proveedor:",font=("Fixedsys", 9), background='white').grid(row=14, column=1, pady=5)
ttk.Label(interface_agregar[3], text="Categoria:",font=("Fixedsys", 9), background='white').grid(row=16, column=1, pady=5)

codigoProd = ttk.Entry(interface_agregar[3], width = 30)
codigoProd.grid(row = 2, column = 2, pady=5)

nombreProd = ttk.Entry(interface_agregar[3], width = 30)
nombreProd.grid(row = 4, column = 2, pady=5)

marcaProd = ttk.Entry(interface_agregar[3], width = 30)
marcaProd.grid(row = 6, column = 2, pady=5)

existProd = ttk.Entry(interface_agregar[3], width = 30)
existProd.grid(row = 8, column = 2, pady=5)

costoProd = ttk.Entry(interface_agregar[3], width = 30)
costoProd.grid(row = 10, column = 2, pady=5)

reordenProd = ttk.Entry(interface_agregar[3], width = 30)
reordenProd.grid(row = 12, column = 2, pady=5)

provedorProd = ttk.Entry(interface_agregar[3], width = 30)
provedorProd.grid(row = 14, column = 2, pady = 5)

categProd = tk.StringVar()
comboTwo = ttk.Combobox(interface_agregar[3], width = 28, textvariable = categProd,
state = "readonly", justify='center')
comboTwo['values'] = ("Refrescos", "Cerveza", "Botanas", "Abarrotes")
comboTwo.current(0)
comboTwo.grid(row = 16, column = 2, pady = 5)


submitProd=tk.Button(interface_agregar[3], text="Ingresar", background='#FF8F00', fg='white',
relief=tk.FLAT, command = lambda: regProd(codigoProd.get(), nombreProd.get(), marcaProd.get(), 
existProd.get(), costoProd.get(), reordenProd.get(), provedorProd.get(), categProd.get()))
submitProd.grid(row=18, column=2, pady=5)
#**************************************************************************

#**************************************** INGRESAR ****************************************
#Option -> Agregar
agregar_frames= []

for x in range(11):
    agregar_frames.append(tk.Frame(options))


title = tk.Frame(options, bg = '#005ea5')
title.grid(row=0, column=0, sticky='NWSE', pady=8)
labelTitle = ttk.Label(title, text = '      TIENDA DE \n    CONVENIENCIA', width = 20, background = '#90d2d8')
labelTitle.pack(side = tk.TOP, anchor = 'center')
labelTitle.config(font=("Courier", 20))
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

#**************************************** MOSTRAR ************************************

show = ttk.Label(options, text="MOSTRAR", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
show.grid(row=5, column=0, sticky='NWSE', pady=5)
#************************************************************************************
interface_agregar[4].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[4].configure(bg='white')
interface_agregar[4].rowconfigure(0, weight=1)
interface_agregar[4].rowconfigure(4, weight=1)
interface_agregar[4].columnconfigure(0, weight=1)
interface_agregar[4].columnconfigure(1, weight=2)
interface_agregar[4].columnconfigure(2, weight=2)
interface_agregar[4].columnconfigure(3, weight=2)
interface_agregar[4].pack_forget()

ttk.Label(interface_agregar[4], text="       \t LISTA DE EMPLEADOS     ", 
font=("Times", 20), background='white').grid(row=0, column=2, sticky='NEWS')

agregar_frames[4]=tk.Frame(options, bg = '#080808')
agregar_frames[4].grid(row=6,column=0,sticky='NWSE', pady=2, padx=10)
employeeShow=ttk.Label(agregar_frames[4], text="EMPLEADO", anchor=tk.CENTER, background='#E0E0E0')
employeeShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
employeeShow.bind("<Button-1>", lambda x: OnClick(4))
employeeShow.bind("<Enter>", LabelEnter)
employeeShow.bind("<Leave>", LabelLeave)
#********************************************************************************************
interface_agregar[5].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[5].configure(bg='white')

interface_agregar[5].rowconfigure(0, weight=1)
interface_agregar[5].rowconfigure(2, weight=1)
interface_agregar[5].rowconfigure(3, weight=1)
interface_agregar[5].columnconfigure(0, weight=1)
interface_agregar[5].columnconfigure(1, weight=2)
interface_agregar[5].columnconfigure(2, weight=2)
interface_agregar[5].columnconfigure(3, weight=2)
interface_agregar[5].pack_forget()

ttk.Label(interface_agregar[5], text="       \t LISTA DE PROVEEDORES     ", 
font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

agregar_frames[5]=tk.Frame(options, bg = '#080808')
agregar_frames[5].grid(row=7,column=0,sticky='NWSE', pady=2, padx=10)
supplierShow=ttk.Label(agregar_frames[5], text="PROVEEDOR", anchor=tk.CENTER, background='#E0E0E0')
supplierShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
supplierShow.bind("<Button-1>", lambda x: OnClick(5))
supplierShow.bind("<Enter>", LabelEnter)
supplierShow.bind("<Leave>", LabelLeave)
#*************************************************************************
interface_agregar[6].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[6].configure(bg='white')
interface_agregar[6].rowconfigure(0, weight=1)
interface_agregar[6].rowconfigure(2, weight=1)
interface_agregar[6].rowconfigure(3, weight=1)
interface_agregar[6].columnconfigure(0, weight=1)
interface_agregar[6].columnconfigure(1, weight=2)
interface_agregar[6].columnconfigure(2, weight=2)
interface_agregar[6].columnconfigure(3, weight=2)
interface_agregar[6].pack_forget()

ttk.Label(interface_agregar[6], text="       \t LISTA DE PRODUCTOS     ", 
font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

agregar_frames[6]=tk.Frame(options, bg = '#080808')
agregar_frames[6].grid(row=8,column=0,sticky='NWSE', pady=2, padx=10)
supplierShow=ttk.Label(agregar_frames[6], text="PRODUCTO", anchor=tk.CENTER, background='#E0E0E0')
supplierShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
supplierShow.bind("<Button-1>", lambda x: OnClick(6))
supplierShow.bind("<Enter>", LabelEnter)
supplierShow.bind("<Leave>", LabelLeave)
#*******************************************************************
interface_agregar[7].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[7].configure(bg='white')
interface_agregar[7].rowconfigure(0, weight=1)
interface_agregar[7].rowconfigure(2, weight=1)
interface_agregar[7].rowconfigure(3, weight=1)
interface_agregar[7].columnconfigure(0, weight=1)
interface_agregar[7].columnconfigure(1, weight=2)
interface_agregar[7].columnconfigure(2, weight=2)
interface_agregar[7].columnconfigure(3, weight=2)
interface_agregar[7].pack_forget()

ttk.Label(interface_agregar[7], text="       \t\tLISTA DE VENTAS     ", 
font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

agregar_frames[7]=tk.Frame(options, bg = '#080808')
agregar_frames[7].grid(row=9,column=0,sticky='NWSE', pady=2, padx=10)
supplierShow=ttk.Label(agregar_frames[7], text="VENTAS", anchor=tk.CENTER, background='#E0E0E0')
supplierShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
supplierShow.bind("<Button-1>", lambda x: OnClick(7))
supplierShow.bind("<Enter>", LabelEnter)
supplierShow.bind("<Leave>", LabelLeave)

#*************************************CATEGORIAS*************************************
categ = ttk.Label(options, text="CATEGORIAS", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
categ.grid(row=10, column=0, sticky='NWSE', pady=5)
#**************************************************************************
interface_agregar[8].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[8].configure(bg='white')
interface_agregar[8].pack_forget()

ttk.Label(interface_agregar[8], text="       \t FORMAS DE PAGO     ", 
font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

agregar_frames[8]=tk.Frame(options, bg = '#080808')
agregar_frames[8].grid(row=11,column=0,sticky='NWSE', pady=2, padx=10)
prodCatShow=ttk.Label(agregar_frames[8], text="FORMAS DE PAGO", anchor=tk.CENTER, background='#E0E0E0')
prodCatShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
prodCatShow.bind("<Button-1>", lambda x: OnClick(8))
prodCatShow.bind("<Enter>", LabelEnter)
prodCatShow.bind("<Leave>", LabelLeave)
#********************************************************************************
interface_agregar[9].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[9].configure(bg='white')
interface_agregar[9].pack_forget()

ttk.Label(interface_agregar[9], text="\n CATEGORIAS DE PRODUCTOS \n", 
font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

agregar_frames[9]=tk.Frame(options, bg = '#080808')
agregar_frames[9].grid(row=12,column=0,sticky='NWSE', pady=2, padx=10)
prodCatShow=ttk.Label(agregar_frames[9], text="PRODUCTOS", anchor=tk.CENTER, background='#E0E0E0')
prodCatShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
prodCatShow.bind("<Button-1>", lambda x: OnClick(9))
prodCatShow.bind("<Enter>", LabelEnter)
prodCatShow.bind("<Leave>", LabelLeave)
#**************************************** VENTAS ************************************
interface_agregar[10].pack(side='bottom',fill=tk.BOTH, expand=True)
interface_agregar[10].configure(bg='white')
interface_agregar[10].pack_forget()

sales = ttk.Label(options, text="VENTAS", anchor=tk.CENTER, background='#0C73A2', foreground='#FFFFFF')
sales.grid(row=13, column=0, sticky='NWSE', pady=5)

agregar_frames[10]=tk.Frame(options, bg = '#080808')
agregar_frames[10].grid(row=14,column=0,sticky='NWSE', pady=2, padx=10)
salesShow=ttk.Label(agregar_frames[10], text="REGISTRAR VENTAS", anchor=tk.CENTER, background='#E0E0E0')
salesShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
salesShow.bind("<Button-1>", lambda x: OnClick(10))
salesShow.bind("<Enter>", LabelEnter)
salesShow.bind("<Leave>", LabelLeave)

labelSale = tk.Label(interface_agregar[10], background = 'white', image = saleImg)
labelSale.grid(row = 4, column = 4, columnspan = 2, rowspan = 12)

ttk.Label(interface_agregar[10], text="\tREGISTRO DE VENTAS \n   ", 
font=("Times", 20), background='white').grid(row=0, column=2)
ttk.Label(interface_agregar[10], text="Clave venta:",font=("Fixedsys", 9), background='white').grid(row=2, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Código de barras:",font=("Fixedsys", 9), background='white').grid(row=4, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Cantidad:",font=("Fixedsys", 9), background='white').grid(row=6, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Precio unitario:",font=("Fixedsys", 9), background='white').grid(row=8, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Importe",font=("Fixedsys", 9), background='white').grid(row=10, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Fecha venta:",font=("Fixedsys", 9), background='white').grid(row=12, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Forma pago:",font=("Fixedsys", 9), background='white').grid(row=14, column=1, pady=5)
ttk.Label(interface_agregar[10], text="Clave empleado:",font=("Fixedsys", 9), background='white').grid(row=16, column=1, pady=5)



codigoVenta = ttk.Entry(interface_agregar[10], width = 30)
codigoVenta.grid(row = 2, column = 2, pady=5)

codigoProdVenta = ttk.Entry(interface_agregar[10], width = 30)
codigoProdVenta.grid(row = 4, column = 2, pady=5)


cantidadVenta = ttk.Entry(interface_agregar[10], width = 30)
cantidadVenta.grid(row = 6, column = 2, pady=5)


precioUnitVenta = ttk.Entry(interface_agregar[10], width = 30)
precioUnitVenta.grid(row = 8, column = 2, pady=5)


importeVenta = ttk.Entry(interface_agregar[10], width = 30)
importeVenta.grid(row = 10, column = 2, pady=5)


fechaVenta = MyDateEntry(interface_agregar[10],
                 width=28,
                 justify='center',
                 selectbackground='gray80',
                 selectforeground='black',
                 normalbackground='white',
                 normalforeground='black',
                 background='gray90',
                 foreground='black',
                 bordercolor='gray90',
                 othermonthforeground='gray50',
                 othermonthbackground='white',
                 othermonthweforeground='gray50',
                 othermonthwebackground='white',
                 weekendbackground='white',
                 weekendforeground='black',
                 headersbackground='white',
                 headersforeground='gray70')
            
fechaVenta.grid(row = 12, column = 2, pady = 5)

pago_var = tk.StringVar()
comboOne = ttk.Combobox(interface_agregar[10], width = 28, textvariable = pago_var,
state = "readonly", justify='center')
comboOne['values'] = ("Cheque", "Vale", "Tarjeta de Credito", "Tarjeta de Debito",
"Pagaré", "Efectivo")
comboOne.current(0)
comboOne.grid(row = 14, column = 2,)


codigoEmpVenta = ttk.Entry(interface_agregar[10], width = 30)
codigoEmpVenta.grid(row = 16, column = 2, pady = 5)

submitVenta=tk.Button(interface_agregar[10], text="Ingresar", background='#2ECC71', fg='white',
relief=tk.FLAT, command = lambda: regVenta(codigoVenta.get(), codigoProdVenta.get(), cantidadVenta.get(),
precioUnitVenta.get(), importeVenta.get(), fechaVenta.get(), pago_var.get(), codigoEmpVenta.get()))
submitVenta.grid(row=18, column = 2, pady = 5)
#************************************************************************************

#*****************************************************************************************
style = ttk.Style(window)
style.theme_use('clam')
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
            ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
            ("Custom.Treeheading.text", {'sticky':'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading",
    background="#212F3C", foreground="white",font=('Calibri',10,'bold') ,relief="flat")

employeeTable = ttk.Treeview(interface_agregar[4],style="Custom.Treeview")
employeeTable.grid(row=1, column=1, columnspan=2, padx=15, pady=5)
employeeTable['columns'] = (
                             'nombre','apellidoP','apellidoM','rfc','fechaNac',
                             'fechaIng','ciudad','estado','pais','calle',
                             'colonia','cp','telefono','sueldo'
                            )


supplierTable = ttk.Treeview(interface_agregar[5], style="Custom.Treeview")
supplierTable.grid(row=2, column=1,sticky='NEWS')
supplierTable['columns'] = ('Nombre', 'RFC', 'Telefono', 'Empresa', 'Ciudad', 'Calle', 
                            'Colonia', 'CP')

productTable = ttk.Treeview(interface_agregar[6], style="Custom.Treeview")
productTable.grid(row=2, column=1,sticky='NEWS')
productTable['columns'] = ('Nombre', 'Marca', 'Existencia', 'Costo', 'Punto de Reorden',
'Proveedor', 'Categoria')

categoPagoTable = ttk.Treeview(interface_agregar[8], style = "Custom.Treeview")
categoPagoTable.grid(row = 2, column = 1, sticky = 'NEWS')
categoPagoTable['columns'] = ("Cheque", "Vale", "Tarjeta de Credito", "Tarjeta de Debito",
"Pagaré", "Efectivo")

categoProdTable = ttk.Treeview(interface_agregar[9], style = "Custom.Treeview")
categoProdTable.grid(row = 2, column = 1, sticky = 'NEWS')
categoProdTable['columns'] = ('Abarrotes', 'Botanas', 'Cervezas', 'Refrescos')

saleTable = ttk.Treeview(interface_agregar[7], style = "Custom.Treeview")
saleTable.grid(row = 1, column = 1, sticky = 'NEWS')
saleTable['columns'] = ('Codigo Producto', 'Cantidad', 'Precio Unitario',
'Importe', 'Fecha de Venta', 'Forma de Pago', 'Clave Empleado')
#--------------------scrollbar----------------
employee_xscrollb= ttk.Scrollbar(interface_agregar[4], orient="horizontal", command=employeeTable.xview)
employee_xscrollb.grid(row=3, column=1, columnspan=2, sticky='WE')
employeeTable.configure(xscrollcommand=employee_xscrollb.set)

employee_yscrollb= ttk.Scrollbar(interface_agregar[4], orient="vertical", command=employeeTable.yview)
employee_yscrollb.grid(row=1, column=4, sticky='NS')
employeeTable.configure(yscrollcommand=employee_yscrollb.set)

supplier_yscrollb= ttk.Scrollbar(interface_agregar[5], orient="vertical", command=supplierTable.yview)
supplier_yscrollb.grid(row=2, column=2, sticky='NS')
supplierTable.configure(yscrollcommand=supplier_yscrollb.set)

product_yscrollb= ttk.Scrollbar(interface_agregar[6], orient="vertical", command=productTable.yview)
product_yscrollb.grid(row=2, column=2, sticky='NS')
productTable.configure(yscrollcommand=product_yscrollb.set)

sale_yscrollb = ttk.Scrollbar(interface_agregar[7], orient = "vertical", command = saleTable.yview)
sale_yscrollb.grid(row = 1, column = 2, sticky = 'NS')
saleTable.configure(yscrollcommand = sale_yscrollb.set)

def tableEmp():
    employeeTable.heading("#0", text='ID', anchor='center')
    employeeTable.column("#0", anchor="w",width=80, stretch=False)
    employeeTable.heading('nombre', text='Nombre')
    employeeTable.column('nombre', anchor='center', width=80, stretch=False)
    employeeTable.heading('apellidoP', text='Apellido P')
    employeeTable.column('apellidoP', anchor='center', width=80, stretch=False)
    employeeTable.heading('apellidoM', text='Apelldio M')
    employeeTable.column('apellidoM', anchor='center', width=80, stretch=False)
    employeeTable.heading('rfc', text='RFC')
    employeeTable.column('rfc', anchor='center', width=80, stretch=False)
    employeeTable.heading('fechaNac', text='FechaNac')
    employeeTable.column('fechaNac', anchor='center', width=80, stretch=False)
    employeeTable.heading('fechaIng', text='FechaIng')
    employeeTable.column('fechaIng', anchor='center', width=80, stretch=False)
    employeeTable.heading('ciudad', text='Ciudad')
    employeeTable.column('ciudad', anchor='center', width=80, stretch=False)
    employeeTable.heading('estado', text='Estado')
    employeeTable.column('estado', anchor='center', width=80, stretch=False)
    employeeTable.heading('pais', text='Pais')
    employeeTable.column('pais', anchor='center', width=80, stretch=False)
    employeeTable.heading('calle', text='Calle')
    employeeTable.column('calle', anchor='center', width=80, stretch=False)
    employeeTable.heading('colonia', text='Colonia')
    employeeTable.column('colonia', anchor='center', width=80, stretch=False)
    employeeTable.heading('cp', text='CP')
    employeeTable.column('cp', anchor='center', width=80, stretch=False)
    employeeTable.heading('telefono', text='Tel')
    employeeTable.column('telefono', anchor='center', width=80, stretch=False)
    employeeTable.heading('sueldo', text='Sueldo')
    employeeTable.column('sueldo', anchor='center', width=80, stretch=False)


def tableSupplier():
    supplierTable.heading("#0", text='ID', anchor='center')
    supplierTable.column("#0", anchor="w",width=80)   
    supplierTable.heading("Nombre", text='Nombre')
    supplierTable.column("Nombre", anchor="center",width=80)   
    supplierTable.heading("RFC", text='RFC')
    supplierTable.column("RFC", anchor="center",width=80)  
    supplierTable.heading("Telefono", text='Telefono')
    supplierTable.column("Telefono", anchor="center",width=80) 
    supplierTable.heading("Empresa", text='Empresa')
    supplierTable.column("Empresa", anchor="center",width=80)   
    supplierTable.heading("Ciudad", text='Ciudad')
    supplierTable.column("Ciudad", anchor="center",width=80)   
    supplierTable.heading("Calle", text='Calle')
    supplierTable.column("Calle", anchor="center",width=80)   
    supplierTable.heading("Colonia", text='Colonia')
    supplierTable.column("Colonia", anchor="center",width=80)   
    supplierTable.heading("CP", text='CP')
    supplierTable.column("CP", anchor="center",width=80)  

def tableProduct():
    productTable.heading("#0", text='Codigo Barras', anchor='center')
    productTable.column("#0", anchor="w",width=80)   
    productTable.heading("Nombre", text='Nombre')
    productTable.column("Nombre", anchor="center",width=80)   
    productTable.heading("Marca", text='Marca')
    productTable.column("Marca", anchor="center",width=80)  
    productTable.heading("Existencia", text='Existencia')
    productTable.column("Existencia", anchor="center",width=80)   
    productTable.heading("Costo", text='Costo')
    productTable.column("Costo", anchor="center",width=80)   
    productTable.heading("Punto de Reorden", text = "Punto de Reorden")
    productTable.column("Punto de Reorden", anchor = "center", width = 80)
    productTable.heading("Proveedor", text='Proveedor')
    productTable.column("Proveedor", anchor="center",width=80)   
    productTable.heading("Categoria", text='Categoria')
    productTable.column("Categoria", anchor="center",width=80)   

def tableCatPago():
    categoPagoTable.heading("#0", text='ID Venta', anchor='center')
    categoPagoTable.column("#0", anchor="w",width=80)   
    categoPagoTable.heading("Cheque", text='Cheque')
    categoPagoTable.column("Cheque", anchor="center",width=80)   
    categoPagoTable.heading("Vale", text='Vale')
    categoPagoTable.column("Vale", anchor="center",width=80)  
    categoPagoTable.heading("Tarjeta de Credito", text='Tarjeta de Credito')
    categoPagoTable.column("Tarjeta de Credito", anchor="center",width=80)   
    categoPagoTable.heading("Tarjeta de Debito", text='Tarjeta de Debito')
    categoPagoTable.column("Tarjeta de Debito", anchor="center",width=80)   
    categoPagoTable.heading("Pagaré", text='Pagaré')
    categoPagoTable.column("Pagaré", anchor="center",width=80)   
    categoPagoTable.heading("Efectivo", text='Efectivo')
    categoPagoTable.column("Efectivo", anchor="center",width=80) 

def tableCatProd():
    categoProdTable.heading("#0", text='ID Producto', anchor='center')
    categoProdTable.column("#0", anchor="w",width=80)   
    categoProdTable.heading("Abarrotes", text='Abarrotes')
    categoProdTable.column("Abarrotes", anchor="center",width=80)   
    categoProdTable.heading("Botanas", text='Botanas')
    categoProdTable.column("Botanas", anchor="center",width=80)  
    categoProdTable.heading("Cervezas", text='Cervezas')
    categoProdTable.column("Cervezas", anchor="center",width=80)   
    categoProdTable.heading("Refrescos", text='Refrescos')
    categoProdTable.column("Refrescos", anchor="center",width=80)   

def tableSale():
    saleTable.heading("#0", text='Clave de Venta', anchor='center')
    saleTable.column("#0", anchor="w",width=80)   
    saleTable.heading("Codigo Producto", text='Codigo Producto')
    saleTable.column("Codigo Producto", anchor="center",width=80)   
    saleTable.heading("Cantidad", text='Cantidad')
    saleTable.column("Cantidad", anchor="center",width=80)  
    saleTable.heading("Precio Unitario", text='Precio Unitario')
    saleTable.column("Precio Unitario", anchor="center",width=80)   
    saleTable.heading("Importe", text='Importe')
    saleTable.column("Importe", anchor="center",width=80)   
    saleTable.heading("Fecha de Venta", text='Fecha de Venta')
    saleTable.column("Fecha de Venta", anchor="center",width=80)   
    saleTable.heading("Forma de Pago", text='Forma de Pago')
    saleTable.column("Forma de Pago", anchor="center",width=80)
    saleTable.heading("Clave Empleado", text = "Clave Empleado")
    saleTable.column("Clave Empleado", anchor = "center", width = 80)

main()
