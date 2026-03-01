try:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    if a > b and a > c:
        print("Terbesar:", a)
    elif b > a and b > c:
        print("Terbesar:", b)
    else:
        print("Terbesar:", c)
except ValueError:
    print("Error: Semua input harus berupa angka!")