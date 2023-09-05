import tkinter as tk

root = tk.Tk()
root.title("Testeando con Tkinter")
root.resizable(0, 0)
root.config(bg="lightblue", padx=10, pady=10)



label = tk.Label(root, text="Holi, porfi no presiones este botoncito c:")
label.grid(column=0, row=0)
label.config(bg="lightblue")

def clickBoton() :
    label["text"] = "¡¡¡TE DIJE QUE NO PRESIONES LA WEÁ CONCHETUMAREEE!!!"
    root.config(bg="red", padx=10, pady=10)
    label.config(bg="red", font=("", 15))
    boton["text"], boton["state"], boton["cursor"] = "el ql aweonao xdddd", "disabled", "x_cursor"

boton = tk.Button(root, text="No presionar", command=clickBoton, cursor="hand2")
boton.grid(column=1, row=0, padx=(20, 0))
boton.config(padx=10, pady=10)

root.mainloop()