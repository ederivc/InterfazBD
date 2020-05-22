import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import mysql.connector as mysql

def start():
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
        showPayment(categoPagoTable)
        showProducCatego(categoProdTable)
        showTransaction(transactionTable)
        showProdOrd(prodOrdTable)
        tableEmp()
        tableSupplier()
        tableProduct()
        tableCatPago()
        tableCatProd()
        tableProdOrd()
        tableSale()
        tableTransaction()


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
            showTransaction(transactionTable)
            labelDisplay.pack(side='top')
            ShowAgregar(8)
            display.config(bg='#3EBD5E') 
        if(event == 9):
            showProdOrd(prodOrdTable)
            labelDisplay.pack(side='top')
            ShowAgregar(9)
            display.config(bg='#2ECC71')   
        if(event == 10):
            labelDisplay.pack(side='top')
            ShowAgregar(10)
            display.config(bg='#2ECC71') 
        if(event == 11):
            showProducCatego(categoProdTable)
            labelDisplay.pack(side='top')
            ShowAgregar(11)
            display.config(bg='#3EBD5E')       
        if(event == 12):
            labelDisplay.pack(side='top')
            ShowAgregar(12)
            display.config(bg='#3EBD5E')   
        if(event == 13):
            showPayment(categoPagoTable)
            labelDisplay.pack(side='top')
            ShowAgregar(13)
            display.config(bg='#3EBD5E') 
        if(event == 14):
            showProducCatego(categoProdTable)
            labelDisplay.pack(side='top')
            ShowAgregar(14)
            display.config(bg='#3EBD5E') 
        if(event == 15):
            labelDisplay.pack(side='top')
            ShowAgregar(15)
            display.config(bg='#3EBD5E')  
        return


    def llenarDatosEmp(event):
        try:
            idEmp = int(aidiEmpMod.get())
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employee WHERE id = %s",(idEmp,))
            empleado = cursor.fetchone()
            cursor.close()

            nombreEmpMod.delete(0, END)
            apPatEmpMod.delete(0, END)
            apMatEmpMod.delete(0, END)
            rfcEmpMod.delete(0, END)
            ciudadEmpMod.delete(0, END)
            estadoEmpMod.delete(0, END)
            paisEmpMod.delete(0, END)
            calleEmpMod.delete(0, END)
            coloniaEmpMod.delete(0, END)
            cpEmpMod.delete(0, END)
            telEmpMod.delete(0, END)
            sueldoEmpMod.delete(0, END)

            nombreEmpMod.insert(0, empleado[1])
            apPatEmpMod.insert(0, empleado[2])
            apMatEmpMod.insert(0, empleado[3])
            rfcEmpMod.insert(0, empleado[4])
            fechaNacEmpMod.set_date(empleado[5])
            fechaIngresoEmpMod.set_date(empleado[6])
            ciudadEmpMod.insert(0, empleado[7])
            estadoEmpMod.insert(0, empleado[8])
            paisEmpMod.insert(0, empleado[9])
            calleEmpMod.insert(0, empleado[10])
            coloniaEmpMod.insert(0, empleado[11])
            cpEmpMod.insert(0, empleado[12])
            telEmpMod.insert(0, empleado[13])
            sueldoEmpMod.insert(0, empleado[14])

        except Exception as e:
            mBox.showerror("ERROR", "Empleado no encontrado")

    def llenarDatosProv(event):
        try:
            idProv = int(claveProvMod.get())
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM supplier WHERE claveProv = %s",(idProv,))
            proveedor = cursor.fetchone()
            cursor.close()

            nombreProvMod.delete(0, END)
            apPatProvMod.delete(0, END)
            apMatProvMod.delete(0, END)
            rfcProvMod.delete(0, END)
            ciudadProvMod.delete(0, END)
            calleProvMod.delete(0, END)
            coloniaProvMod.delete(0, END)
            cpProvMod.delete(0, END)
            telProvMod.delete(0, END)
            empresaProvMod.delete(0, END)

            nombreProvMod.insert(0, proveedor[1])
            apPatProvMod.insert(0, proveedor[2])
            apMatProvMod.insert(0, proveedor[3])
            rfcProvMod.insert(0, proveedor[4])
            telProvMod.insert(0, proveedor[5])
            empresaProvMod.insert(0,proveedor[6])
            ciudadProvMod.insert(0, proveedor[7])
            calleProvMod.insert(0,proveedor[8])
            coloniaProvMod.insert(0, proveedor[9])
            cpProvMod.insert(0, proveedor[10])

        except Exception as e:
            mBox.showerror("ERROR", "Proveedor no encontrado")

    def llenarDatosProd(event):
        try:
            idProd = int(codigoProdMod.get())
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM product WHERE codigoProd = %s",(idProd,))
            producto = cursor.fetchone()
            cursor.close()

            nombreProdMod.delete(0, END)
            marcaProdMod.delete(0, END)
            existProdMod.delete(0, END)
            costoProdMod.delete(0, END)
            precioventaProdMod.delete(0, END)
            reordenProdMod.delete(0, END)
            proveedorProdMod.delete(0, END)
            comboTwoMod.current(0)


            nombreProdMod.insert(0, producto[1])
            marcaProdMod.insert(0, producto[2])
            existProdMod.insert(0, producto[3])
            costoProdMod.insert(0, producto[4])
            precioventaProdMod.insert(0, producto[5])
            reordenProdMod.insert(0,producto[6])
            proveedorProdMod.insert(0, producto[7])
            comboTwoMod.set(producto[8])



        except Exception as e:
            mBox.showerror("ERROR", "Producto no encontrado")

    def fprecioVenta(event):
        if cantidadVenta.get():
            try:
                codigo= int(codigoProdVenta.get())
                cantidad = int(cantidadVenta.get())
                connection = mysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='registration')         
                operacion = connection.cursor()
                operacion.execute("SELECT precioventaProd FROM product WHERE codigoProd = %s",(codigo,)) 
                valor = operacion.fetchone()
                valorProd=float(valor[0])
                precioUnitVenta.config(text=str(valorProd))
                importe=str(valorProd*cantidad)
                importeVenta.config(text=importe)
                operacion.close()
        
            except Exception as e:
                mBox.showerror("ERROR", "Producto no registrado")


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
            fechaNacEmpStr = fechaNacEmp.get_date().strftime('%Y-%m-%d')
            fechaIngresoEmpStr = fechaIngresoEmp.get_date().strftime('%Y-%m-%d')
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')         
            mySql_insert_query  =f"""INSERT INTO employee VALUES ({aidi.get()}, '{nombreEmp.get()}', 
            '{apPatEmp.get()}','{apMatEmp.get()}', '{rfcEmp.get()}', '{fechaNacEmpStr}', 
            '{fechaIngresoEmpStr}', '{ciudadEmp.get()}', '{estadoEmp.get()}', '{paisEmp.get()}', 
            '{calleEmp.get()}', '{coloniaEmp.get()}', '{cpEmp.get()}', '{telEmp.get()}','{sueldoEmp.get()}')"""
            
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            mBox.showinfo("EMPLEADOS", "El usuario: " + str(aidi.get()) + " ha sido"+
            " agregado correctamente")
            cursor.close()

            aidi.delete(0, END), nombreEmp.delete(0, END), apPatEmp.delete(0, END), 
            apMatEmp.delete(0, END), rfcEmp.delete(0, END), fechaNacEmp.delete(0, END),
            fechaIngresoEmp.delete(0, END),ciudadEmp.delete(0, END), estadoEmp.delete(0, END), 
            paisEmp.delete(0, END),calleEmp.delete(0, END), coloniaEmp.delete(0, END), 
            cpEmp.delete(0, END), telEmp.delete(0, END), sueldoEmp.delete(0, END)

        except Exception as e:
            mBox.showerror("ERROR", "No se pudo registrar al empleado, verifique sus "+
            "datos.")
            print("Failed to insert record into Employee table {}".format(e))   

    def regProv(cveProv, nombreProv, apPatProv, apMatProv, rfcProv, telefonoProv, empresaProv, 
    ciudadProv, calleProv, coloniaProv, cpProv):
        try:
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')
            mySql_insert_query  =f"""INSERT INTO supplier VALUES ({cveProv.get()}, 
            '{nombreProv.get()}', '{apPatProv.get()}', '{apMatProv.get()}', '{rfcProv.get()}', 
            '{telefonoProv.get()}','{empresaProv.get()}', '{ciudadProv.get()}', 
            '{calleProv.get()}', '{coloniaProv.get()}', '{cpProv.get()}')"""

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            mBox.showinfo("PROVEEDORES", "El proveedor: " + str(cveProv.get()) + " ha sido"+
            " agregado correctamente")
            cursor.close()
            
            cveProv.delete(0, END), nombreProv.delete(0, END), apPatProv.delete(0, END),
            apMatProv.delete(0, END), rfcProv.delete(0, END),telefonoProv.delete(0, END), 
            empresaProv.delete(0, END), ciudadProv.delete(0, END),calleProv.delete(0, END), 
            coloniaProv.delete(0, END), cpProv.delete(0, END)

        except Exception as e:
            mBox.showerror("ERROR", "No se pudo registrar al proveedor, verifique sus "+
            "datos.")
            print("Failed to insert record into Supplier table {}".format(e))


    def regProd(codigoProd, nombreProd, marcaProd, existProd, costoProd,
    precioVProd, reordenProd, provedorProd, categProd):
        while TRUE:
            try:
                connection = mysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='registration')
                mySql_insert_query  =f"""INSERT INTO product VALUES ({codigoProd.get()}, 
                '{nombreProd.get()}', '{marcaProd.get()}', '{existProd.get()}',
                '{costoProd.get()}',{precioVProd.get()} ,'{reordenProd.get()}',
                '{provedorProd.get()}', '{categProd}')"""

                x = verificaProv(provedorProd.get())
                if(x == FALSE):
                    mBox.showerror("ERROR", "El proveedor que ingresaste no existe.")
                    break

                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                mBox.showinfo("PRODUCTOS", "El producto: " + str(codigoProd.get()) + " ha sido"+
                " agregado correctamente")
                cursor.close()

                codigoProd.delete(0, END), nombreProd.delete(0, END), marcaProd.delete(0, END),
                existProd.delete(0, END), costoProd.delete(0, END), precioVProd.delete(0, END),
                reordenProd.delete(0, END), provedorProd.delete(0, END)
                break

            except Exception as e:
                mBox.showerror("ERROR", "No se pudo registrar el producto, verifique sus "+
                "datos.")
                print("Failed to insert record into Product table {}".format(e))
                break

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

                x = verificaEmpleado(idEmp)
                if(x == FALSE):
                    mBox.showerror("ERROR", "El empleado que ingresaste no existe.")
                    break

                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                mBox.showinfo("VENTAS", "La venta: " + str(claveVenta) + " ha sido"+
                " relizada")
                elimina(codigoProd, cantidad)
                #verificaReo(codigoProd)
                cursor.close()
                break
            except Exception as e:
                mBox.showerror("ERROR", "No se pudo realizar la venta, verifique sus "+
                "datos.")
                print("Failed to insert record into Sales table {}".format(e))
                break

    def regVenta_2(claveVenta, codigoProd, cantidad, precioUnit, importe,
    fechaVent, formaPago, idEmp):
        while TRUE:
            try:
                fecheVentStr = fechaVent.get_date().strftime('%Y-%m-%d')
                if len(carrito)==0:
                    mBox.showerror("ERROR", "El carrito esta vacío")
                    break
                connection = mysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='registration')

                x = verificaEmpleado(idEmp)
                if(x == FALSE):
                    mBox.showerror("ERROR", "El empleado que ingresaste no existe.")
                    break
                cursor = connection.cursor()

                importeTotal=0
                for index in range(len(carrito)):
                    mySql_insert_query_2  =f"""INSERT INTO transaction VALUES ('{claveVenta}', '{carrito[index].get('codigoProd')}', 
                    '{carrito[index].get('cantidad')}', '{carrito[index].get('precioUnit')}', '{carrito[index].get('importe')}')"""
                    cursor.execute(mySql_insert_query_2)
                    elimina(carrito[index].get('codigoProd'), carrito[index].get('cantidad'))
                    importeTotal += carrito[index].get('importe')
                    #verificaReo(carrito[index].get('codigoProd')) 

                mySql_insert_query  =f"""INSERT INTO sales VALUES ('{claveVenta}', '{importeTotal}', '{fecheVentStr}', '{formaPago}', '{idEmp}')"""
                cursor.execute(mySql_insert_query)
                connection.commit()

                codigoVenta.delete(0, END)
                codigoEmpVenta.delete(0,END) 
                
                mBox.showinfo("VENTAS", "La venta: " + str(claveVenta) + " ha sido"+
                " relizada")

                for x in range(len(carrito)):
                    carrito.pop() 

                cursor.close()
                break
            except Exception as e:
                mBox.showerror("ERROR", "No se pudo realizar la venta, verifique sus "+
                "datos.")
                print("Failed to insert record into Sales table {}".format(e))
                break

    def regConcepto(codigoProd, cantidad, precioUnit, importe):
        while TRUE:
            try:
                codigoProd=int(codigoProd)
                cantidad =int(cantidad)
                precioUnit = float(precioUnit)
                importe = float (importe)
                        
                check, index = verificaCarrito(codigoProd)
                if check:
                    cantidad += carrito[index].get('cantidad')
                    importe += carrito[index].get('importe')
                    i = verifica(codigoProd, cantidad)
                    if(i == FALSE):
                        mBox.showerror("ERROR", "Excediste el limite de compra, intenta de nuevo.")
                        break 
                    carrito[index].update({'cantidad': cantidad})
                    carrito[index].update({'importe': importe})
                else:    
                    i = verifica(codigoProd, cantidad)
                    if(i == FALSE):
                        mBox.showerror("ERROR", "Excediste el limite de compra, intenta de nuevo.")
                        break 

                    venta={
                        'codigoProd':codigoProd, 
                        'cantidad': cantidad,
                        'precioUnit': precioUnit,
                        'importe': importe
                        }
                    carrito.append(venta.copy())
                print(carrito) 
                
                
                codigoProdVenta.delete(0, END)
                cantidadVenta.delete(0,END)
                importeVenta.config(text='0')
                precioUnitVenta.config(text='0')

                mBox.showinfo("CARRITO", "El producto " + str(codigoProd) + " ha sido "+
                "agregago al carrito")
                break
            except Exception as e:
                mBox.showerror("ERROR", "Datos incorrectos.")
                print("Failed to insert record into transaction table {}".format(e))
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
        for claveProv, nombreProv, apPatProv,apMatProv, rfcProv,telefonoProv,empresaProv,ciudadProv,calleProv,coloniaProv,cpProv in operacion.fetchall():
            supplierTable.insert('', 'end', text = claveProv, values=(nombreProv, apPatProv,
            apMatProv, rfcProv,telefonoProv, empresaProv,ciudadProv, calleProv, coloniaProv, cpProv))
        conexion.close()

    def showProduct(productTable):
        for i in productTable.get_children():
            productTable.delete(i)

        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        operacion.execute( "SELECT * FROM product" )
        for codigoProd,nombreProd,marcaProd,existProd,costoProd, precioventaProd,reordenProd,provedorProd,categProd in operacion.fetchall():
            productTable.insert('', 'end', text = codigoProd, values=(nombreProd,marcaProd,existProd,
            costoProd,precioventaProd,reordenProd,provedorProd,categProd))
        conexion.close()

    def showProdOrd(prodOrdTable):
        for i in prodOrdTable.get_children():
            prodOrdTable.delete(i)

        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        operacion.execute("SELECT * FROM product WHERE existencia < reordenProd")
        for codigoProd,nombreProd,marcaProd,existProd,costoProd, precioventaProd,reordenProd,provedorProd,categProd in operacion.fetchall():
            prodOrdTable.insert('', 'end', text = codigoProd, values=(nombreProd,marcaProd,existProd,
            costoProd,precioventaProd,reordenProd,provedorProd,categProd))
        conexion.close()   

    def showSale(saleTable):
        for i in saleTable.get_children():
            saleTable.delete(i)

        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        operacion.execute( "SELECT * FROM sales" )
        for clave,importeT,fecha,fPago, claveEmp in operacion.fetchall():
            saleTable.insert('', 'end', text = clave, values=(importeT, fecha,fPago,claveEmp))
        conexion.close()

    def showTransaction(transactionTable):
        for i in transactionTable.get_children():
            transactionTable.delete(i)

        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()    

        operacion.execute("SELECT clave, codigoProd, cantidad, precioUni, importe FROM transaction")
        for clave, codigoProd, cantidad, precioUni, importe in operacion.fetchall():
            transactionTable.insert('','end', text = clave, values = (codigoProd, cantidad,
            precioUni, importe))
        conexion.close()
        
    def showPayment(categoPagoTable):
        for i in categoPagoTable.get_children():
            categoPagoTable.delete(i)

        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        
        operacion.execute("SELECT clave, importeT FROM sales WHERE fPago = 'Cheque'")
        for clave, importeT in operacion.fetchall():
            categoPagoTable.insert('','end', text = clave, values = (importeT,'-',
            '-','-','-','-'))

        operacion.execute("SELECT clave, importeT FROM sales WHERE fPago = 'Vale'")
        for clave, importeT in operacion.fetchall():
            categoPagoTable.insert('','end', text = clave, values = ("-",importeT,
            '-','-','-','-'))

        operacion.execute("SELECT clave, importeT FROM sales WHERE fPago = 'Tarjeta de Credito'")
        for clave, importeT in operacion.fetchall():
            categoPagoTable.insert('','end', text = clave, values = ("-","-",
            importeT,'-','-','-'))

        operacion.execute("SELECT clave, importeT FROM sales WHERE fPago = 'Tarjeta de Debito'")
        for clave, importeT in operacion.fetchall():
            categoPagoTable.insert('','end', text = clave, values = ("-","-",
            '-',importeT,'-','-'))

        operacion.execute("SELECT clave, importeT FROM sales WHERE fPago = 'Pagaré'")
        for clave, importeT in operacion.fetchall():
            categoPagoTable.insert('','end', text = clave, values = ("-","-",
            '-','-',importeT,'-'))

        operacion.execute("SELECT clave, importeT FROM sales WHERE fPago = 'Efectivo'")
        for clave, importeT in operacion.fetchall():
            categoPagoTable.insert('','end', text = clave, values = ("-","-",
            '-','-','-',importeT))

        conexion.close()

    def showProducCatego(categoProdTable):
        for i in categoProdTable.get_children():
            categoProdTable.delete(i)

        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()

        operacion.execute("SELECT codigoProd, nombre FROM product WHERE categoria = 'Abarrotes'")
        for codigoProd, nombre in operacion.fetchall():
            categoProdTable.insert('','end', text = codigoProd, values = (nombre,'-','-','-'))

        operacion.execute("SELECT codigoProd, nombre FROM product WHERE categoria = 'Botanas'")
        for codigoProd, nombre in operacion.fetchall():
            categoProdTable.insert('','end', text = codigoProd, values = ("-",nombre,'-','-'))

        operacion.execute("SELECT codigoProd, nombre FROM product WHERE categoria = 'Cerveza'")
        for codigoProd, nombre in operacion.fetchall():
            categoProdTable.insert('','end', text = codigoProd, values = ("-","-",nombre,'-'))

        operacion.execute("SELECT codigoProd, nombre FROM product WHERE categoria = 'Refrescos'")
        for codigoProd, nombre in operacion.fetchall():
            categoProdTable.insert('','end', text = codigoProd, values = ("-","-",'-',nombre))

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

    """def verificaReo(codigo):
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
        conexion.close()"""

    def verificaEmpleado(idEmp):
        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        operacion.execute("SELECT id FROM employee WHERE  id = %s",(idEmp,))
        x = operacion.fetchone()
        if x == None:
            return FALSE
        conexion.close()

    def verificaProv(idP):
        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        operacion.execute("SELECT claveProv FROM supplier WHERE claveProv = %s",(idP,))
        x = operacion.fetchone()
        if x == None:
            return FALSE
        conexion.close()

    def verificaProd(codigo):
        conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='registration' )
        operacion = conexion.cursor()
        operacion.execute("SELECT codigoProd FROM product WHERE codigoProd = %s",(codigo,))
        x = operacion.fetchone()
        if x == None:
            return FALSE
        conexion.close()

    def verificaCarrito(codigoProd):
        for x in range(len(carrito)):
            if carrito[x].get('codigoProd') == codigoProd:
                return (True, x)
        return (False, 0) 


    def modEmp(aidiEmpMod, nombreEmpMod, apPatEmpMod, apMatEmpMod, rfcEmpMod, fechaNacEmpMod, 
    fechaIngresoEmpMod, ciudadEmpMod, estadoEmpMod, paisEmpMod, calleEmpMod, coloniaEmpMod,
    cpEmpMod, telEmpMod, sueldoEmpMod):
        while TRUE:
            try:
                fechaNacEmpStr = fechaNacEmpMod.get_date().strftime('%Y-%m-%d')
                fechaIngresoEmpStr = fechaIngresoEmp.get_date().strftime('%Y-%m-%d')
                connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')  
                operacion = connection.cursor()
                operacion.execute("UPDATE employee SET nombreEmp = %s, apPatEmp = %s, apMatEmp = %s,"+
                "rfcEmp = %s, fechaNacEmp = %s,fechaIngEmp = %s, ciudadEMp = %s, estadoEmp = %s,"+
                "paisEmp = %s, calleEmp = %s, coloniaEmp = %s, cpEmp = %s, telEmp = %s,"+
                "sueldoEmp = %s WHERE id = %s", (nombreEmpMod.get(), apPatEmpMod.get(), apMatEmpMod.get(), 
                rfcEmpMod.get(), fechaNacEmpStr, fechaIngresoEmpStr, ciudadEmpMod.get(), 
                estadoEmpMod.get(),paisEmpMod.get(),calleEmpMod.get(), coloniaEmpMod.get(),cpEmpMod.get(), 
                telEmpMod.get(),sueldoEmpMod.get(), aidiEmpMod.get()))

                x = verificaEmpleado(aidiEmpMod.get())
                if(x == FALSE):
                    mBox.showerror("ERROR", "El empleado que ingresaste no existe.")
                    break

                connection.commit()
                mBox.showinfo("MODIFICACION","El empleado " + str(aidiEmpMod.get()) + " ha sido modificado satisfactoriamente.")
                connection.close()
                aidiEmpMod.delete(0, END), nombreEmpMod.delete(0, END), apPatEmpMod.delete(0, END), 
                apMatEmpMod.delete(0, END), rfcEmpMod.delete(0, END), fechaNacEmpMod.delete(0, END), 
                fechaIngresoEmpMod.delete(0, END), ciudadEmpMod.delete(0, END), estadoEmpMod.delete(0, END),
                paisEmpMod.delete(0, END), calleEmpMod.delete(0, END), coloniaEmpMod.delete(0, END),
                cpEmpMod.delete(0, END), telEmpMod.delete(0, END), sueldoEmpMod.delete(0, END)
                break
                
            except Exception as e:
                mBox.showerror("ERROR", "Empleado no modificado, verifica tus datos.")
                print(e)
                break


    def modProv(claveProvMod, nombreProdMod, apPatProvMod, apMatProvMod,
    rfcProvMod, telProvMod, empresaProvMod, ciudadProvMod, calleProvMod, coloniaProvMod, cpProvMod):
        while TRUE:
            try:
                connection = mysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='registration')  
                operacion = connection.cursor()  
                operacion.execute("UPDATE supplier SET nombreProv = %s, apPatProv = %s, apMatProv = %s," + 
                "rfcProv = %s, telefonoProv = %s, empresaProv = %s, ciudadProv = %s,"+
                "calleProv = %s, coloniaProv = %s, cpProv = %s WHERE claveProv = %s",(nombreProvMod.get(), 
                apPatProvMod.get(), apMatProvMod.get(), rfcProvMod.get(), telProvMod.get(), empresaProvMod.get(), 
                ciudadProvMod.get(), calleProvMod.get(), coloniaProvMod.get(), cpProvMod.get(), claveProvMod.get()))

                x = verificaProv(claveProvMod.get())
                if(x == FALSE):
                    mBox.showerror("ERROR", "El proveedor que ingresaste no existe.")
                    break

                connection.commit()
                mBox.showinfo("MODIFICACION", "El proveedor " + str(claveProvMod.get()) + " ha sido "+
                "modificado satisfactoriamente.")
                connection.close()

                claveProvMod.delete(0, END), nombreProvMod.delete(0, END), apPatProvMod.delete(0, END),
                apMatProvMod.delete(0, END), rfcProvMod.delete(0, END), telProvMod.delete(0, END),
                empresaProvMod.delete(0, END), ciudadProvMod.delete(0, END), calleProvMod.delete(0, END),
                coloniaProvMod.delete(0, END), cpProvMod.delete(0, END)
                break

            except Exception as e:
                mBox.showerror("ERROR", "Proveedor no modificado, verifica tus datos.")
                print(e)
                break

    def modProd(codigoProdMod, nombreProdMod, marcaProdMod, existProdMod,
    costoProdMod, precioventaProdMod, reordenProdMod, proveedorProdMod, categProdMod):
        while TRUE:
            try:
                connection = mysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            database='registration')  
                operacion = connection.cursor() 
                operacion.execute("UPDATE product SET nombre = %s, marca = %s, existencia = %s," + 
                "costo = %s, precioventaProd = %s, reordenProd = %s, proveedor = %s," + 
                "categoria = %s WHERE codigoProd = %s", (nombreProdMod.get(), marcaProdMod.get(), 
                existProdMod.get(), costoProdMod.get(), precioventaProdMod.get(), reordenProdMod.get(),
                proveedorProdMod.get(), categProdMod, codigoProdMod.get())) 

                x = verificaProd(codigoProdMod.get())
                if(x == FALSE):
                    mBox.showerror("ERROR", "El producto que ingresaste no existe.")
                    break

                y = verificaProv(proveedorProdMod.get())
                if(y == FALSE):
                    mBox.showerror("ERROR", "El proveedor que ingresaste no existe.")
                    break

                connection.commit()
                mBox.showinfo("MODIFICACION", "El producto " + str(codigoProdMod.get()) + " ha"+
                " sido modificado satisfactoriamente." )
                connection.close()

                codigoProdMod.delete(0, END), nombreProdMod.delete(0, END), marcaProdMod.delete(0, END), 
                existProdMod.delete(0, END), costoProdMod.delete(0, END), precioventaProdMod.delete(0, END), 
                reordenProdMod.delete(0, END), proveedorProdMod.delete(0, END)
                break

                """fINSERT INTO product VALUES ({codigoProd.get()}, 
                '{nombreProd.get()}', '{marcaProd.get()}', '{existProd.get()}',
                '{costoProd.get()}',{precioVProd.get()} ,'{reordenProd.get()}',
                '{provedorProd.get()}', '{categProd}')"""

            except Exception as e:
                mBox.showerror("ERROR", "Producto no modificado, verifica sus datos.")
                print(e)
                break

    def eliEmp(aidiEmpMod):
        try:
            idEmp = int(aidiEmpMod.get())
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')  
            operacion = connection.cursor() 
            operacion.execute("DELETE FROM employee WHERE id = %s",(idEmp,)) 

            connection.commit()
            mBox.showinfo("ELIMINACION", "El empleado " + str(idEmp) + " ha"+
            " sido eliminado satisfactoriamente." )
            connection.close()

            aidiEmpMod.delete(0, END), nombreEmpMod.delete(0, END), apPatEmpMod.delete(0, END), 
            apMatEmpMod.delete(0, END), rfcEmpMod.delete(0, END), fechaNacEmpMod.delete(0, END), 
            fechaIngresoEmpMod.delete(0, END), ciudadEmpMod.delete(0, END), estadoEmpMod.delete(0, END),
            paisEmpMod.delete(0, END), calleEmpMod.delete(0, END), coloniaEmpMod.delete(0, END),
            cpEmpMod.delete(0, END), telEmpMod.delete(0, END), sueldoEmpMod.delete(0, END)

        except Exception as e:
            mBox.showerror("ERROR", "Empleado no eliminado, verifica tus datos")
    
    def eliProv(claveProv):
        try:
            idProv = int(claveProv.get())
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')  
            operacion = connection.cursor() 
            operacion.execute("DELETE FROM supplier WHERE claveProv = %s",(idProv,)) 

            connection.commit()
            mBox.showinfo("ELIMINACION", "El proveedor " + str(idProv) + " ha"+
            " sido eliminado satisfactoriamente." )
            connection.close()

            claveProvMod.delete(0, END), nombreProvMod.delete(0, END), apPatProvMod.delete(0, END),
            apMatProvMod.delete(0, END), rfcProvMod.delete(0, END), telProvMod.delete(0, END),
            empresaProvMod.delete(0, END), ciudadProvMod.delete(0, END), calleProvMod.delete(0, END),
            coloniaProvMod.delete(0, END), cpProvMod.delete(0, END)

        except Exception as e:
            mBox.showerror("ERROR", "Proveedor no eliminado, verifica tus datos")


    def eliProd(codigoProdMod):
        try:
            idProd = int(codigoProdMod.get())
            connection = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        database='registration')  
            operacion = connection.cursor() 
            operacion.execute("DELETE FROM product WHERE codigoProd = %s",(idProd,)) 

            connection.commit()
            mBox.showinfo("ELIMINACION", "El producto " + str(idProd) + " ha"+
            " sido eliminado satisfactoriamente." )
            connection.close()

            codigoProdMod.delete(0, END), nombreProdMod.delete(0, END), marcaProdMod.delete(0, END), 
            existProdMod.delete(0, END), costoProdMod.delete(0, END), precioventaProdMod.delete(0, END), 
            reordenProdMod.delete(0, END), proveedorProdMod.delete(0, END), comboTwoMod.current(0)

        except Exception as e:
            mBox.showerror("ERROR", "Producto no eliminado, verifica tus datos")

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

    options= tk.Frame(window, bg="#7a6756")
    options.grid(row=0,column=0, sticky='NSWE')
    options.columnconfigure(0, weight=1)

    display = tk.Frame(window, bg="blue")
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

    manageEmployeeImg = PhotoImage(file = "manageEmployee.png")
    manageEmployeeImg = manageEmployeeImg.zoom(2)
    manageEmployeeImg = manageEmployeeImg.subsample(6)

    manageSupplierImg = PhotoImage(file = "manageSupplier.png")
    manageSupplierImg = manageSupplierImg.zoom(2)
    manageSupplierImg = manageSupplierImg.subsample(6)

    manageProductImg = PhotoImage(file = "manageProduct.png")
    manageProductImg = manageProductImg.zoom(2)
    manageProductImg = manageProductImg.subsample(6)

    #*************************************** LABELS ****************************************
    interface_agregar= []

    for x in range(16):
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
    relief=tk.FLAT, command = lambda: regEmp(aidi, nombreEmp, apPatEmp, 
    apMatEmp, rfcEmp, fechaNacEmp, fechaIngresoEmp, ciudadEmp, estadoEmp, 
    paisEmp, calleEmp, coloniaEmp, cpEmp, telEmp, sueldoEmp))
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
    ttk.Label(interface_agregar[2], text="Apellido Paterno:",font=("Fixedsys", 9), background='white').grid(row=8, column=1,pady=5)
    ttk.Label(interface_agregar[2], text="Apellido Materno:",font=("Fixedsys", 9), background='white').grid(row=10, column=1,pady=5)
    ttk.Label(interface_agregar[2], text="RFC:",font=("Fixedsys", 9), background='white').grid(row=12, column=1,pady=5)
    ttk.Label(interface_agregar[2], text ="Telefono:", font=("Fixedsys", 9), background = 'white').grid(row=14,column = 1,pady=5)
    ttk.Label(interface_agregar[2], text="Nombre Empresa:",font=("Fixedsys", 9), background='white').grid(row=16, column=1,pady=5)
    ttk.Label(interface_agregar[2], text="Ciudad:",font=("Fixedsys", 9), background='white').grid(row=18, column=1,pady=5)
    ttk.Label(interface_agregar[2], text="Calle:",font=("Fixedsys", 9), background='white').grid(row=20, column=1,pady=5)
    ttk.Label(interface_agregar[2], text="Colonia:",font=("Fixedsys", 9), background='white').grid(row=22, column=1,pady=5)
    ttk.Label(interface_agregar[2], text="CP:",font=("Fixedsys", 9), background='white').grid(row=24, column=1,pady=5)

    claveProv = ttk.Entry(interface_agregar[2], width = 15)
    claveProv.grid(row = 4, column = 2,pady=5)

    nombreProv = ttk.Entry(interface_agregar[2], width = 15)
    nombreProv.grid(row = 6, column = 2,pady=5)

    apPatProv = ttk.Entry(interface_agregar[2], width = 15)
    apPatProv.grid(row = 8, column = 2, pady = 5)

    apMatProv = ttk.Entry(interface_agregar[2], width = 15)
    apMatProv.grid(row = 10, column = 2, pady = 5)

    rfcProv = ttk.Entry(interface_agregar[2], width = 15)
    rfcProv.grid(row = 12, column = 2,pady=5)

    telProv = ttk.Entry(interface_agregar[2], width = 15)
    telProv.grid(row = 14, column = 2,pady=5)

    empresaProv = ttk.Entry(interface_agregar[2], width = 15)
    empresaProv.grid(row = 16, column = 2,pady=5)

    ciudadProv = ttk.Entry(interface_agregar[2], width = 15)
    ciudadProv.grid(row = 18, column = 2,pady=5)

    calleProv = ttk.Entry(interface_agregar[2], width = 15)
    calleProv.grid(row = 20, column = 2,pady=5)

    coloniaProv = ttk.Entry(interface_agregar[2], width = 15)
    coloniaProv.grid(row = 22, column = 2,pady=5)

    cpProv = ttk.Entry(interface_agregar[2], width = 15)
    cpProv.grid(row = 24, column = 2,pady=5)

    submitProv=tk.Button(interface_agregar[2], text="Registrar", background='#0781F4', fg='white',
    relief=tk.FLAT, command = lambda: regProv(claveProv, nombreProv,apPatProv,apMatProv, rfcProv, 
    telProv,empresaProv,ciudadProv, calleProv, coloniaProv, cpProv))
    submitProv.grid(row=26, column=2,pady=5)
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
    ttk.Label(interface_agregar[3], text="Precio Venta:",font=("Fixedsys", 9), background='white').grid(row=12, column=1, pady=5)
    ttk.Label(interface_agregar[3], text ="Punto de Reorden:",font=("Fixedsys", 9), background='white').grid(row = 14,column=1, pady=5)
    ttk.Label(interface_agregar[3], text="Proveedor:",font=("Fixedsys", 9), background='white').grid(row=16, column=1, pady=5)
    ttk.Label(interface_agregar[3], text="Categoria:",font=("Fixedsys", 9), background='white').grid(row=18, column=1, pady=5)

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

    precioventaProd = ttk.Entry(interface_agregar[3], width = 30)
    precioventaProd.grid(row = 12, column = 2, pady=5)

    reordenProd = ttk.Entry(interface_agregar[3], width = 30)
    reordenProd.grid(row = 14, column = 2, pady=5)

    provedorProd = ttk.Entry(interface_agregar[3], width = 30)
    provedorProd.grid(row = 16, column = 2, pady = 5)

    categProd = tk.StringVar()
    comboTwo = ttk.Combobox(interface_agregar[3], width = 28, textvariable = categProd,
    state = "readonly", justify='center')
    comboTwo['values'] = ("Refrescos", "Cerveza", "Botanas", "Abarrotes")
    comboTwo.current(0)
    comboTwo.grid(row = 18, column = 2, pady = 5)


    submitProd=tk.Button(interface_agregar[3], text="Ingresar", background='#FF8F00', fg='white',
    relief=tk.FLAT, command = lambda: regProd(codigoProd, nombreProd, marcaProd, 
    existProd, costoProd, precioventaProd, reordenProd, provedorProd, categProd.get()))
    submitProd.grid(row=20, column=2, pady=5)
    #**************************************************************************

    #**************************************** INGRESAR ****************************************
    #Option -> Agregar
    agregar_frames= []

    for x in range(16):
        agregar_frames.append(tk.Frame(options))


    title = tk.Frame(options, bg = '#005ea5')
    title.grid(row=0, column=0, sticky='NWSE', pady=8)
    labelTitle = ttk.Label(title, text = '      TIENDA DE \n    CONVENIENCIA', width = 20, background = '#e9d5c4')
    labelTitle.pack(side = tk.TOP, anchor = 'center')
    labelTitle.config(font=("Courier", 20))
    labelTitle.bind("<Button-1>", lambda x: OnClick(0))

    agregar_frames[0]=tk.Frame(options)
    agregar_frames[0].grid(row=1,column=0,sticky='NWSE', pady=2)
    agregar=ttk.Label(agregar_frames[0], text="AGREGAR", anchor=tk.CENTER, background='#a8684c', foreground='#FFFFFF')
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

    show = ttk.Label(options, text="MOSTRAR", anchor=tk.CENTER, background='#a8684c', foreground='#FFFFFF')
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

    ttk.Label(interface_agregar[4], text="LISTA DE EMPLEADOS", 
    font=("Times", 20), background='white', anchor='center').grid(row=0, column=0, columnspan=4, sticky='NEWS')

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

    ttk.Label(interface_agregar[5], text="LISTA DE PROVEEDORES", 
    font=("Times", 20), background='white', anchor='center').grid(row=0, column=0, columnspan=4, sticky='NEWS')

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

    ttk.Label(interface_agregar[6], text=" LISTA DE PRODUCTOS", 
    font=("Times", 20), background='white', anchor='center').grid(row=0, column=1, columnspan= 4,sticky='NEWS')

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
    interface_agregar[7].rowconfigure(1, weight=1)
    interface_agregar[7].rowconfigure(2, weight=1)
    interface_agregar[7].rowconfigure(3, weight=1)
    interface_agregar[7].columnconfigure(0, weight=1)
    interface_agregar[7].columnconfigure(1, weight=1)
    interface_agregar[7].columnconfigure(2, weight=1)
    interface_agregar[7].columnconfigure(3, weight=1)
    interface_agregar[7].columnconfigure(4, weight=1)

    interface_agregar[7].pack_forget()

    ttk.Label(interface_agregar[7], text="LISTA DE VENTAS", 
    font=("Times", 20), background='white', anchor='center').grid(row=0, column=0, columnspan=6,sticky='NESW')

    agregar_frames[7]=tk.Frame(options, bg = '#080808')
    agregar_frames[7].grid(row=9,column=0,sticky='NWSE', pady=2, padx=10)
    supplierShow=ttk.Label(agregar_frames[7], text="VENTAS", anchor=tk.CENTER, background='#E0E0E0')
    supplierShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    supplierShow.bind("<Button-1>", lambda x: OnClick(7))
    supplierShow.bind("<Enter>", LabelEnter)
    supplierShow.bind("<Leave>", LabelLeave)

    ttk.Label(interface_agregar[7], text="Fecha:", font=("Fixedsys", 9), background='white').grid(row=2, column=0, pady=2, padx=10, sticky='e')

    saleDate = MyDateEntry(interface_agregar[7],
                    width=10,
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
                    
    saleDate.grid(row = 2, column = 1, pady=2, sticky='w') 
    #*******************************************************************
    interface_agregar[8].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[8].configure(bg='white')
    interface_agregar[8].rowconfigure(0, weight=1)
    interface_agregar[8].rowconfigure(2, weight=1)
    interface_agregar[8].rowconfigure(3, weight=1)
    interface_agregar[8].columnconfigure(0, weight=1)
    interface_agregar[8].columnconfigure(1, weight=2)
    interface_agregar[8].columnconfigure(2, weight=2)
    interface_agregar[8].columnconfigure(3, weight=2)
    interface_agregar[8].pack_forget()

    ttk.Label(interface_agregar[8], text="      \tLISTA DE CONCEPTOS DE VENTA   ", 
    font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

    agregar_frames[8]=tk.Frame(options, bg = '#080808')
    agregar_frames[8].grid(row=10,column=0,sticky='NWSE', pady=2, padx=10)
    supplierShow=ttk.Label(agregar_frames[8], text="CONCEPTO", anchor=tk.CENTER, background='#E0E0E0')
    supplierShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    supplierShow.bind("<Button-1>", lambda x: OnClick(8))
    supplierShow.bind("<Enter>", LabelEnter)
    supplierShow.bind("<Leave>", LabelLeave)
    #************************************************************************
    interface_agregar[9].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[9].configure(bg='white')
    interface_agregar[9].pack_forget()

    ttk.Label(interface_agregar[9], text="   PRODUCTOS A ORDENAR     ", 
    font=("Times", 20), background='white').grid(row=0, column=1)

    agregar_frames[9]=tk.Frame(options, bg = '#080808')
    agregar_frames[9].grid(row=11,column=0,sticky='NWSE', pady=2, padx=10)
    prodOrdShow=ttk.Label(agregar_frames[9], text="PRODUCTOS A ORDENAR", anchor=tk.CENTER, background='#E0E0E0')
    prodOrdShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    prodOrdShow.bind("<Button-1>", lambda x: OnClick(9))
    prodOrdShow.bind("<Enter>", LabelEnter)
    prodOrdShow.bind("<Leave>", LabelLeave)


    #************************************ ELIMINAR/MODIFICAR *****************************
    modif = ttk.Label(options, text="MODIFICAR Ó ELIMINAR", anchor=tk.CENTER, background='#a8684c', foreground='#FFFFFF')
    modif.grid(row=12, column=0, sticky='NWSE', pady=5)

    #***************************************************************************************
    interface_agregar[10].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[10].configure(bg='white')
    interface_agregar[10].pack_forget()

    agregar_frames[10]=tk.Frame(options, bg = '#080808')
    agregar_frames[10].grid(row=13,column=0,sticky='NWSE', pady=2, padx=10)
    empModShow=ttk.Label(agregar_frames[10], text="EMPLEADOS", anchor=tk.CENTER, background='#E0E0E0')
    empModShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    empModShow.bind("<Button-1>", lambda x: OnClick(10))
    empModShow.bind("<Enter>", LabelEnter)
    empModShow.bind("<Leave>", LabelLeave)

    ttk.Label(interface_agregar[10], text="MODIFICAR O ELIMINAR EMPLEADO", 
    font=("Times", 20), background='white').grid(row=0, column=2)

    LabelEmployeeMod = tk.Label(interface_agregar[10], background = 'white', image = manageEmployeeImg)
    LabelEmployeeMod.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

    ttk.Label(interface_agregar[10], text="ID:", font=("Fixedsys", 9), background='white').grid(row=2, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Nombre:", font=("Fixedsys", 9),  background='white').grid(row=4, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Apellido Paterno:", font=("Fixedsys", 9),  background='white').grid(row=6, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Apellido Materno:", font=("Fixedsys", 9),  background='white').grid(row=8, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="RFC:", font=("Fixedsys", 9),  background='white').grid(row=10, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Fecha Nacimiento:", font=("Fixedsys", 9),  background='white').grid(row=12, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Fecha Ingreso:", font=("Fixedsys", 9),  background='white').grid(row=14, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Ciudad:", font=("Fixedsys", 9),  background='white').grid(row=16, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Estado:", font=("Fixedsys", 9),  background='white').grid(row=18, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="País:", font=("Fixedsys", 9),  background='white').grid(row=20, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Calle:", font=("Fixedsys", 9),  background='white').grid(row=22, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Colonia:", font=("Fixedsys", 9),  background='white').grid(row=24, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="CP:", font=("Fixedsys", 9),  background='white').grid(row=26, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Teléfono:", font=("Fixedsys", 9),  background='white').grid(row=28, column=1, pady=2)
    ttk.Label(interface_agregar[10], text="Sueldo:", font=("Fixedsys", 9),  background='white').grid(row=30, column=1, pady=2)


    aidiEmpMod = ttk.Entry(interface_agregar[10], width=30)
    aidiEmpMod.grid(row=2, column=2, pady=2)
    aidiEmpMod.bind('<Return>',  llenarDatosEmp)

    nombreEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    nombreEmpMod.grid(row = 4, column = 2, pady=2)

    apPatEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    apPatEmpMod.grid(row = 6, column = 2)

    apMatEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    apMatEmpMod.grid(row = 8, column = 2)

    rfcEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    rfcEmpMod.grid(row = 10, column = 2, pady=2)

    fechaNacEmpMod = MyDateEntry(interface_agregar[10],
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
                    
    fechaNacEmpMod.grid(row = 12, column = 2, pady=2) 

    fechaIngresoEmpMod = MyDateEntry(interface_agregar[10],
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

    fechaIngresoEmpMod.grid(row = 14, column = 2, pady=2)

    ciudadEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    ciudadEmpMod.grid(row = 16, column = 2, pady=2)

    estadoEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    estadoEmpMod.grid(row = 18, column = 2, pady=2)

    paisEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    paisEmpMod.grid(row = 20, column = 2, pady=2)

    calleEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    calleEmpMod.grid(row = 22, column = 2, pady=2)

    coloniaEmpMod = ttk.Entry(interface_agregar[10], width = 30)    
    coloniaEmpMod.grid(row = 24, column = 2, pady=2)

    cpEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    cpEmpMod.grid(row = 26, column = 2, pady=2)

    telEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    telEmpMod.grid(row = 28, column = 2, pady=2)

    sueldoEmpMod = ttk.Entry(interface_agregar[10], width = 30)
    sueldoEmpMod.grid(row = 30, column = 2, pady=2)

    submitEmpMod=tk.Button(interface_agregar[10], text="Modificar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: modEmp(aidiEmpMod, nombreEmpMod, apPatEmpMod, apMatEmpMod, rfcEmpMod,
    fechaNacEmpMod, fechaIngresoEmpMod, ciudadEmpMod, estadoEmpMod, paisEmpMod, calleEmpMod, coloniaEmpMod,
    cpEmpMod, telEmpMod, sueldoEmpMod))
    submitEmpMod.grid(row=34, column=2, pady=2)

    submitEmpEli=tk.Button(interface_agregar[10], text="Eliminar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: eliEmp(aidiEmpMod))
    submitEmpEli.grid(row=35, column=2, pady=2)

    #***************************************************************************************

    interface_agregar[11].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[11].configure(bg='white')
    interface_agregar[11].pack_forget()

    ttk.Label(interface_agregar[11], text="      MODIFICAR PROVEEDORES     ",
    font=("Times", 20), background='white').grid(row=0, column=2, sticky='NEWS')

    agregar_frames[11]=tk.Frame(options, bg = '#080808')
    agregar_frames[11].grid(row=14,column=0,sticky='NWSE', pady=2, padx=10)
    provModShow=ttk.Label(agregar_frames[11], text="PROVEEDORES", anchor=tk.CENTER, background='#E0E0E0')
    provModShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    provModShow.bind("<Button-1>", lambda x: OnClick(11))
    provModShow.bind("<Enter>", LabelEnter)
    provModShow.bind("<Leave>", LabelLeave)

    labelSupplierMod = tk.Label(interface_agregar[11], background = 'white', image = manageSupplierImg)
    labelSupplierMod.grid(row = 10, column = 4, columnspan = 2, rowspan = 12)

    ttk.Label(interface_agregar[11], text="Clave:",font=("Fixedsys", 9), background='white').grid(row=4, column=1, pady=5)
    ttk.Label(interface_agregar[11], text="Nombre:",font=("Fixedsys", 9), background='white').grid(row=6, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="Apellido Paterno:",font=("Fixedsys", 9), background='white').grid(row=8, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="Apellido Materno:",font=("Fixedsys", 9), background='white').grid(row=10, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="RFC:",font=("Fixedsys", 9), background='white').grid(row=12, column=1,pady=5)
    ttk.Label(interface_agregar[11], text ="Telefono:", font=("Fixedsys", 9), background = 'white').grid(row=14,column = 1,pady=5)
    ttk.Label(interface_agregar[11], text="Nombre Empresa:",font=("Fixedsys", 9), background='white').grid(row=16, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="Ciudad:",font=("Fixedsys", 9), background='white').grid(row=18, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="Calle:",font=("Fixedsys", 9), background='white').grid(row=20, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="Colonia:",font=("Fixedsys", 9), background='white').grid(row=22, column=1,pady=5)
    ttk.Label(interface_agregar[11], text="CP:",font=("Fixedsys", 9), background='white').grid(row=24, column=1,pady=5)

    claveProvMod = ttk.Entry(interface_agregar[11], width = 30)
    claveProvMod.grid(row = 4, column = 2, columnspan=2, pady=5)
    claveProvMod.bind('<Return>',  llenarDatosProv)

    nombreProvMod = ttk.Entry(interface_agregar[11], width = 30)
    nombreProvMod.grid(row = 6, column = 2,columnspan=2, pady=5)

    apPatProvMod = ttk.Entry(interface_agregar[11], width = 30)
    apPatProvMod.grid(row = 8, column = 2,columnspan=2,  pady = 5)

    apMatProvMod = ttk.Entry(interface_agregar[11], width = 30)
    apMatProvMod.grid(row = 10, column = 2,columnspan=2,  pady = 5)

    rfcProvMod = ttk.Entry(interface_agregar[11], width = 30)
    rfcProvMod.grid(row = 12, column = 2,columnspan=2, pady=5)

    telProvMod = ttk.Entry(interface_agregar[11], width = 30)
    telProvMod.grid(row = 14, column = 2,columnspan=2, pady=5)

    empresaProvMod = ttk.Entry(interface_agregar[11], width = 30)
    empresaProvMod.grid(row = 16, column = 2,columnspan=2, pady=5)

    ciudadProvMod = ttk.Entry(interface_agregar[11], width = 30)
    ciudadProvMod.grid(row = 18, column = 2,columnspan=2, pady=5)

    calleProvMod = ttk.Entry(interface_agregar[11], width = 30)
    calleProvMod.grid(row = 20, column = 2,columnspan=2, pady=5)

    coloniaProvMod = ttk.Entry(interface_agregar[11], width = 30)
    coloniaProvMod.grid(row = 22, column = 2,columnspan=2, pady=5)

    cpProvMod = ttk.Entry(interface_agregar[11], width = 30)
    cpProvMod.grid(row = 24, column = 2, columnspan=2, pady=5)

    submitProvMod=tk.Button(interface_agregar[11], text="Modificar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: modProv(claveProvMod, nombreProdMod, apPatProvMod, apMatProvMod,
    rfcProvMod, telProvMod, empresaProvMod, ciudadProvMod, calleProvMod, coloniaProvMod, cpProvMod))
    submitProvMod.grid(row=26, column=2, pady=2)

    submitProvEli=tk.Button(interface_agregar[11], text="Eliminar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: eliProv(claveProvMod))
    submitProvEli.grid(row=27, column=2, pady=2)
    #**************************************************************************

    interface_agregar[12].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[12].configure(bg='white')
    interface_agregar[12].pack_forget()

    agregar_frames[12]=tk.Frame(options, bg = '#080808')
    agregar_frames[12].grid(row=15,column=0,sticky='NWSE', pady=2, padx=10)
    prodModShow=ttk.Label(agregar_frames[12], text="PRODUCTOS", anchor=tk.CENTER, background='#E0E0E0')
    prodModShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    prodModShow.bind("<Button-1>", lambda x: OnClick(12))
    prodModShow.bind("<Enter>", LabelEnter)
    prodModShow.bind("<Leave>", LabelLeave)

    labelBoxMod = tk.Label(interface_agregar[12], background = 'white', image = manageProductImg)
    labelBoxMod.grid(row = 4, column = 4, columnspan = 2, rowspan = 12)

    ttk.Label(interface_agregar[12], text="   MODIFICAR PRODUCTOS     ", 
    font=("Times", 20), background='white').grid(row=0, column=2)
    ttk.Label(interface_agregar[12], text="Código de barras:",font=("Fixedsys", 9), background='white').grid(row=2, column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Nombre:",font=("Fixedsys", 9), background='white').grid(row=4, column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Marca:",font=("Fixedsys", 9), background='white').grid(row=6, column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Existencia:",font=("Fixedsys", 9), background='white').grid(row=8, column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Costo:",font=("Fixedsys", 9), background='white').grid(row=10, column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Precio Venta:",font=("Fixedsys", 9), background='white').grid(row=12, column=1, pady=5)
    ttk.Label(interface_agregar[12], text ="Punto de Reorden:",font=("Fixedsys", 9), background='white').grid(row = 14,column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Proveedor:",font=("Fixedsys", 9), background='white').grid(row=16, column=1, pady=5)
    ttk.Label(interface_agregar[12], text="Categoria:",font=("Fixedsys", 9), background='white').grid(row=18, column=1, pady=5)

    codigoProdMod = ttk.Entry(interface_agregar[12], width = 30)
    codigoProdMod.grid(row = 2, column = 2, pady=5)
    codigoProdMod.bind('<Return>', llenarDatosProd)

    nombreProdMod = ttk.Entry(interface_agregar[12], width = 30)
    nombreProdMod.grid(row = 4, column = 2, pady=5)

    marcaProdMod = ttk.Entry(interface_agregar[12], width = 30)
    marcaProdMod.grid(row = 6, column = 2, pady=5)

    existProdMod = ttk.Entry(interface_agregar[12], width = 30)
    existProdMod.grid(row = 8, column = 2, pady=5)

    costoProdMod = ttk.Entry(interface_agregar[12], width = 30)
    costoProdMod.grid(row = 10, column = 2, pady=5)

    precioventaProdMod = ttk.Entry(interface_agregar[12], width = 30)
    precioventaProdMod.grid(row = 12, column = 2, pady=5)

    reordenProdMod = ttk.Entry(interface_agregar[12], width = 30)
    reordenProdMod.grid(row = 14, column = 2, pady=5)

    proveedorProdMod = ttk.Entry(interface_agregar[12], width = 30)
    proveedorProdMod.grid(row = 16, column = 2, pady = 5)

    categProdMod = tk.StringVar()
    comboTwoMod = ttk.Combobox(interface_agregar[12], width = 28, textvariable = categProdMod,
    state = "readonly", justify='center')
    comboTwoMod['values'] = ("Refrescos", "Cerveza", "Botanas", "Abarrotes")
    comboTwoMod.current(0)
    comboTwoMod.grid(row = 18, column = 2, pady = 5)


    submitProdMod=tk.Button(interface_agregar[12], text="Modificar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: modProd(codigoProdMod, nombreProdMod, marcaProdMod, existProdMod,
    costoProdMod, precioventaProdMod, reordenProdMod, proveedorProdMod, categProdMod.get()))
    submitProdMod.grid(row=26, column=2, pady=2)


    submitProdEli=tk.Button(interface_agregar[12], text="Eliminar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: eliProd(codigoProdMod))
    submitProdEli.grid(row=27, column=2, pady=2)

    #*************************************CATEGORIAS*************************************
    categ = ttk.Label(options, text="CATEGORIAS", anchor=tk.CENTER, background='#a8684c', foreground='#FFFFFF')
    categ.grid(row=16, column=0, sticky='NWSE', pady=5)
    #**************************************************************************
    interface_agregar[13].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[13].configure(bg='white')
    interface_agregar[13].pack_forget()

    ttk.Label(interface_agregar[13], text="       \t FORMAS DE PAGO     ", 
    font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

    agregar_frames[13]=tk.Frame(options, bg = '#080808')
    agregar_frames[13].grid(row=17,column=0,sticky='NWSE', pady=2, padx=10)
    prodCatShow=ttk.Label(agregar_frames[13], text="FORMAS DE PAGO", anchor=tk.CENTER, background='#E0E0E0')
    prodCatShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    prodCatShow.bind("<Button-1>", lambda x: OnClick(13))
    prodCatShow.bind("<Enter>", LabelEnter)
    prodCatShow.bind("<Leave>", LabelLeave)
    #********************************************************************************
    interface_agregar[14].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[14].configure(bg='white')
    interface_agregar[14].pack_forget()

    ttk.Label(interface_agregar[14], text="\n CATEGORIAS DE PRODUCTOS \n", 
    font=("Times", 20), background='white').grid(row=0, column=1, sticky='NEWS')

    agregar_frames[14]=tk.Frame(options, bg = '#080808')
    agregar_frames[14].grid(row=18,column=0,sticky='NWSE', pady=2, padx=10)
    prodCatShow=ttk.Label(agregar_frames[14], text="PRODUCTOS", anchor=tk.CENTER, background='#E0E0E0')
    prodCatShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    prodCatShow.bind("<Button-1>", lambda x: OnClick(14))
    prodCatShow.bind("<Enter>", LabelEnter)
    prodCatShow.bind("<Leave>", LabelLeave)
    #**************************************** VENTAS ************************************
    interface_agregar[15].pack(side='bottom',fill=tk.BOTH, expand=True)
    interface_agregar[15].configure(bg='white')
    interface_agregar[15].pack_forget()

    sales = ttk.Label(options, text="VENTAS", anchor=tk.CENTER, background='#a8684c', foreground='#FFFFFF')
    sales.grid(row=19, column=0, sticky='NWSE', pady=5)

    agregar_frames[15]=tk.Frame(options, bg = '#080808')
    agregar_frames[15].grid(row=20,column=0,sticky='NWSE', pady=2, padx=10)
    salesShow=ttk.Label(agregar_frames[15], text="REGISTRAR VENTAS", anchor=tk.CENTER, background='#E0E0E0')
    salesShow.pack(side='right', fill='both', expand=1, padx=5, pady=1)
    salesShow.bind("<Button-1>", lambda x: OnClick(15))
    salesShow.bind("<Enter>", LabelEnter)
    salesShow.bind("<Leave>", LabelLeave)

    labelSale = tk.Label(interface_agregar[15], background = 'white', image = saleImg)
    labelSale.grid(row = 4, column = 4, columnspan = 2, rowspan = 12)

    ttk.Label(interface_agregar[15], text="\tREGISTRO DE VENTAS \n   ", 
    font=("Times", 20), background='white').grid(row=0, column=2)
    ttk.Label(interface_agregar[15], text="Clave venta:",font=("Fixedsys", 9), background='white').grid(row=2, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Código de barras producto:",font=("Fixedsys", 9), background='white').grid(row=4, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Cantidad:",font=("Fixedsys", 9), background='white').grid(row=6, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Precio unitario:",font=("Fixedsys", 9), background='white').grid(row=8, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Importe",font=("Fixedsys", 9), background='white').grid(row=10, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Fecha venta:",font=("Fixedsys", 9), background='white').grid(row=12, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Forma pago:",font=("Fixedsys", 9), background='white').grid(row=14, column=1, pady=5)
    ttk.Label(interface_agregar[15], text="Clave empleado:",font=("Fixedsys", 9), background='white').grid(row=16, column=1, pady=5)



    codigoVenta = ttk.Entry(interface_agregar[15], width = 30)
    codigoVenta.grid(row = 2, column = 2, pady=5)

    codigoProdVenta = ttk.Entry(interface_agregar[15], width = 30)
    codigoProdVenta.grid(row = 4, column = 2, pady=5)
    codigoProdVenta.bind('<FocusOut>', fprecioVenta)

    cantidadVenta = ttk.Entry(interface_agregar[15], width = 30)
    cantidadVenta.grid(row = 6, column = 2, pady=5)
    cantidadVenta.bind('<FocusOut>', fprecioVenta)


    precioUnitVenta = ttk.Label(interface_agregar[15], text="0", width=30, anchor='e')
    precioUnitVenta.grid(row = 8, column = 2, pady=5)


    importeVenta = ttk.Label(interface_agregar[15],  text="0", width=30, anchor='e')
    importeVenta.grid(row = 10, column = 2, pady=5)


    fechaVenta = MyDateEntry(interface_agregar[15],
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
    comboOne = ttk.Combobox(interface_agregar[15], width = 28, textvariable = pago_var,
    state = "readonly", justify='center')
    comboOne['values'] = ("Cheque", "Vale", "Tarjeta de Credito", "Tarjeta de Debito",
    "Pagaré", "Efectivo")
    comboOne.current(0)
    comboOne.grid(row = 14, column = 2,)

    codigoEmpVenta = ttk.Entry(interface_agregar[15], width = 30)
    codigoEmpVenta.grid(row = 16, column = 2, pady = 5)

    global carrito
    carrito=[]

    submitConcepto=tk.Button(interface_agregar[15], text='Agregar al carrito', background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: regConcepto(codigoProdVenta.get(),cantidadVenta.get(),
    precioUnitVenta.cget('text'), importeVenta.cget('text')))
    submitConcepto.grid(row=18, column = 2, pady = 5)

    submitVenta=tk.Button(interface_agregar[15], text="Ingresar", background='#2ECC71', fg='white',
    relief=tk.FLAT, command = lambda: regVenta_2(codigoVenta.get(), codigoProdVenta.get(), cantidadVenta.get(),
    precioUnitVenta.cget('text'), importeVenta.cget('text'), fechaVenta, pago_var.get(), codigoEmpVenta.get()))
    submitVenta.grid(row=20, column = 2, pady = 5)

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
    supplierTable['columns'] = ('Nombre','Apellido Paterno','Apellido Materno','RFC', 'Telefono', 
                                'Empresa', 'Ciudad', 'Calle', 'Colonia', 'CP')

    productTable = ttk.Treeview(interface_agregar[6], style="Custom.Treeview")
    productTable.grid(row=2, column=1,sticky='NEWS')
    productTable['columns'] = ('Nombre', 'Marca', 'Existencia', 'Costo', 'Precio Venta', 'Punto de Reorden',
    'Proveedor', 'Categoria')

    saleTable = ttk.Treeview(interface_agregar[7], style = "Custom.Treeview")
    saleTable.grid(row = 1, column = 0, columnspan=5, sticky = 'NEWS', padx=10)
    saleTable['columns'] = ('Importe Total', 'Fecha de Venta', 'Forma de Pago', 'Clave Empleado')

    transactionTable = ttk.Treeview(interface_agregar[8], style = "Custom.Treeview")
    transactionTable.grid(row = 2, column = 1, sticky = 'NEWS')
    transactionTable['columns'] = ('Codigo Producto' , 'Cantidad', 'Precio Unitario',
    'Importe')

    prodOrdTable = ttk.Treeview(interface_agregar[9], style = "Custom.Treeview")
    prodOrdTable.grid(row=2, column=1,sticky='NEWS')
    prodOrdTable['columns'] = ('Nombre', 'Marca', 'Existencia', 'Costo', 'Precio Venta', 'Punto de Reorden',
    'Proveedor', 'Categoria')

    categoPagoTable = ttk.Treeview(interface_agregar[13], style = "Custom.Treeview")
    categoPagoTable.grid(row = 2, column = 1, sticky = 'NEWS')
    categoPagoTable['columns'] = ("Cheque", "Vale", "Tarjeta de Credito", "Tarjeta de Debito",
    "Pagaré", "Efectivo")

    categoProdTable = ttk.Treeview(interface_agregar[14], style = "Custom.Treeview")
    categoProdTable.grid(row = 2, column = 1, sticky = 'NEWS')
    categoProdTable['columns'] = ('Abarrotes', 'Botanas', 'Cervezas', 'Refrescos')



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
    sale_yscrollb.grid(row = 1, column = 5, sticky = 'NS', padx=10)
    saleTable.configure(yscrollcommand = sale_yscrollb.set)

    transaction_yscrollb= ttk.Scrollbar(interface_agregar[8], orient="vertical", command=transactionTable.yview)
    transaction_yscrollb.grid(row=2, column=2, sticky='NS')
    transactionTable.configure(yscrollcommand=transaction_yscrollb.set)

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
        supplierTable.heading("Apellido Paterno", text='Apellido Paterno')
        supplierTable.column("Apellido Paterno", anchor="center",width=80) 
        supplierTable.heading("Apellido Materno", text='Apellido Materno')
        supplierTable.column("Apellido Materno", anchor="center",width=80)      
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
        productTable.heading("Precio Venta", text='Precio Venta')
        productTable.column("Precio Venta", anchor="center",width=80)    
        productTable.heading("Punto de Reorden", text = "Punto de Reorden")
        productTable.column("Punto de Reorden", anchor = "center", width = 80)
        productTable.heading("Proveedor", text='Proveedor')
        productTable.column("Proveedor", anchor="center",width=80)   
        productTable.heading("Categoria", text='Categoria')
        productTable.column("Categoria", anchor="center",width=80)   

    def tableProdOrd():
        prodOrdTable.heading("#0", text='Codigo Barras', anchor='center')
        prodOrdTable.column("#0", anchor="w",width=80)   
        prodOrdTable.heading("Nombre", text='Nombre')
        prodOrdTable.column("Nombre", anchor="center",width=80)   
        prodOrdTable.heading("Marca", text='Marca')
        prodOrdTable.column("Marca", anchor="center",width=80)  
        prodOrdTable.heading("Existencia", text='Existencia')
        prodOrdTable.column("Existencia", anchor="center",width=80)   
        prodOrdTable.heading("Costo", text='Costo')
        prodOrdTable.column("Costo", anchor="center",width=80)
        prodOrdTable.heading("Precio Venta", text='Precio Venta')
        prodOrdTable.column("Precio Venta", anchor="center",width=80)    
        prodOrdTable.heading("Punto de Reorden", text = "Punto de Reorden")
        prodOrdTable.column("Punto de Reorden", anchor = "center", width = 80)
        prodOrdTable.heading("Proveedor", text='Proveedor')
        prodOrdTable.column("Proveedor", anchor="center",width=80)   
        prodOrdTable.heading("Categoria", text='Categoria')
        prodOrdTable.column("Categoria", anchor="center",width=80)   

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
        saleTable.heading("#0", text='Clave de Venta')
        saleTable.column("#0", anchor='w',width=80)     
        saleTable.heading("Importe Total", text='Importe Total')
        saleTable.column("Importe Total", anchor="center",width=80)   
        saleTable.heading("Fecha de Venta", text='Fecha de Venta')
        saleTable.column("Fecha de Venta", anchor="center",width=80)   
        saleTable.heading("Forma de Pago", text='Forma de Pago')
        saleTable.column("Forma de Pago", anchor="center",width=80)
        saleTable.heading("Clave Empleado", text = "Clave Empleado")
        saleTable.column("Clave Empleado", anchor = "center", width = 80)

    def tableTransaction():
        transactionTable.heading("#0", text='Clave Venta', anchor='center')
        transactionTable.column("#0", anchor="w",width=80)   
        transactionTable.heading("Codigo Producto", text='Codigo Producto')
        transactionTable.column("Codigo Producto", anchor="center",width=80)   
        transactionTable.heading("Cantidad", text='Cantidad')
        transactionTable.column("Cantidad", anchor="center",width=80)  
        transactionTable.heading("Precio Unitario", text='Precio Unitario')
        transactionTable.column("Precio Unitario", anchor="center",width=80)   
        transactionTable.heading("Importe", text='Importe')
        transactionTable.column("Importe", anchor="center",width=80)   

    
    main()
    window.mainloop()

