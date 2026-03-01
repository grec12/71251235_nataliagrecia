try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    print("Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol")
except ValueError:
    print("Input harus berupa angka")