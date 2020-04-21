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
    elif(item_id=="proveedor"):
        ShowAgregar(1)
    elif(item_id=="producto"):
        ShowAgregar(2)
    elif(item_id=="venta"):
        ShowAgregar(3)
    else:
        return

def ShowAgregar(index):
    x=0
    while(x<len(interface_agregar)):
        if x!=index:
            interface_agregar[x].pack_forget()
        x+=1
    interface_agregar[index].pack(fill=tk.BOTH, expand=True)



window = tk.Tk()
window.title('Base de datos')
window.geometry('1080x600')

options= tk.Frame(window, bg="#04517D")
options.pack(side=tk.LEFT, fill= tk.BOTH ,expand=1)


display=tk.Frame(window, bg="#c4dbe9")
display.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

interface_agregar= []

for x in range(4):
    interface_agregar.append(tk.Frame(display))


#Empleado
interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[0].configure(bg='black')
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

#Treeview 1
data_tree = ttk.Treeview(options)
data_tree.pack(side=tk.LEFT, fill=tk.Y)
data_tree.pack_configure(padx=10, pady=10)

data_tree.insert('','0','add', text='Agregar', tags = ('add',))
data_tree.insert('add','0','empleado', text='Empleado',tags = ('data',))
data_tree.insert('add','1','proveedor', text='Proveedor',tags = ('data',))
data_tree.insert('add','2','producto', text='Producto',tags = ('data',))
data_tree.insert('add','3','venta', text='Venta',tags = ('data',))


data_tree.insert('','1','table', text='Tablas', tags = ('table',))
data_tree.insert('table','0','tabla1', text='Tabla 1',tags = ('data',))
data_tree.insert('table','1','tabla2', text='Tabla 2',tags = ('data',))
data_tree.insert('table','2','tabla3', text='Tabla 3',tags = ('data',))
data_tree.insert('table','3','tabla4', text='Tabla 4',tags = ('data',))
 

data_tree.tag_configure('data', background='#E8E8E8')

data_tree.bind("<Double-1>", OnDoubleClick)

main()