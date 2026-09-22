import tkinter as tk
from tkinter import ttk
import time


# tema elegido: CPS Test

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        
        # Aquí se define una sola vez al instanciar la clase
        self.contador = 0 
                

import tkinter as tk

class Aplicacion:
    def __init__(self, root):
        # Ventana
        self.root = root
        self.root.geometry("800x600")
        
        # Aquí se define una sola vez al instanciar la clase
        self.contador = 0 
        
        self.label = tk.Label(self.root, text=self.contador, font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.botonClick = tk.Button(self.root, text="Incrementar", command=self.incrementar)
        self.botonClick.configure(state="disabled")
        self.botonClick.pack(pady=20)

        self.botonTemp = tk.Button(self.root, text="Iniciar Temporizador", command=lambda: self.temporizador())
        self.botonTemp.pack(pady=20)


    def incrementar(self):
        # Modifica el atributo existente sin redefinirlo
        self.contador += 1
        self.label.config(text=self.contador)

    def temporizador(self):
        self.botonClick.configure(state="normal")
        self.botonTemp.configure(state="disabled")

        for i in range(3, 0, -1):
            time.sleep(1)

        print("tiempo terminado")
        self.finalizar()

    def finalizar(self):
        self.botonTemp.configure(state="disabled")
        self.botonClick.configure(state="disabled")
        print("Finalizado boton Temp y click")


    

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
