from tkinter import Tk, Frame, Menu, Button, Label
from tkinter import messagebox
from typing import Any

class VentanaPrincipal:
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.master.title("Sistema de Facturación POS")
        self.master.geometry("800x600")

        self.frame = Frame(self.master)
        self.frame.pack(fill="both", expand=True)

        self.create_menu()
        self.create_widgets()

    def create_menu(self) -> None:
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        archivo_menu = Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Importar Datos", command=self.importar_datos)
        archivo_menu.add_command(label="Exportar Datos", command=self.exportar_datos)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.master.quit)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        reportes_menu = Menu(menu_bar, tearoff=0)
        reportes_menu.add_command(label="Generar Reporte", command=self.generar_reporte)
        menu_bar.add_cascade(label="Reportes", menu=reportes_menu)

        usuarios_menu = Menu(menu_bar, tearoff=0)
        usuarios_menu.add_command(label="Gestionar Usuarios", command=self.gestionar_usuarios)
        menu_bar.add_cascade(label="Usuarios", menu=usuarios_menu)

    def create_widgets(self) -> None:
        Label(self.frame, text="Bienvenido al Sistema de Facturación POS", font=("Arial", 16)).pack(pady=20)

        Button(self.frame, text="Facturación", command=self.abrir_facturacion).pack(pady=10)
        Button(self.frame, text="Gestión de Productos", command=self.gestionar_productos).pack(pady=10)
        Button(self.frame, text="Gestión de Clientes", command=self.gestionar_clientes).pack(pady=10)

    def abrir_facturacion(self) -> None:
        messagebox.showinfo("Facturación", "Abrir ventana de facturación.")

    def gestionar_productos(self) -> None:
        messagebox.showinfo("Gestión de Productos", "Abrir gestión de productos.")

    def gestionar_clientes(self) -> None:
        messagebox.showinfo("Gestión de Clientes", "Abrir gestión de clientes.")

    def importar_datos(self) -> None:
        messagebox.showinfo("Importar Datos", "Funcionalidad de importación de datos.")

    def exportar_datos(self) -> None:
        messagebox.showinfo("Exportar Datos", "Funcionalidad de exportación de datos.")

    def generar_reporte(self) -> None:
        messagebox.showinfo("Generar Reporte", "Funcionalidad para generar reportes.")

    def gestionar_usuarios(self) -> None:
        messagebox.showinfo("Gestionar Usuarios", "Funcionalidad para gestionar usuarios.")

if __name__ == "__main__":
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()