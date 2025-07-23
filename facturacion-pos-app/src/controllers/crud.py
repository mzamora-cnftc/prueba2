from typing import List, Optional
from sqlalchemy.orm import Session
from src.db.models import Cliente, Producto, Categoria, Departamento  # Importar los modelos necesarios

class CRUD:
    @staticmethod
    def create_cliente(db: Session, nombre: str, email: str) -> Cliente:
        nuevo_cliente = Cliente(nombre=nombre, email=email)
        db.add(nuevo_cliente)
        db.commit()
        db.refresh(nuevo_cliente)
        return nuevo_cliente

    @staticmethod
    def read_cliente(db: Session, cliente_id: int) -> Optional[Cliente]:
        return db.query(Cliente).filter(Cliente.id == cliente_id).first()

    @staticmethod
    def update_cliente(db: Session, cliente_id: int, nombre: str, email: str) -> Optional[Cliente]:
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if cliente:
            cliente.nombre = nombre
            cliente.email = email
            db.commit()
            db.refresh(cliente)
        return cliente

    @staticmethod
    def delete_cliente(db: Session, cliente_id: int) -> Optional[Cliente]:
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if cliente:
            db.delete(cliente)
            db.commit()
        return cliente

    @staticmethod
    def list_clientes(db: Session) -> List[Cliente]:
        return db.query(Cliente).all()

    @staticmethod
    def create_producto(db: Session, nombre: str, precio: float, categoria_id: int) -> Producto:
        nuevo_producto = Producto(nombre=nombre, precio=precio, categoria_id=categoria_id)
        db.add(nuevo_producto)
        db.commit()
        db.refresh(nuevo_producto)
        return nuevo_producto

    @staticmethod
    def read_producto(db: Session, producto_id: int) -> Optional[Producto]:
        return db.query(Producto).filter(Producto.id == producto_id).first()

    @staticmethod
    def update_producto(db: Session, producto_id: int, nombre: str, precio: float, categoria_id: int) -> Optional[Producto]:
        producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if producto:
            producto.nombre = nombre
            producto.precio = precio
            producto.categoria_id = categoria_id
            db.commit()
            db.refresh(producto)
        return producto

    @staticmethod
    def delete_producto(db: Session, producto_id: int) -> Optional[Producto]:
        producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if producto:
            db.delete(producto)
            db.commit()
        return producto

    @staticmethod
    def list_productos(db: Session) -> List[Producto]:
        return db.query(Producto).all()

    # Métodos adicionales para Categoria y Departamento se pueden agregar aquí siguiendo el mismo patrón.