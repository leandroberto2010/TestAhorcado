import tkinter as tk
from Ahorcado import Ahorcado

class AhorcadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ahorcado")
        
        #Ventana de inicio
        label = tk.Label(root, text="Ingresar palabra: ", font=("Helvetica", 14))
        label.pack(pady=10)
        
        self.palabraInput = tk.Entry(root, font=("Helvetica", 14), show="*")
        self.palabraInput.pack(pady=5)
        
        self.startButton = tk.Button(root, text="Empezar juego", command=self.start)
        self.startButton.pack(pady=10)

        #Ocultar ventana principal
        self.ocultarElementos()

    def ocultarElementos(self):
        """Oculta los elementos de la interfaz del juego hasta que se ingrese la palabra secreta."""
        self.palabraLabel = tk.Label(self.root, font=("Helvetica", 24))
        self.letraInput = tk.Entry(self.root, font=("Helvetica", 18), width=5)
        self.adivinarLetraButton = tk.Button(self.root, text="Adivinar Letra", command=self.adivinarLetra)
        self.palabraCompletaInput = tk.Entry(self.root, font=("Helvetica", 18), width=20)
        self.adivinarPalabraButton = tk.Button(self.root, text="Adivinar Palabra", command=self.adivinarPalabra)
        self.resetButton = tk.Button(self.root, text="Reiniciar", command=self.reset )
        self.usadasLabel = tk.Label(self.root, text="Letras usadas: ", font=("Helvetica", 16))
        self.vidasLabel = tk.Label(self.root, text="Vidas restantes: 6", font=("Helvetica", 16))
        self.mensajeLabel = tk.Label(self.root, text="", font=("Helvetica", 16), fg="red")

    def start(self):
        """Inicia el juego con la palabra ingresada y muestra la interfaz del juego."""
        palabra = self.palabraInput.get().upper()
        if palabra:
            self.juego = Ahorcado(palabra)
            
            #Ocultar ventana de inicio
            self.palabraInput.pack_forget()
            self.startButton.pack_forget()

            self.mostrarInterfaz()

    def mostrarInterfaz(self):
        """Muestra los elementos de la interfaz del juego."""
        self.palabraLabel.config(text=" ".join(self.juego.palabraescondida))
        self.palabraLabel.pack(pady=10)

        self.letraInput.pack(pady=10)
        self.adivinarLetraButton.pack(pady=10)
        self.palabraCompletaInput.pack(pady=10)
        self.adivinarPalabraButton.pack(pady=10)
        self.usadasLabel.pack(pady=10)
        self.mensajeLabel.pack(pady=10)
        self.vidasLabel.pack(pady=10)
        self.resetButton.pack(padx=10)

    def update(self, mensaje=""):
        """Actualiza la interfaz de usuario con el estado actual del juego."""
        #Actualizar elementos
        self.palabraLabel.config(text=" ".join(self.juego.palabraescondida))
        self.usadasLabel.config(text="Letras usadas: " + ", ".join(self.juego.letrasUsadas))
        self.mensajeLabel.config(text=mensaje)
        self.vidasLabel.config(text="Vidas restantes: " + str(self.juego.getVidas()))

        #Deshabilitar botones si termino
        if mensaje == "GANASTE" or mensaje == "PERDISTE":
            self.letraInput.config(state="disabled")
            self.adivinarLetraButton.config(state="disabled")
            self.palabraCompletaInput.config(state="disabled")
            self.adivinarPalabraButton.config(state="disabled")

    def adivinarLetra(self):
        letra = self.letraInput.get().upper()
        if letra:
            resultado = self.juego.pruebaLetra(letra)
            self.update(mensaje=resultado)
            self.letraInput.delete(0, tk.END)

    def adivinarPalabra(self):
        intentoPalabra = self.palabraCompletaInput.get().upper()
        if intentoPalabra:
            resultado = self.juego.verificarPalabra(intentoPalabra)
            self.update(mensaje=resultado)
            self.palabraCompletaInput.delete(0, tk.END)
    
    def reset(self):
        #Reinicia el estado interno
        self.juego.reset()

        #Ocultar elementos
        self.palabraLabel.pack_forget()
        self.letraInput.pack_forget()
        self.adivinarLetraButton.pack_forget()
        self.palabraCompletaInput.pack_forget()
        self.adivinarPalabraButton.pack_forget()
        self.usadasLabel.pack_forget()
        self.mensajeLabel.pack_forget()
        self.vidasLabel.pack_forget()
        self.resetButton.pack_forget()

        #Habilitar botones
        self.letraInput.config(state="normal")
        self.adivinarLetraButton.config(state="normal")
        self.palabraCompletaInput.config(state="normal")
        self.adivinarPalabraButton.config(state="normal")


        #Limpiar campos
        self.palabraInput.delete(0, tk.END)
        self.letraInput.delete(0, tk.END)
        self.palabraCompletaInput.delete(0, tk.END)
        self.update()

        #Mostrar ingreso de nuevo
        self.palabraInput.pack(pady=5)
        self.startButton.pack(pady=10)

#Ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AhorcadoApp(root)
    root.mainloop()
