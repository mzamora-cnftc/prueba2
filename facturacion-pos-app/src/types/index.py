from typing import List, Dict, Any, Optional, Protocol

class User(Protocol):
    id: int
    username: str
    password: str
    role: str

class Product(Protocol):
    id: int
    name: str
    price: float
    category_id: int
    stock: int

class Invoice(Protocol):
    id: int
    user_id: int
    total_amount: float
    payment_status: str
    items: List[Dict[str, Any]]

class Category(Protocol):
    id: int
    name: str

class Payment(Protocol):
    id: int
    invoice_id: int
    amount: float
    payment_method: str

class CRUDOperations(Protocol):
    def create(self, item: Any) -> None:
        ...

    def read(self, item_id: int) -> Optional[Any]:
        ...

    def update(self, item_id: int, item: Any) -> None:
        ...

    def delete(self, item_id: int) -> None:
        ...

class Report(Protocol):
    title: str
    data: List[Dict[str, Any]]