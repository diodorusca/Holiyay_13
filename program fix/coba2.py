import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def sign_up():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print("Sign up berhasil!")

#==========================================================================================

def sign_in():
        global username
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        file = open("data_base.txt", "r")
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("Sign in berhasil!")
                return
            else:
                break
        sign_in()

#==========================================================================================

def keluar():
     print("Terima Kasih sudah menggunakan Holiyay")
     exit()

#==========================================================================================

def get_filtered_tempat_wisata_dan_hotel(cek_total_harga):
    tempat_wisata_dan_hotel_dict = {}
    tempat_wisata_list = []
    hotel_list = []
    filtered_tempat_wisata_list = []
    filtered_hotel_list = []

    with open("tempat_wisata.txt", "r") as file:
        tempat_wisata_reader = csv.reader(file, delimiter=',')
        next(tempat_wisata_reader)

        for row in tempat_wisata_reader:
            tempat_wisata_list.append(row)

    with open("hotel.txt", "r") as file:
        hotel_reader = csv.reader(file, delimiter=',')
        next(hotel_reader)

        for row in hotel_reader:
            hotel_list.append(row)

    tempat_wisata_list.sort(key=lambda element: int(element[0]))
    hotel_list.sort(key=lambda element: int(element[0]))

    for tempat_wisata in tempat_wisata_list:
        for hotel in hotel_list:
            if cek_total_harga(int(tempat_wisata[0]) + int(hotel[0])):
                if not tempat_wisata in filtered_tempat_wisata_list:
                    filtered_tempat_wisata_list.append(tempat_wisata)
                
                if not hotel in filtered_hotel_list:
                    filtered_hotel_list.append(hotel)
            else:
                if int(hotel[0]) > int(tempat_wisata[0]):
                    if hotel in filtered_hotel_list:
                        filtered_hotel_list.remove(hotel)
                else:
                    if tempat_wisata in filtered_tempat_wisata_list:
                        filtered_tempat_wisata_list.remove(tempat_wisata)

    tempat_wisata_dan_hotel_dict ["tempat_wisata"] = filtered_tempat_wisata_list
    tempat_wisata_dan_hotel_dict ["hotel"] = filtered_hotel_list

    return tempat_wisata_dan_hotel_dict

#==========================================================================================

def bank():
    print('''\nSilahkan memilih jenis bank:
            1. Bank BRI
            2. Bank BCA
            3. Bank Mandiri''')
    jenis_pembayaran = int(input("Masukkan jenis bank (1/2/3): "))
    

#==========================================================================================

def pilih_pemandu():
    print('''
Selamat datang di program pemilihan pemandu wisata!
✿ ♡＾▽ ＾♡ ✿
Disini anda akan diminta memilih salah satu pemandu wisata selama berada di Bali
Silahkan pilih pemandu Anda:
1.  Pemandu A
    Berikut Kriteria Pemandu A :
    1. Memiliki kemampuan 2 bahasa asing (bahasa inggris dan bahasa Italia)
    2. Sudah pernah menjelajahi keseluruhan Pulau Bali
    3. Mengetahui tempat kuliner yang enak di Bali
    4. Biaya Tourguide A adalah Rp 100.000,-

2.  Pemandu B
    Berikut Kriteria Pemandu B :
    1. Fasih dalam berbahasa daerah Bali
    2. Mengetahui sejarah dan adat istiadat Bali
    3. Tahu tempat diving yang bagus di Bali
    4. Biaya Tourguide B adalah Rp 80.000,-

3.  Pemandu C
    Berikut Kriteria Pemandu C :
    1. Menguasai 3 jenis bahasa asing (bahasa inggris, bahasa chinese, bahasa spanyol)
    2. Sudah kenal dekat dengan beberapa pemiliki wisata di Bali
    3. Tahu tempat berbelanja oleh-oleh di Bali
    4. Biaya Tourguide C adalah Rp 120.000,-

4.  Tidak menggunakan pemandu wisata''')

    pemandu_dict = {}
    pemandu_terpilih = None
    harga_pemandu = None

    while pemandu_terpilih is None:
        pilihan = input("\nMasukkan pilihan Anda (1/2/3/4): ")

        if pilihan == "1":
            print("Anda memilih pemandu A.")
            pemandu_terpilih = "A"
            harga_pemandu = 100000

        elif pilihan == "2":
            print("Anda memilih pemandu B.")
            pemandu_terpilih = "B"
            harga_pemandu = 80000
            
        elif pilihan == "3":
            print("Anda memilih pemandu C.")
            pemandu_terpilih = "C"
            harga_pemandu = 120000

        elif pilihan =="4":
            print("Anda tidak menggunakan jasa pemandu wisata")
            pemandu_terpilih = "tanpa pemandu"
            harga_pemandu = 0
           
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")

    print("Selamat! Pilihan Anda telah berhasil disimpan\n")

    pemandu_dict["pemandu_terpilih"] = pemandu_terpilih
    pemandu_dict["harga_pemandu"] = harga_pemandu

    return pemandu_dict
    
