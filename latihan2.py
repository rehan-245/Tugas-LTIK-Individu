# Muhammad Raihan Ananditha
# Kelas 1B RPL
# NIM 2403360

def HitungTotalDanRataRata(*angka):
    total = sum(angka)
    ratarata = total / len(angka)
    return total, ratarata

input_angka = input("Masukkan angka: ")
nilai_list = list(map(float, input_angka.split(',')))
total, ratarata = HitungTotalDanRataRata(*nilai_list)

print(f"Total: {total}")
print(f"Rata-rata: {ratarata}")
    