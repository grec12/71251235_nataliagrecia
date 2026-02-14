x = int(input("Masukkan nilai x: "))

if x == 0:
    print("Error: x tidak boleh 0 karena akan menyebabkan pembagian dengan nol.")
else:
    f_x = 2 * x**3 + 2 * x + (15 / x)

    print(f"Hasil f({x}) = {f_x:.2f}")
