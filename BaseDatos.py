import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox


def main():
    window.mainloop()


def OnDoubleClick(event=None):
    item_id = event.widget.focus()
    #item = event.widget.item(item_id)
    if(item_id=="empleado"):
        ShowAgregar(0)
        interface_agregar1.pack(fill=tk.BOTH, expand=True)
    elif(item_id=="proveedor"):
        ShowAgregar(1)
        interface_agregar2.pack(fill=tk.BOTH, expand=True)
    elif(item_id=="producto"):
        ShowAgregar(2)
        interface_agregar3.pack(fill=tk.BOTH, expand=True)
    elif(item_id=="venta"):
        ShowAgregar(3)
        interface_agregar4.pack(fill=tk.BOTH, expand=True)
    else:
        return

def ShowAgregar(index):
        interface_agregar1.pack_forget()
        interface_agregar2.pack_forget()
        interface_agregar3.pack_forget()
        interface_agregar4.pack_forget()



window = tk.Tk()
window.title('Base de datos')
window.geometry('1080x600')

options= tk.Frame(window)
options.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

display=tk.Frame(window)
display.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

interface_agregar1= tk.Frame(display)
interface_agregar2= tk.Frame(display)
interface_agregar3= tk.Frame(display)
interface_agregar4= tk.Frame(display)
interface_agregar1.pack(fill=tk.BOTH, expand=True)
interface_agregar2.pack(fill=tk.BOTH, expand=True)
interface_agregar3.pack(fill=tk.BOTH, expand=True)
interface_agregar4.pack(fill=tk.BOTH, expand=True)

interface_agregar4.configure(bg='black')
interface_agregar4.pack_forget()

interface_agregar1.configure(bg='red')
interface_agregar1.pack_forget()

interface_agregar2.configure(bg='blue')
interface_agregar2.pack_forget()

interface_agregar3.configure(bg='green')
interface_agregar3.pack_forget()

#Treeview 1
insert_data = ttk.Treeview(options)
insert_data.pack(side=tk.TOP,fill=tk.BOTH, expand=True)
insert_data.insert('','0','add', text='Agregar')
insert_data.insert('add','0','empleado', text='Empleado')
insert_data.insert('add','1','proveedor', text='Proveedor')
insert_data.insert('add','2','producto', text='Producto')
insert_data.insert('add','3','venta', text='Venta')


#Treeview 2
table_view = ttk.Treeview(options)
table_view.pack(side=tk.BOTTOM,fill=tk.BOTH, expand=True)
table_view.insert('','1','table', text='Tablas')
table_view.insert('table','0','tabla1', text='Tabla 1')
table_view.insert('table','1','tabla2', text='Tabla 2')
table_view.insert('table','2','tabla3', text='Tabla 3')
table_view.insert('table','3','tabla4', text='Tabla 4')
 

insert_data.bind("<Double-1>", OnDoubleClick)

main()