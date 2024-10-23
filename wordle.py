import tkinter as tk
from tkinter import messagebox
import random

class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle en Español")
        self.root.configure(bg='#121213')
        
        # Lista de palabras
        self.palabras = [
            "gatos", "perro", "verde", "azual", "negro", "blaco", 
            "libro", "papel", "tenis", "jugar", "comer", "beber",
            "plato", "mesa", "silla", "coche", "avion", "barco",
            "mundo", "tierra"
        ]
        
        # Configuración del juego
        self.palabra = random.choice(self.palabras)
        self.fila_actual = 0
        self.columna_actual = 0
        self.intentos_maximos = 6
        
        # Crear la cuadrícula de letras
        self.celdas = []
        self.crear_interfaz()
        
        # Vincular eventos de teclado
        self.root.bind('<Key>', self.tecla_presionada)
        self.root.bind('<Return>', self.verificar_palabra)
        self.root.bind('<BackSpace>', self.borrar_letra)

    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.root, text="WORDLE", font=('Arial', 24, 'bold'), 
                         fg='white', bg='#121213')
        titulo.pack(pady=20)
        
        # Marco para la cuadrícula
        marco_cuadricula = tk.Frame(self.root, bg='#121213')
        marco_cuadricula.pack(padx=20, pady=20)
        
        # Crear cuadrícula de 6x5
        for i in range(6):
            fila = []
            for j in range(5):
                celda = tk.Label(marco_cuadricula, 
                               width=4, height=2,
                               font=('Arial', 20, 'bold'),
                               bg='#3a3a3c',
                               fg='white',
                               relief='solid',
                               borderwidth=2)
                celda.grid(row=i, column=j, padx=2, pady=2)
                fila.append(celda)
            self.celdas.append(fila)
            
        # Instrucciones
        instrucciones = tk.Label(self.root,
                               text="Usa el teclado para escribir y Enter para validar",
                               font=('Arial', 12),
                               fg='white',
                               bg='#121213')
        instrucciones.pack(pady=10)

    def tecla_presionada(self, evento):
        # Solo procesar letras
        if evento.char.isalpha() and self.columna_actual < 5:
            letra = evento.char.upper()
            self.celdas[self.fila_actual][self.columna_actual].config(text=letra)
            self.columna_actual += 1

    def borrar_letra(self, evento):
        if self.columna_actual > 0:
            self.columna_actual -= 1
            self.celdas[self.fila_actual][self.columna_actual].config(text='')

    def obtener_palabra_actual(self):
        return ''.join(celda['text'].lower() for celda in self.celdas[self.fila_actual])

    def verificar_palabra(self, evento):
        if self.columna_actual != 5:
            messagebox.showwarning("Aviso", "¡La palabra debe tener 5 letras!")
            return

        intento = self.obtener_palabra_actual()
        
        # Colorear celdas según el resultado
        for i, (letra_intento, letra_palabra) in enumerate(zip(intento, self.palabra)):
            if letra_intento == letra_palabra:
                color = '#538d4e'  # Verde para letras correctas
            elif letra_intento in self.palabra:
                color = '#b59f3b'  # Amarillo para letras en posición incorrecta
            else:
                color = '#3a3a3c'  # Gris para letras incorrectas
            self.celdas[self.fila_actual][i].config(bg=color)

        # Verificar victoria
        if intento == self.palabra:
            messagebox.showinfo("¡Felicitaciones!", 
                              f"¡Has ganado en {self.fila_actual + 1} intentos!")
            self.root.quit()
            return

        # Verificar derrota
        if self.fila_actual == self.intentos_maximos - 1:
            messagebox.showinfo("Fin del juego", 
                              f"¡Se acabaron los intentos! La palabra era {self.palabra}")
            self.root.quit()
            return

        # Preparar siguiente intento
        self.fila_actual += 1
        self.columna_actual = 0

if __name__ == "__main__":
    root = tk.Tk()
    juego = WordleGUI(root)
    root.mainloop()
