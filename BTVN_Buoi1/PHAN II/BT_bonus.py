name = input("Tên của bạn: ")
print(name)

a = input("Nhập số thứ 1: ")
a = float(a)
b = input("Nhập số thứ 2: ")
b = float(b)

sum = a+b
difference = a-b
product = a * b
quotient = a/b

print(f"Tổng của 2 số là {sum :.2f}")
print(f"Hiệu của 2 số là {difference :.2f}")
print(f"Tích của 2 số là {product :.2f}")
print(f"Thương của 2 số là {quotient :.2f}")