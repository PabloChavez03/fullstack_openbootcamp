import tkinter

window = tkinter.Tk()

valor = tkinter.StringVar()

def reset(event):
    valor.set('')

r1 = tkinter.Radiobutton(window, text="Boton 1", value="Soy el boton 1", variable=valor)
r2 = tkinter.Radiobutton(window, text="Boton 2", value="Soy el boton 2", variable=valor)
r3 = tkinter.Radiobutton(window, text="Boton 3", value="Soy el boton 3", variable=valor)
r1.pack(padx=10,pady=10)
r2.pack(padx=10,pady=10)
r3.pack(padx=10,pady=10)

labelValor = tkinter.Label(window, textvariable=valor)
labelValor.pack(padx=10,pady=10)

botonSalir = tkinter.Button(window, text="Reset")
botonSalir.pack()

botonSalir.bind('<Button-1>', reset)

window.mainloop()