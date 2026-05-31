def jumlah_deret_ganil(n):
    if n <= 1:
        return 1
    else:
        return n + jumlah_deret_ganil(n - 2)
    
try:
    n = int(input("Masukkan nilai n: "))
    if n < 1:
        print("Nilai n harus lebih besar dari 0.")
    else:
        hasil = jumlah_deret_ganil(n)
        print(f"Jumlah deret ganjil adalah {hasil}")
except ValueError:
    print("Masukkan angka bulat positif!")

