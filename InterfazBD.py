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

LabelAgregar = tk.Label(frameIzq, width=100, height=1, text = 'AGREGAR', bg = 'purple')
LabelAgregar.pack_propagate(0)
LabelAgregar.pack(side='top', padx=10, pady=5, anchor='center')

#TREE 1
data_tree = ttk.Treeview(frameIzq, height = 11)
data_tree.pack_configure(padx=10, pady=10)

LabelMostrar = tk.Label(frameIzq, width=100, height=1, text = 'MOSTRAR', bg = 'purple')
LabelMostrar.pack_propagate(0)
LabelMostrar.pack(side='top', padx=10, pady=3, anchor='w')

#TREE 2
data_tree2 = ttk.Treeview(frameIzq, height = 11)
data_tree2.pack_configure(padx=10, pady=10)

main()