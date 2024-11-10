# Muhammad Raihan Ananditha
# Kelas 1B RPL
# NIM 2403360

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range (n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

N = input("Masukkan jumlah angka fibonacci: ")

if N.isdigit():
    N = int(N)
    if N <= 0:
        print("Silahkan masukkan angka positif")
    else:
        result = fibonacci(N)
        print("Deret fibonacci", result)
else: 
    print("Masukin angka bulat yaa, jangan yang lain.")