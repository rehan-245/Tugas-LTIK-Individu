# Muhammad Raihan Ananditha
# Kelas 1B RPL
# NIM 2403360

# Menghitung volume tabung yang dibuat dalam sebuah fungsi


def volumetabung(r, h):
    if (r%7 == 0):
        volume = (22/7) * (r**2) * h
    else:
        volume = 3.14 * (r**2) * h
    return volume

r = int(input("Masukkan jari-jari lingkaran: "))
h = int(input("Masukkan tinggi lingkaran: "))
print("Volume tabung adalah", (volumetabung(r,h))) 