import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

window = tk.Tk()
window.title('Base de datos')
window.geometry('500x500')

options= tk.Frame(window)
options.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

display=tk.Frame(window)
display.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#Treeview 1
insert_data = ttk.Treeview(options)
insert_data.pack(side=tk.TOP,fill=tk.BOTH, expand=True)
insert_data.insert('','0','add', text='Agregar')
insert_data.insert('add','0','empleado', text='Empleado')
insert_data.insert('add','1','proveedor', text='Proveedor')
insert_data.insert('add','2','producto', text='Producto')
insert_data.insert('add','3','venta', text='Venta')


#Treeview 2
view_table = ttk.Treeview(options)
view_table.pack(side=tk.BOTTOM,fill=tk.BOTH, expand=True)
view_table.insert('','1','table', text='Tablas')
view_table.insert('table','0','tabla1', text='Tabla 1')
view_table.insert('table','1','tabla2', text='Tabla 2')
view_table.insert('table','2','tabla3', text='Tabla 3')
view_table.insert('table','3','tabla4', text='Tabla 4')



def main():
    window.mainloop()

main()