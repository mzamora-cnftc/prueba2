from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional

class Caja:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.session: Optional[Session] = None

    def abrir_caja(self):
        try:
            self.session = Session(self.engine)
            # Logic to open the cash register
            print("Caja abierta.")
        except SQLAlchemyError as e:
            print(f"Error al abrir la caja: {e}")

    def cerrar_caja(self):
        if self.session:
            self.session.close()
            print("Caja cerrada.")

    def procesar_pago(self, monto: float):
        if self.session:
            # Logic to process payment
            print(f"Pago procesado por un monto de: {monto}")
        else:
            print("La caja no está abierta.")

    def imprimir_comprobante(self, datos: dict):
        # Logic to interact with the POS printer
        print("Comprobante impreso con los siguientes datos:", datos)

    def obtener_consecutivo(self) -> int:
        # Logic to get the next invoice number
        return 1  # Placeholder for actual implementation

    def __del__(self):
        self.cerrar_caja()