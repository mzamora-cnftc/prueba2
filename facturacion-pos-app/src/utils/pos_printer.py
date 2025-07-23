from typing import Any, Dict
import escpos.printer

class POSPrinter:
    def __init__(self, printer_name: str):
        self.printer = escpos.printer.Usb(printer_name)

    def print_receipt(self, items: Dict[str, Any], total: float, payment_method: str) -> None:
        self.printer.set(align='center', font='a', width=2, height=2)
        self.printer.text("Comprobante de Venta\n")
        self.printer.text("-------------------------\n")
        
        for item, details in items.items():
            self.printer.text(f"{item}: {details['quantity']} x {details['price']:.2f} = {details['total']:.2f}\n")
        
        self.printer.text("-------------------------\n")
        self.printer.text(f"Total: {total:.2f}\n")
        self.printer.text(f"Método de Pago: {payment_method}\n")
        self.printer.text("-------------------------\n")
        self.printer.cut()