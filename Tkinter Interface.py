#-*- coding: utf-8 -*-
# Created on Fri Sep 29 19:39:03 2023
# @author: Monjaraz Briseno Luis FERNANDO

from tkinter import *
import re
import random
import string

class aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("600x400")
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('Expresiones regulares')
        
        # Etiquetas y Frames principales [cite: 2665-2671]
        label = Label(self.raiz, text='Validación de expresiones regulares')
        label.pack(side=TOP)
        
        self.textos = Frame(self.raiz)
        self.textos.pack(side=TOP)
        
        self.frameDeAbajo = Frame(self.raiz)
        self.frameDeAbajo.pack(side=BOTTOM)
        
        # Entradas de texto (Entry) [cite: 2673-2685]
        self.t1 = Entry(self.textos, width=40)
        self.t1.grid(row=0, column=1, padx=10, pady=10)
        self.t2 = Entry(self.textos, width=40)
        self.t2.grid(row=1, column=1, padx=10, pady=10)
        self.t3 = Entry(self.textos, width=40)
        self.t3.grid(row=2, column=1, padx=10, pady=10)
        self.t4 = Entry(self.textos, width=40)
        self.t4.grid(row=3, column=1, padx=10, pady=10)
        
        self.num1 = Entry(self.textos, width=40)
        self.num1.grid(row=5, column=1, padx=10, pady=10)
        self.num2 = Entry(self.textos, width=40)
        self.num2.grid(row=6, column=1, padx=10, pady=10)
        
        # Botones de Validación [cite: 2686]
        self.b1 = Button(self.textos, text='Validar', command=lambda: self.validar(self.t1, self.l1))
        self.b1.grid(row=0, column=2, padx=10, pady=10)
        self.b2 = Button(self.textos, text='Validar', command=lambda: self.validar(self.t2, self.l2))
        self.b2.grid(row=1, column=2, padx=10, pady=10)
        self.b3 = Button(self.textos, text='Validar', command=lambda: self.validar(self.t3, self.l3))
        self.b3.grid(row=2, column=2, padx=10, pady=10)
        self.b4 = Button(self.textos, text='Validar', command=lambda: self.validar(self.t4, self.l4))
        self.b4.grid(row=3, column=2, padx=10, pady=10)
        
        self.b7 = Button(self.textos, text='Sumar', command=self.sumar)
        self.b7.grid(row=7, column=2, padx=10, pady=10)
        
        # Etiquetas de resultado (Labels) [cite: 2694-2709]
        self.l1 = Label(self.textos, text='...')
        self.l1.grid(row=0, column=3)
        self.l2 = Label(self.textos, text='...')
        self.l2.grid(row=1, column=3)
        self.l3 = Label(self.textos, text='...')
        self.l3.grid(row=2, column=3)
        self.l4 = Label(self.textos, text='...')
        self.l4.grid(row=3, column=3)
        self.l5 = Label(self.textos, text='Num 1')
        self.l5.grid(row=5, column=3)
        self.l6 = Label(self.textos, text='Num 2')
        self.l6.grid(row=6, column=3)
        self.l7 = Label(self.textos, text='Resultado:')
        self.l7.grid(row=7, column=3)
        
        # Botones de control inferiores [cite: 2710-2719]
        self.bsalir = Button(self.frameDeAbajo, text='Salir', command=self.raiz.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar = Button(self.frameDeAbajo, text='Limpiar', command=self.limpiar)
        self.blimpiar.pack(side=LEFT)
        self.doradoTNR = Button(self.frameDeAbajo, text='Personalizar', command=self.doradoTMR)
        self.doradoTNR.pack(side=LEFT)
        
        # Botones para generación aleatoria [cite: 2720-2742]
        self.ipAleatoria1 = Button(self.textos, text='IP Aleatoria', command=lambda: self.IPAleatoria(self.t1))
        self.ipAleatoria1.grid(row=0, column=0, padx=10, pady=10)
        self.ipAleatoria2 = Button(self.textos, text='IP Aleatoria', command=lambda: self.IPAleatoria(self.t2))
        self.ipAleatoria2.grid(row=1, column=0, padx=10, pady=10)
        self.ipAleatoria3 = Button(self.textos, text='IP Aleatoria', command=lambda: self.IPAleatoria(self.t3))
        self.ipAleatoria3.grid(row=2, column=0, padx=10, pady=10)
        self.ipAleatoria4 = Button(self.textos, text='IP Aleatoria', command=lambda: self.IPAleatoria(self.t4))
        self.ipAleatoria4.grid(row=3, column=0, padx=10, pady=10)
        
        self.noip1 = Button(self.textos, text='No IP Aleatoria', command=lambda: self.NoIpAleatoria(self.t1))
        self.noip1.grid(row=0, column=4, padx=10, pady=10)
        self.noip2 = Button(self.textos, text='No IP Aleatoria', command=lambda: self.NoIpAleatoria(self.t2))
        self.noip2.grid(row=1, column=4, padx=10, pady=10)
        self.noip3 = Button(self.textos, text='No IP Aleatoria', command=lambda: self.NoIpAleatoria(self.t3))
        self.noip3.grid(row=2, column=4, padx=10, pady=10)
        self.noip4 = Button(self.textos, text='No IP Aleatoria', command=lambda: self.NoIpAleatoria(self.t4))
        self.noip4.grid(row=3, column=4, padx=10, pady=10)
        
        self.raiz.mainloop()

    def limpiar(self):
        """Limpia todos los campos de entrada y restablece las etiquetas."""
        for entry in [self.t1, self.t2, self.t3, self.t4, self.num1, self.num2]:
            entry.delete(0, 'end')
        for label in [self.l1, self.l2, self.l3, self.l4]:
            label.config(fg='black', text='...')
        self.l7.config(fg='black', text='Resultado:')

    def validar(self, cuadro, etiqueta):
        """Valida si el texto ingresado es una IPv4 válida usando Regex."""
        txtAValidar = cuadro.get()
        # Expresión regular para IPv4 (0-255) [cite: 2755]
        regex = r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
        if re.search(regex, txtAValidar):
            etiqueta.config(fg='green', text='IPv4 Valida')
        else:
            etiqueta.config(fg='red', text='IPv4 Invalida')

    def doradoTMR(self):
        """Cambia el diseño de la interfaz a un fondo dorado y fuente Times New Roman."""
        self.raiz.configure(bg='gold')
        estilo = ('Times New Roman', 12)
        # El reporte menciona un cambio de geometría a 1280x720 [cite: 2762]
        self.raiz.geometry('1280x720')
        for label in [self.l1, self.l2, self.l3, self.l4]:
            label.configure(font=estilo)

    def IPAleatoria(self, cuadro):
        """Genera una dirección IP aleatoria válida[cite: 2766]."""
        IPxdnt = ".".join(str(random.randint(0, 255)) for _ in range(4))
        cuadro.delete(0, 'end')
        cuadro.insert(0, IPxdnt)

    def NoIpAleatoria(self, cuadro):
        """Genera una cadena aleatoria de 20 caracteres que no es una IP [cite: 2772-2776]."""
        caracteres = string.ascii_letters + string.digits
        xdnt = ''.join(random.choice(caracteres) for _ in range(20))
        cuadro.delete(0, 'end')
        cuadro.insert(0, xdnt)

    def sumar(self):
        """Suma los valores de num1 y num2 con manejo de errores [cite: 2781-2786]."""
        try:
            v1 = int(self.num1.get())
            v2 = int(self.num2.get())
            suma = v1 + v2
            self.l7.config(fg='green', text='Resultado: ' + str(suma))
        except ValueError:
            self.l7.config(fg='red', text='Resultado: Error')

# Ejecución de la aplicación
if __name__ == "__main__":
    app = aplicacion()