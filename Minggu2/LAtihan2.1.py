def hitung_berat_badan(tinggi, bmi_target):
    berat_diperlukan = bmi_target * (tinggi ** 2)
    return berat_diperlukan

tinggi = float(input("Masukkan tinggi badan (cm): ")) / 100
bmi_target = float(input("Masukkan nilai BMI yang diharapkan: "))

berat_diperlukan = hitung_berat_badan(tinggi, bmi_target)

print(f"Berat badan yang diperlukan agar mencapai BMI {bmi_target} adalah {berat_diperlukan: .2f} kg")
