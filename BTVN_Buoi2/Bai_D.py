secret = 7
max_turns = 5
turns = 0
while turns < max_turns:
    a = int(input(f"Lượt {turns+1}. Nhập số bạn đoán"))
    turns += 1
    if a == secret:
        print(f"Bạn đã đoán chính xác số {secret} ở lượt thứ {turns}")
        break
    elif a < secret:
        print("Bạn hãy đoán số lớn hơn")
    else:
        print("Bạn hãy đoán số nhỏ hơn")  
else:
    print(f"Bạn đã hết lượt chơi")