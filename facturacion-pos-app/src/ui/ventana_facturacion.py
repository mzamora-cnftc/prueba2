from tkinter import Tk, Frame, Label, Entry, Button, StringVar, messagebox
from typing import List
from controllers.facturacion import procesar_pago  # Importar la función de procesamiento de pagos

class VentanaFacturacion:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Ventana de Facturación")
        self.frame = Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.label_producto = Label(self.frame, text="Producto:")
        self.label_producto.grid(row=0, column=0)
        self.entry_producto = Entry(self.frame)
        self.entry_producto.grid(row=0, column=1)

        self.label_cantidad = Label(self.frame, text="Cantidad:")
        self.label_cantidad.grid(row=1, column=0)
        self.entry_cantidad = Entry(self.frame)
        self.entry_cantidad.grid(row=1, column=1)

        self.label_precio = Label(self.frame, text="Precio:")
        self.label_precio.grid(row=2, column=0)
        self.entry_precio = Entry(self.frame)
        self.entry_precio.grid(row=2, column=1)

        self.boton_facturar = Button(self.frame, text="Facturar", command=self.facturar)
        self.boton_facturar.grid(row=3, columnspan=2)

        self.resultado = StringVar()
        self.label_resultado = Label(self.frame, textvariable=self.resultado)
        self.label_resultado.grid(row=4, columnspan=2)

    def facturar(self):
        producto = self.entry_producto.get()
        cantidad = self.entry_cantidad.get()
        precio = self.entry_precio.get()

        if not producto or not cantidad.isdigit() or not precio.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")
            return

        cantidad = int(cantidad)
        precio = float(precio)
        total = cantidad * precio

        # Procesar el pago (aquí se puede integrar la lógica de pago)
        resultado_pago = procesar_pago(producto, cantidad, total)

        if resultado_pago:
            self.resultado.set(f"Factura generada: {producto} x {cantidad} = {total:.2f}")
        else:
            self.resultado.set("Error al procesar el pago.")

def main():
    root = Tk()
    app = VentanaFacturacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()