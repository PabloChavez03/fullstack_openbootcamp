import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="hola", bg="yellow", fg="blue")
label_saludo.pack(ipadx=50,ipady=50,fill='x')

label_adios = tkinter.Label(window, text="adios", bg="green", fg="white")
label_adios.pack(ipadx=50,ipady=100,fill='both')

window.mainloop()