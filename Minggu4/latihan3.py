try:
    bulan = int(input("masukkan bulan (1-12): "))

    if 1 < bulan > 12:
        print("Bulan tidak valid, masukkan angka 1-12")
    else: 
        if bulan in [4, 6, 9, 11]:
            print("Jumlah hari: 30")
        elif bulan in [1, 3, 5, 7, 8, 10, 12]:
            print("Jumlah hari: 31")
        else:
            print("Jumlah hari: 29")
except ValueError:
    print("Input harus berupa angka!")