try:
    suhu = float(input("Masukkan suhu tubuh: "))
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except ValueError:
    print("Input tidak valid! harap masukkan sngka suhu dengan benar")