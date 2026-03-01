try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    else:
        print("Nol")
except ValueError:
    print("Error: Input harus berupa angka")