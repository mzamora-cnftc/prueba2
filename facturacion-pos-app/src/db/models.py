from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Departamento(Base):
    __tablename__ = 'departamentos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String)
    telefono = Column(String)

class Familia(Base):
    __tablename__ = 'familias'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Unidad(Base):
    __tablename__ = 'unidades'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Categoria(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Pasillo(Base):
    __tablename__ = 'pasillos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Producto(Base):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    familia_id = Column(Integer, ForeignKey('familias.id'))
    
    familia = relationship("Familia")

class Ubicacion(Base):
    __tablename__ = 'ubicaciones'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)