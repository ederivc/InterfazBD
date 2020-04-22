import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

def main():
    window.mainloop()

window = tk.Tk()
window.title("BASE DE DATOS")
window.geometry('1080x600')

frameInf = tk.Frame(window, bg="#04517D")
frameInf.pack(side=tk.LEFT, fill= tk.BOTH ,expand=1)

frameIzq = tk.Frame(frameInf, width=260, height=800, bg='green')
frameIzq.pack_propagate(0)
frameIzq.pack(side='top', padx=0, pady=0, anchor='w')

frameTit = tk.Frame(frameIzq, bg = 'yellow', width=260, height=80)
frameTit.pack_propagate(0)
frameTit.pack(side='top', padx=0, pady=0, anchor='w')

LabelTit = tk.Label(frameTit, width=100, height=20, text = '  TIENDA DE \n CONVENIENCIA', bg = 'brown')
LabelTit.pack_propagate(0)
LabelTit.pack(side='top', padx=0, pady=0, anchor='w')
LabelTit.config(font=("Courier", 20))

#-----------------------------------------------------------------------
LabelAgregar = tk.Label(frameIzq, width=100, height=1, text = 'AGREGAR', bg = 'purple')
LabelAgregar.pack_propagate(0)
LabelAgregar.pack(side='top', padx=10, pady=5, anchor='center')
#---------------------------------------------------------------------------

#FRAMES Y LABELS DE AGREGAR
frameAg = tk.Frame(frameIzq, width=200, height=240, bg = 'blue')
frameAg.pack_propagate(0)
frameAg.pack(side='top', padx=10, pady=20, anchor='center')

LabelEmpleado = tk.Label(frameAg, width=100, height=1, text = 'Empleado', bg = 'purple')
LabelEmpleado.pack_propagate(0)
LabelEmpleado.pack(side='top', padx=10, pady=10, anchor='w')

LabelProveedor = tk.Label(frameAg, width=100, height=1, text = 'Proveedor', bg = 'purple')
LabelProveedor.pack_propagate(0)
LabelProveedor.pack(side='top', padx=10, pady=10, anchor='w')

LabelProducto = tk.Label(frameAg, width=100, height=1, text = 'Producto', bg = 'purple')
LabelProducto.pack_propagate(0)
LabelProducto.pack(side='top', padx=10, pady=10, anchor='w')

LabelCategoria = tk.Label(frameAg, width=100, height=1, text = 'Categoria', bg = 'purple')
LabelCategoria.pack_propagate(0)
LabelCategoria.pack(side='top', padx=10, pady=10, anchor='w')

#----------------------------------------------------------------------------
LabelMostrar = tk.Label(frameIzq, width=100, height=1, text = 'MOSTRAR', bg = 'purple')
LabelMostrar.pack_propagate(0)
LabelMostrar.pack(side='top', padx=10, pady=3, anchor='w')
#----------------------------------------------------------------------------

#FRAMES Y LABELS DE MOSTRAR
frameMo = tk.Frame(frameIzq, width=200, height=240, bg = 'yellow')
frameMo.pack_propagate(0)
frameMo.pack(side='top', padx=10, pady=20, anchor='center')

LabelTabla = tk.Label(frameMo, width=100, height=1, text = 'MOSTRAR', bg = 'purple')
LabelTabla.pack_propagate(0)
LabelTabla.pack(side='top', padx=10, pady=3, anchor='w')

main()