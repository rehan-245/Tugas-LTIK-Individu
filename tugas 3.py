def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
 
    selisih_detik = total_detik_selesai - total_detik_mulai
    
    jam = selisih_detik // 3600
    menit = (selisih_detik % 3600) // 60
    detik = selisih_detik % 60
    return jam, menit, detik

jam_mulai = int(input("Input mulai:\nJam: "))
menit_mulai = int(input("Menit: "))
detik_mulai = int(input("Detik: "))

jam_selesai = int(input("Input selesai:\nJam: "))
menit_selesai = int(input("Menit: "))
detik_selesai = int(input("Detik: "))

jam, menit, detik = hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)

print(f"Hitung selisih:\nOutput: {jam} jam - {menit} menit - {detik} detik")
