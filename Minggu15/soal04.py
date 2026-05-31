def jumlah_digit(n):
    if n < 10:
        return n 
    else:
        return n % 10 + jumlah_digit(n // 10)
    
try:
    bilangan = int(input("Masukkan bilangan: "))
    hasil = jumlah_digit(bilangan)
    print(f"Jumah digit dari {bilangan} adalah {hasil}")
except ValueError:
    print("Masukkan bilangan bulat yang valid.")

    