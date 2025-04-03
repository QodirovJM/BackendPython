from dataclasses import dataclass

@dataclass
class BarDrink:
    name: str
    price: float

@dataclass
class BarCustomer:
    name: str
    spent: float

@dataclass
class BarOrder:
    order_id: int
    drink: str