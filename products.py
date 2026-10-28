products = [
    {"code": "P001", "name": "น้ำดื่ม 600ml", "price": 7, "qty": 48},
    {"code": "P002", "name": "น้ำส้ม 1000ml", "price": 30, "qty": 36},
    {"code": "P003", "name": "น้ำอัดลม 600ml", "price": 40, "qty": 24}
]

for product in products:
    print (f"{product['code']}  {product['name']}  ราคา {product['price']} บาท  คงเหลือ {product['qty']} ชิ้น")