# Muhammad Raihan Ananditha
# Kelas 1B RPL
# NIM 2403360

def login():
    PasswordBenar = "Latihan"
    kesempatan = 3
    while kesempatan > 0 :
        username = input("Silahkan Login\nMasukkan Username: ")
        password = input("Masukkan Password: ")
        if password == PasswordBenar:
            print("Selamat, login telah berhasil")
            return
        else:
            kesempatan -= 1
            print(f"Password salah, Anda memiliki {kesempatan} kesempatan tersisa")

        print("Anda telah memasukkan password yang salah berkali-kali, keluar dari menu login")

login()