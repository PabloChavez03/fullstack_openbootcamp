import tkinter

window = tkinter.Tk()

paises = ["Argentina","Paraguay","Bolivia","Uruguay","Perú","Italia","España"]

labelTitulo = tkinter.Label(window,text="Paises")
labelTitulo.pack(padx=10)

listaPaises = tkinter.StringVar(value=paises)
listaBox = tkinter.Listbox(window, height=10, listvariable=listaPaises, selectmode='single')
listaBox.pack(padx=10,pady=10)


def seleccionado(event):
    showPais.config(text=paises[listaBox.curselection()[0]])

listaBox.bind('<<ListboxSelect>>', seleccionado)

showPais = tkinter.Label(window, text='')
showPais.pack(padx=10,pady=10)

window.mainloop()