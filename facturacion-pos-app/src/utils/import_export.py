from typing import List, Dict
import pandas as pd

def export_to_excel(data: List[Dict], filename: str) -> None:
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def import_from_excel(filename: str) -> List[Dict]:
    df = pd.read_excel(filename)
    return df.to_dict(orient='records')

def generate_excel_template(columns: List[str], filename: str) -> None:
    df = pd.DataFrame(columns=columns)
    df.to_excel(filename, index=False)