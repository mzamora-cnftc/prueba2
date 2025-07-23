from tkinter import Tk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.session import Session
from ui.ventana_principal import VentanaPrincipal

def main():
    # Inicializar la ventana principal
    root = Tk()
    root.title("Facturación POS")
    
    # Establecer conexión a la base de datos
    engine = create_engine('sqlite:///facturacion.db')  # Cambiar a la URL de MariaDB si es necesario
    Session.configure(bind=engine)
    
    # Crear la interfaz de usuario
    app = VentanaPrincipal()
    app.mainloop()  # <-- Usar mainloop en vez de pack

if __name__ == "__main__":
    main()