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

options= tk.Frame(window)
options.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

display=tk.Frame(window)
display.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

interface_agregar= []

for x in range(4):
    interface_agregar.append(tk.Frame(display))

interface_agregar[0].pack(fill=tk.BOTH, expand=True)
interface_agregar[1].pack(fill=tk.BOTH, expand=True)
interface_agregar[2].pack(fill=tk.BOTH, expand=True)
interface_agregar[3].pack(fill=tk.BOTH, expand=True)

interface_agregar[0].configure(bg='black')
interface_agregar[0].pack_forget()

interface_agregar[1].configure(bg='red')
interface_agregar[1].pack_forget()

interface_agregar[2].configure(bg='blue')
interface_agregar[2].pack_forget()

interface_agregar[3].configure(bg='green')
interface_agregar[3].pack_forget()

#Treeview 1
tree_data = ttk.Treeview(options)
tree_data.pack(side=tk.TOP,fill=tk.BOTH, expand=True)

tree_data.insert('','0','add', text='Agregar')
tree_data.insert('add','0','empleado', text='Empleado')
tree_data.insert('add','1','proveedor', text='Proveedor')
tree_data.insert('add','2','producto', text='Producto')
tree_data.insert('add','3','venta', text='Venta')


tree_data.insert('','1','table', text='Tablas')
tree_data.insert('table','0','tabla1', text='Tabla 1')
tree_data.insert('table','1','tabla2', text='Tabla 2')
tree_data.insert('table','2','tabla3', text='Tabla 3')
tree_data.insert('table','3','tabla4', text='Tabla 4')
 

tree_data.bind("<Double-1>", OnDoubleClick)

main()