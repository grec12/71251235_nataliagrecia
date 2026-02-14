gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

pendapatan_kotor = gaji_per_jam * jam_per_minggu * 4

pajak = pendapatan_kotor * 0.14
pendapatan_bersih = pendapatan_kotor - pajak

biaya_pakaian = pendapatan_bersih * 0.10
biaya_alat_tulis = pendapatan_bersih * 0.01

sisa_uang = pendapatan_bersih - (biaya_pakaian + biaya_alat_tulis)

sedekah = sisa_uang * 0.25
anak_yatim = sedekah * 0.30
kaum_dhuafa = sedekah * 0.70

print("\nHasil Perhitungan Keuzngan Budi: ")
print(f"1. Pendapatan sebelum pajak: Rp{pendapatan_kotor:,.2f}")
print(f"2. Pendapatan setelah pajak: Rp{pendapatan_bersih:,.2f}")
print(f"3. Biaya pakaian dan aksesoris: Rp{biaya_pakaian:,.2f}")
print(f"4. Biaya alat tulis: Rp{biaya_alat_tulis:,.2f}")
print(f"5. Totalsedekah: Rp{sedekah:,.2f}")
print(f"6. Uang untuk anak yatim: Rp{anak_yatim:,.2f}")
print(f"7. Uang unutk kaum dhuafa: Rp{kaum_dhuafa:,.2f}")
