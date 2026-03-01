try:
    sisi1 = int(input("Masukkan sisi 1: "))
    sisi2 = int(input("Masukkan sisi 2: "))
    sisi3 = int(input("Masukkan sisi 3: "))

    if sisi1 > 0 and sisi2 > 0 and sisi1 + sisi2 > sisi3 \
        and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
        if sisi1 == sisi2 == sisi3:
            print("3 sisi sama")
        elif sisi1 == sisi2 or sisi1== sisi3 or sisi2 == sisi3:
            print("2 sisi sama")
        else:
            print("Tidak ada yang sama")
    else:
        print("Input tidak valid")

except ValueError:
    print("Semua input harus berupa angka")