from decimal import Decimal

products = [
    {"code": "P001", "name": "น้ำดื่ม 600ml", "price": Decimal("7"), "qty": 48},
    {"code": "P002", "name": "น้ำส้ม 1000ml", "price": Decimal("30"), "qty": 36},
    {"code": "P003", "name": "น้ำอัดลม 600ml", "price": Decimal("40"), "qty": 24}
]

def total_stock_value(items):
    total = Decimal("0")
    for product in items:
        total += product["price"] * product["qty"]
    return total

value = total_stock_value(products)
print(f"มูลค่าสต๊อกรวม {value:,.2f} บาท")