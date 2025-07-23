from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.db.models import Factura, Producto
from src.utils.pos_printer import imprimir_factura
from typing import List, Optional

class FacturacionController:
    def __init__(self, session: Session):
        self.session = session

    def crear_factura(self, productos: List[dict], total: float, cliente_id: Optional[int] = None) -> Factura:
        nueva_factura = Factura(total=total, cliente_id=cliente_id)
        self.session.add(nueva_factura)
        try:
            self.session.commit()
            for producto in productos:
                self.agregar_producto_a_factura(nueva_factura.id, producto['id'], producto['cantidad'])
            return nueva_factura
        except IntegrityError:
            self.session.rollback()
            raise

    def agregar_producto_a_factura(self, factura_id: int, producto_id: int, cantidad: int):
        producto = self.session.query(Producto).filter(Producto.id == producto_id).first()
        if producto:
            producto.cantidad -= cantidad
            self.session.commit()
            # Aquí se podría agregar la lógica para registrar el detalle de la factura

    def procesar_pago(self, factura_id: int, metodo_pago: str):
        factura = self.session.query(Factura).filter(Factura.id == factura_id).first()
        if factura:
            factura.metodo_pago = metodo_pago
            self.session.commit()
            imprimir_factura(factura)

    def obtener_factura(self, factura_id: int) -> Optional[Factura]:
        return self.session.query(Factura).filter(Factura.id == factura_id).first()

    def listar_facturas(self) -> List[Factura]:
        return self.session.query(Factura).all()