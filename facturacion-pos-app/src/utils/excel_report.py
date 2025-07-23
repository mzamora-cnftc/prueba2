from typing import List, Dict
import pandas as pd

def generate_excel_report(data: List[Dict], filename: str) -> None:
    """
    Genera un reporte en formato Excel a partir de los datos proporcionados.

    :param data: Lista de diccionarios con los datos a incluir en el reporte.
    :param filename: Nombre del archivo Excel a generar.
    """
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def create_report_template(columns: List[str], filename: str) -> None:
    """
    Crea una plantilla de reporte en formato Excel con las columnas especificadas.

    :param columns: Lista de nombres de columnas para la plantilla.
    :param filename: Nombre del archivo Excel a generar.
    """
    df = pd.DataFrame(columns=columns)
    df.to_excel(filename, index=False)