#==========================================================================================

def cetak_struk_holiyay(
        username, tempat_wisata, harga_tempat_wisata, hotel_pilihan, 
        harga_per_malam, hari, pemandu_terpilih, harga_pemandu, harga_total, input_biaya):
    print("="*35)
    print("          STRUK HOLIYAY             ")
    print("="*35)
    print("Username            : ", username)
    print("Tempat Wisata       : ", tempat_wisata)
    print("Harga Tempat Wisata : ", harga_tempat_wisata)
    print("Nama Hotel          : ", hotel_pilihan)
    print("Harga per Malam     : ", harga_per_malam)
    print("Jumlah hari         : ", hari)
    print("Tour Guide          : ", pemandu_terpilih)
    print("Harga Tour Guide    : ", harga_pemandu)
    print("-"*35)
    print("Total Biaya         : ", harga_total)
    print("Biaya yang dibayar  : ", input_biaya)
    print("="*35)
    print("\nTerima kasih sudah menggunakan program Holiyay")

#==========================================================================================

def lama_libur():
    while True:
        try:
            print(
    '''\nSilakan memilih jumlah hari:
    2 hari
    3 hari
    4 hari''')
            hari = int(input("Silakan memilih berapa lama waktu berwisata (2/3/4): "))
            if hari not in [2, 3, 4]:
                raise ValueError("\nPilihan jumlah hari yang dimasukkan tidak valid, silakan memilih jumlah hari 2, 3, atau 4.")
            break
        except ValueError as e:
            print("#404 Not Found#", str(e))

    cek_total_harga = None

    if hari == 2:
            print(
    '''Silahkan memilih rentang budget:
        1. Kurang dari Rp 600.000,-
        2. Lebih dari Rp 600.000,-''')
            kategori_budget = int(input("masukkan jumlah nominal budget anda (1/2): "))
            if kategori_budget == 1:
                cek_total_harga = lambda total_harga: total_harga < 400000
            elif kategori_budget == 2:
                cek_total_harga = lambda total_harga: total_harga > 400000
    elif hari == 3:
            print(
    '''Silahkan memilih rentang budget:
        1. Kurang dari Rp 800.000,-
        2. Lebih dari Rp 800.000,-''')
            kategori_budget = int(input("masukkan jumlah nominal budget anda (1/2): "))
            
            if kategori_budget == 1:
                cek_total_harga = lambda total_harga: total_harga < 400000
            elif kategori_budget == 2:
                cek_total_harga = lambda total_harga: total_harga > 400000
    elif hari == 4:
            print(
    '''Silahkan memilih rentang budget:
        1. Kurang dari Rp 1.000.000,-
        2. Lebih dari Rp 1.000.000,-''')
            kategori_budget = int(input("masukkan jumlah nominal budget anda (1/2): "))
            if kategori_budget == 1:
                cek_total_harga = lambda total_harga: total_harga < 400000
            elif kategori_budget == 2:
                cek_total_harga = lambda total_harga: total_harga > 400000

    tempat_wisata_dan_hotel_dict = get_filtered_tempat_wisata_dan_hotel(cek_total_harga)
    tempat_wisata_list = tempat_wisata_dan_hotel_dict["tempat_wisata"]
    hotel_list = tempat_wisata_dan_hotel_dict["hotel"]

    print("\n\nberikut tempat wisata yang dapat anda pilih\n")
    for tempat_wisata in tempat_wisata_list:
            print(f"{tempat_wisata[1]} | {tempat_wisata[0]} | {tempat_wisata[2]}")
            print("="*70)
    print("\nberikut tempat penginapan yang dapat anda pilih\n")
    for hotel in hotel_list:
            print(f"{hotel[1]} | {hotel[0]} | {hotel[2]}")
            print("="*70)

    input_tempat_wisata = input("\nsilahkan memilih tempat wisata: ")
    input_hotel = input("silahkan memilih tepat penginapan: ")

    pemandu_dict = pilih_pemandu()

    total_harga = 0

    for tempat_wisata in tempat_wisata_list:
            if tempat_wisata[1].lower() == input_tempat_wisata.lower():
                harga_tempat_wisata = int(tempat_wisata[0])
                total_harga += harga_tempat_wisata
                tempat_wisata_pilihan = tempat_wisata[1]
                break

    for hotel in hotel_list:
            if hotel[1].lower() == input_hotel.lower():
                harga_per_malam = int(hotel[0])
                total_harga += harga_per_malam*hari
                hotel_pilihan = hotel[1]
                break

    total_harga += pemandu_dict["harga_pemandu"]
    print("="*60)
    print("Total harga (tempat wisata, hotel, dan pemandu): ", total_harga)
    print("="*60)

    bank()

    while True:
            try:
                input_biaya = int(input("Masukkan biaya dengan nominal pas: "))
            
            # Lanjutkan dengan program selanjutnya
                if input_biaya == total_harga:
                    break
                elif input_biaya > total_harga:
                    raise ValueError(f"Nominal yang dimasukkan lebih dari total harga, silakan memasukkan nominal {total_harga}.")
                elif input_biaya < total_harga:
                    raise ValueError(f"Nominal yang dimasukkan kurang dari total harga, silakan memasukkan nominal {total_harga}.")
            
            except ValueError as e:
                print("Kesalahan Jumlah biaya\n",str(e))
    konfirmasi_pembayaran = input("Apakah Anda setuju dengan pembayaran tersebut? (ya/tidak) ")

    while True:
        if konfirmasi_pembayaran.lower() == "ya":
                    cetak_struk_holiyay(
                        username, tempat_wisata_pilihan, harga_tempat_wisata, hotel_pilihan, harga_per_malam, hari,
                        pemandu_dict["pemandu_terpilih"], pemandu_dict["harga_pemandu"],
                        total_harga, input_biaya)
                    break
        elif konfirmasi_pembayaran.lower() == "tidak":
                    print(
            '''\nSilakan memilih opsi:
                1. Menu Awal
                2. Keluar''')
                    kembali = input("\nMasukkan pilihan anda (1/2): ")
                    if kembali == "1":
                        menu_awal()                
                    else:
                        keluar()
   

#==========================================================================================

def menu_awal():
    print("Selamat datang di Holiyay!")
    while True:
        try:
            print(
'''Silakan memilih opsi:
1. Sign up
2. Sign in
3. Keluar''')
            pilih = input("Masukkan pilihan (1/2/3): ")
            if pilih == "1":
                sign_up()
                menu_awal()
            elif pilih == "2":
                sign_in()
                lama_libur()
                break
            elif pilih == "3":
                 keluar()
            else:
                raise ValueError("Pilihan yang dimasukkan tidak valid, silakan pilih 1 atau 2.")        
        except ValueError as e:
            print("#Kesalahan pada akun anda atau kesalahan input#\n", str(e))
            continue
menu_awal()