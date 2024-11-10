# Contoh function
def penjumlahan(a, b):
    hasil = a + b
    return hasil

penjumlahan(2, 3)

# Contoh procedure
def greeting(nama):
    print(f"Halo, {nama}!")

greeting("Sasa")

# Contoh global variable
globalVar = 10

def globalFunction():
    print(f"Nilai dari global variabel")


def greeting(nama = "Kuro"):
    print(f"Halo, {nama}")

greeting()
greeting("rehan")