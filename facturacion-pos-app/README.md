# Facturación POS App

Este proyecto es una aplicación de facturación que utiliza Python, Tkinter para la interfaz gráfica, SQLAlchemy para la gestión de la base de datos, y permite la generación de reportes en formato Excel. Además, incluye un sistema de facturación con soporte para impresoras POS.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
facturacion-pos-app
├── src
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── db
│   │   ├── models.py            # Modelos de datos utilizando SQLAlchemy
│   │   └── session.py           # Gestión de la sesión de la base de datos
│   ├── ui
│   │   ├── __init__.py          # Inicialización del paquete de la interfaz de usuario
│   │   ├── ventana_principal.py  # Ventana principal de la aplicación
│   │   ├── ventana_facturacion.py # Ventana de facturación
│   │   ├── tooltips.py          # Funciones para mostrar tooltips
│   │   └── hotkeys.py           # Definición de combinaciones de teclas rápidas
│   ├── controllers
│   │   ├── crud.py              # Funciones para operaciones CRUD
│   │   ├── caja.py              # Gestión de la caja registradora
│   │   ├── usuarios.py          # Control de usuarios y perfiles
│   │   └── facturacion.py       # Lógica de facturación
│   ├── utils
│   │   ├── excel_report.py       # Funciones para generar reportes en Excel
│   │   ├── import_export.py      # Gestión de importación y exportación de datos
│   │   └── pos_printer.py       # Interacción con la impresora POS
│   └── types
│       └── index.py             # Tipos y interfaces utilizados en la aplicación
├── requirements.txt              # Dependencias necesarias para el proyecto
└── README.md                     # Documentación del proyecto
```

## Instalación

Para instalar las dependencias necesarias, ejecute el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

1. Ejecute el archivo `main.py` para iniciar la aplicación.
2. Utilice la ventana principal para acceder a las diferentes funcionalidades del CRUD y reportes.
3. En la ventana de facturación, registre las ventas y procese los pagos.

## Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir, por favor abra un issue o envíe un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.