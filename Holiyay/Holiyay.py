import csv

def sign_up():
    global username
    print("\n============================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print("============================")
    file = open("data_base.txt", "a")
    file.write(f"{username}:{password}\n")
    print(f"{'Sign up berhasil!':^28}\n")

#==========================================================================================

def sign_in():
    global username
    print("\n============================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print("============================")
    file = open("data_base.txt", "r")
    lines = file.readlines()
    for line in lines:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            print(f"{'Sign in berhasil!':^28}")
            lama_libur()
            return
    print("\nUsername atau password salah.")
    sign_in()
        

#==========================================================================================

def keluar():
     print("Terima Kasih sudah menggunakan Holiyay")
     exit()

#==========================================================================================

def get_filtered_tempat_wisata_dan_hotel(cek_total_harga):
    global tempat_wisata_dan_hotel_dict
    global tempat_wisata_list
    global hotel_list
    global filtered_tempat_wisata_list
    global filtered_hotel_list

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
    global jenis_pembayaran
    jenis_pembayaran = (input("Masukkan jenis bank (1/2/3): "))

    while jenis_pembayaran not in ["1", "2", "3"]:
        print("Jenis bank yang Anda masukkan tidak valid. Silakan coba lagi.")
        jenis_pembayaran = (input("Masukkan jenis bank (1/2/3): "))    

#==========================================================================================

def pilih_pemandu():
    print('''
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

    global pemandu_dict
    global pemandu_terpilih
    global harga_pemandu

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

    # print("Selamat! Pilihan Anda telah berhasil disimpan\n")

    pemandu_dict["pemandu_terpilih"] = pemandu_terpilih
    pemandu_dict["harga_pemandu"] = harga_pemandu

    return pemandu_dict
    
#==========================================================================================

def cetak_struk_holiyay(
        username, tempat_wisata, harga_tempat_wisata, hotel_pilihan, 
        harga_per_malam, hari, pemandu_terpilih, harga_pemandu, harga_total, input_biaya):
    print("="*50)
    print(f"|          {'STRUK HOLIYAY':^25}             |")
    print("="*50)
    print(f"| Username            : {username:^25}|")
    print(f"| Tempat Wisata       : {tempat_wisata:^25}|",)
    print(f"| Harga Tempat Wisata : {harga_tempat_wisata:^25}|")
    print(f"| Nama Hotel          : {hotel_pilihan:^25}|")
    print(f"| Harga per Malam     : {harga_per_malam:^25}|")
    print(f"| Jumlah hari         : {hari:^25}|")
    print(f"| Tour Guide          : {pemandu_terpilih:^25}|")
    print(f"| Harga Tour Guide    : {harga_pemandu:^25}|")
    print("-"*50)
    print(f"| Total Biaya         : {harga_total:^25}|")
    print(f"| Biaya yang dibayar  : {input_biaya:^25}|")
    print("="*50)
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
            global hari
            hari = int(input("Silakan memilih berapa lama waktu berwisata (2/3/4): "))
            if hari not in [2, 3, 4]:
                raise ValueError("Pilihan jumlah hari yang dimasukkan tidak valid, silakan memilih jumlah hari 2, 3, atau 4.")
            break
        except ValueError as e:
            print("\n==========================================================================================")
            print(f"{'#404 Not Found#':^85}") 
            print(f"{str(e):^85}")
            print("==========================================================================================")
    global cek_total_harga
    cek_total_harga = None

    global kategori_budget
    global total_harga

    if hari == 2:
            print(
    '''\nSilahkan memilih rentang budget:
        1. Kurang dari Rp 600.000,-
        2. Lebih dari Rp 600.000,-''')
            print("\n===========================================")
            kategori_budget = int(input("masukkan jumlah nominal budget anda (1/2): "))
            print("===========================================\n")
            if kategori_budget == 1:
                cek_total_harga = lambda total_harga: total_harga < 400000
            elif kategori_budget == 2:
                cek_total_harga = lambda total_harga: total_harga > 400000
            else:
                lama_libur()

    elif hari == 3:
            print(
    '''\nSilahkan memilih rentang budget:
        1. Kurang dari Rp 800.000,-
        2. Lebih dari Rp 800.000,-''')
            print("\n===========================================")
            kategori_budget = int(input("masukkan jumlah nominal budget anda (1/2): "))
            print("===========================================\n")
            if kategori_budget == 1:
                cek_total_harga = lambda total_harga: total_harga < 400000
            elif kategori_budget == 2:
                cek_total_harga = lambda total_harga: total_harga > 400000
            else:
                lama_libur()

    elif hari == 4:
            print(
    '''\nSilahkan memilih rentang budget:
        1. Kurang dari Rp 1.000.000,-
        2. Lebih dari Rp 1.000.000,-''')
            print("\n==========================================")
            kategori_budget = int(input("masukkan jumlah nominal budget anda (1/2): "))
            print("==========================================\n")
            if kategori_budget == 1:
                cek_total_harga = lambda total_harga: total_harga < 400000
            elif kategori_budget == 2:
                cek_total_harga = lambda total_harga: total_harga > 400000
            else:
                lama_libur()

    tempat_wisata_dan_hotel_dict = get_filtered_tempat_wisata_dan_hotel(cek_total_harga)
    tempat_wisata_list = tempat_wisata_dan_hotel_dict["tempat_wisata"]
    hotel_list = tempat_wisata_dan_hotel_dict["hotel"]

    print("\nberikut tempat wisata yang dapat anda pilih")
    print("="*77)
    for tempat_wisata in tempat_wisata_list:
            print(f"{tempat_wisata[1]:^53} | {tempat_wisata[0]:^8} | {tempat_wisata[2]:^8} |")
            print("="*77)
    print("\nberikut tempat penginapan yang dapat anda pilih")
    print("="*61)
    for hotel in hotel_list:
            print(f"| {hotel[1]:^35} | {hotel[0]:^8} | {hotel[2]:^8} |")
            print("="*61)
    memilih()

def memilih():
    input_tempat_wisata = input("\nsilahkan memilih tempat wisata: ")
    input_hotel = input("silahkan memilih tempat penginapan: ")
    print("="*50)

    total_harga = 0

    for tempat_wisata in tempat_wisata_list:
        if tempat_wisata[1].lower() == input_tempat_wisata.lower():
            harga_tempat_wisata = int(tempat_wisata[0])
            total_harga += harga_tempat_wisata
            tempat_wisata_pilihan = tempat_wisata[1]
            break
    else:
        print("Input anda tidak valid")
        memilih()
            

    for hotel in hotel_list:
        if hotel[1].lower() == input_hotel.lower():
            harga_per_malam = int(hotel[0])
            total_harga += harga_per_malam*hari
            hotel_pilihan = hotel[1]
            break
    else:
         print("input anda tidak valid")
         memilih()

    global pemandu_dict
    pemandu_dict = pilih_pemandu()        
    total_harga += pemandu_dict["harga_pemandu"]
    print("\n============================================================")
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
                    print()
                    cetak_struk_holiyay(
                        username, tempat_wisata_pilihan, harga_tempat_wisata, hotel_pilihan, harga_per_malam, hari,
                        pemandu_dict["pemandu_terpilih"], pemandu_dict["harga_pemandu"],
                        total_harga, input_biaya)
                    exit()
        elif konfirmasi_pembayaran.lower() == "tidak":
                    print(
            '''\nSilakan memilih opsi:
                1. Menu Awal
                2. Pilih Wisata dan Penginapan
                3. Keluar''')
                    kembali = input("\nMasukkan pilihan anda (1/2/3): ")
                    if kembali == "1":
                        menu_awal()                
                    elif kembali == "2":
                        lama_libur()
                    else:
                        keluar()
   

#==========================================================================================

def menu_awal():
    print(
'''Selamat datang di Holiyay!
Program ini akan membantu anda untuk memilih penginapan, tempat wisata, dan pemandu wisata :)''')
    print("⋆˚✿˖°⋆˚✿˖°⋆˚✿˖°⋆˚✿˖° ପ(๑•ᴗ•๑)ଓ ♡⋆˚✿˖°⋆˚✿˖°⋆˚✿˖°⋆˚✿˖°")
    print("  /)  /)")
    print("( ᵔ ᵕ ᵔ )")
    print("/ づ  づ ~ ♡")
    while True:
        try:
            print(
'''\nSilakan memilih opsi:
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
                raise ValueError("Pilihan yang dimasukkan tidak valid, silakan pilih 1, 2, atau 3.")        
        except ValueError as e:
            print("\n===============================================================")
            print(f"{'#Kesalahan pada akun anda atau kesalahan input#':^60}")
            print(f"{str(e):^60}")
            print("===============================================================")
            continue

menu_awal()