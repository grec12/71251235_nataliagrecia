def kombinasi(n, s):
    if s == 0 or s == n:
        return 1
    else:
        return kombinasi(n - 1, s - 1) + kombinasi(n - 1, s)
    
v = int(input("Masukkan nilai v: "))
t = int(input("Masukkan nilai t: "))
hasil = kombinasi(v, t)
print(f"Hasil Kombinasinya adalah {hasil}")


