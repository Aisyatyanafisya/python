from os import system

d_nama = []
d_jenis = []
d_beli = []
d_kirim = []
d_alamat = []
id_nama = []

def judul():
    print("===============================================")
    print("|    PROGRAM PENDATAAN PEMBELI HEWAN QURBAN   |")
    print("===============================================")

def menu():
    judul()
    print("|                                             |")
    print("|          1. Owner   |   2. Customer         |")
    print("|                                             |")
    print("===============================================")
    print("*Ketik 3 untuk keluar")
    print("-----------------------------------------------")
    menupilih = (input("Pilih Menu Login : "))
    if menupilih == "1":
        owner()
    elif menupilih == "2":
        customer()
    elif menupilih == "3":
        exit()
    else:
        system("cls")
        menu()

#Owner
def owner():
    system("cls")
    print('===============================================')
    print('|                   Login                     |')
    print('===============================================')
    print("Masukkan Password!")
    print("\n")
    kode = input("Password : ")
    if kode == "admin" or kode == "ADMIN":
        menu_owner()
    else:
        salah = input("Password salah!")
        owner()

def menu_owner():
    system("cls")
    print('===============================================')
    print('    Input Data Pembeli    '.center(45))
    print('===============================================')
    print('| 1. Tambah Data Pembeli                      |')
    print('| 2. Lihat Data Pembeli                       |')
    print('| 3. Ubah Data Pembeli                        |')
    print('| 4. Hapus Data Pembeli                       |')
    print('| 5. Selesai                                  |')
    print('===============================================')
    pilih2 = input("Pilih Menu : ")
    if pilih2 == "1":
        tambah()
    elif pilih2 == "2":
        lihat()
    elif pilih2 == "3":
        ubah()
    elif pilih2 == "4":
        hapus()
    elif pilih2 == "5":
        selesai()
    else: 
        tidak = input("Menu Tidak Tersedia")
        system("cls")
        menu_owner()

def tambah():
    system("cls")
    judul()
    file=open("DataKurban.txt","a")
    print("Tambah Data" .center(45))
    print('===============================================')
    
    nama = input("Nama : ")
    jenis = input("Jenis Hewan [Sapi/Kambing/Domba] : ")
    if jenis == "Sapi" or jenis =="sapi":
        j = "Sapi"
    elif jenis == "Kambing" or jenis == "kambing":
        j = "Kambing"
    elif jenis == "Domba" or jenis =="domba":
        j = "Domba"
    else:
        kembali = input("Jenis Tidak Terdeteksi")
        tambah()
    beli = input("Tanggal Pembelian : ")
    kirim = input("Tanggal Pengiriman : ")
    alamat = input("Alamat : ")
    id_nama = str(id(nama))
    
    print("Data Tersimpan".center(40))
    file.writelines([nama.capitalize()," - ", id_nama," - ",jenis," - ",beli," - ",kirim," - ",alamat,"\n"])
    file.close()
    kembali = input("Kembali Tekan [Enter]")
    menu_owner()

def lihat():                                                    #Membuat fungsi untuk melihat data
    system("cls")
    judul()                                                     #Mencetak kembali judul dari def judul()
    file=open("DataKurban.txt","r")                             #Membuka data txt dengan metode read
    data=file.readlines()                                       #Membaca setiap baris isi data
    print("Isi File:")                                          #Mencetak kata "Isis File: " dan dilanjutkan isi filenya
    y = 1
    for i in data:
        print(str(y)+". ",i)
        y+=1
    file.close()                                                #Menutup kembali file
    kembali = input("Kembali Tekan [Enter]")                    #Perintah untuk tekan enter jika ingin kembali ke menu_owner
    menu_owner()                                                #Kembali ke menu owner

def ubah():                                                     #Membuat fungsi untuk mengubah data yang sudah disimpan
    import os
    os.system("cls")
    judul()                                                     #Mencetak kembali judul dari fungsi judul
    
    file=open("DataKurban.txt","r")                             #Membuka kembali file txt dengan metode read
    data = file.readlines()                                     #Perintah untuk membaca setiap baris file
    data.sort()                                                 #Mengurutkan data sesuai abjad A-Z
    
    if(len(data) == 0):                                         #Kondisi jika panjang data == 0 maka perintah 
        print("Data Belum Dimasukkan")                          #yang ada di bawahnya akan berjalan
        print("\nSilakan Masukkan Data terlebih dahulu")
        print("Tekan [Enter] untuk Melanjutkan...")
        input()
        os.system('clear')
        menu_owner()                                            #Kembali ke menu owner
    else:                                                       #Jika panjang data tidak == 0, maka perintah yang
        y = 1                                                   #ada dibawahnya akan berjalan
        print("Daftar Kurban\n")                                #Mencetak kata Daftar Kurban dengan line baru setelahnya
        for i in data:                                          #Jika i atau data yg dimasukan ada pada file
            pembatas = i.split(" - ")                           #perintah dibawahnya akan berjalan dan setiap datanya
            print(str(y)+". ",end="")                           #akan dipisahkan dengan -
            print(pembatas[0])
            y += 1
    file.close()                                                #File akan menutup

    nama = input("Masukkan nama yang akan diedit : ")           #Variabel nama akan memerintah untuk menginput nama yang
                                                                #yang ingin di edit
    file = open("DataKurban.txt")                               #Membuka file txt
    data = file.readlines()                                     #Perintah untuk membaca setiap baris yang ada pada data txt
    index = 0                                                   #Posisi berada di awal atau 0 dengan n = 0
    n = 0
    for i in data:                                              #Jika i atau data ada pada file txt, maka perintah 
        p = i.split(" - ")                                      #akan berjalan dan data dipisahkan dengan -
        if (p[0].lower()).find(nama.lower())+1 >= 1:            #Jika nama yang kita cari ada dalam file, perintah 
            print("\nDATA LAMA")                                #akan mencetak sesuai perintah
            print("ID              : %s" %(p[1]))
            print("Nama Costumer   : %s" %(p[0]))
            print("Jenis Hewan     : %s" %(p[2]))
            print("Tanggal Beli    : %s" %(p[3]))
            print("Tanggal Kirim   : %s" %(p[4]))
            print("Alamat          : %s" %(p[5]))

            confirm = input("Apakah data ini yang akan anda edit (Y/N)? ")         #Variabel untuk mengkonfirmasi apakah 
            if (confirm == "y") or (confirm == "Y"):                               #kita ingin mengudah data atau tidak
                print("\n")                                                        #Jika y maka perintah dibawahnya akan 
                print("1. Nama")                                                   #berjalan
                print("2. Jenis Hewan")
                print("3. Tanggal beli")
                print("4. Tanggal kirim")
                print("5. Alamat")
                print("6. Semua")
                
                pilih_edit = input("Pilih yang ingin anda edit : ").capitalize()   #Variabel untuk menginput pilihan 
                                                                                   #yang ingin kita edit
                if (pilih_edit =='Nama') or (pilih_edit == '1'):                   #Jika memilih angka 1, perintah 
                    print("\nDATA BARU!")                                          #selanjutnya akan berjalan
                    namabaru   = input("Nama Customer : ").capitalize()
                    p[0] = namabaru
                    pg = " - ".join(p)
                    data[index] = pg

                elif (pilih_edit =='Jenis Hewan') or (pilih_edit == '2'):          #Jika memilih angka 2, perintah
                    print("\nDATA BARU!")                                          #selanjutnya akan berjalan
                    jenisbaru   = input("Jenis Hewan (Sapi/Kambing/Domba) : ")
                    p[2] = jenisbaru
                    pg = " - ".join(p)
                    data[index] = pg
            
                elif (pilih_edit =='Tanggal beli') or (pilih_edit == '3'):         #Jika memilih angka 3, perintah
                    print("\nDATA BARU!")                                          #selanjutnya akan berjalan
                    belibaru   = input("Tanggal Beli : ")
                    p[3] = belibaru
                    pg = " - ".join(p)
                    data[index] = pg

                elif (pilih_edit =='Tanggal kirim') or (pilih_edit == '4'):        #Jika memilih angka 4, perintah
                    print("\nDATA BARU!")                                          #selanjutnya akan berjalan
                    kirimbaru   = input("Tanggal Kirim : ").capitalize()
                    p[4] = kirimbaru
                    pg = " - ".join(p)
                    data[index] = pg

                elif (pilih_edit =='Alamat') or (pilih_edit == '5'):               #Jika memilih angka 5, perintah
                    print("\nDATA BARU!")                                          #selanjutnya akan berjalan
                    alamatbaru   = input("Alamat : ").capitalize()
                    p[5] = alamatbaru
                    pg = " - ".join(p)
                    data[index] = pg

                elif (pilih_edit =='Semua') or (pilih_edit == '6'):               #Jika memilih angka 6, perintah
                    print("\nDATA BARU!")                                         #selanjutnya akan berjalan
                    namabaru    = input("Nama Customer : ").capitalize()          #211 kebawah diperintahkan untuk
                    jenisbaru   = input("Jenis Hewan (Sapi/Kambing/Domba : ")     #menginput data yang baru
                    belibaru    = input("Tanggal Beli : ")
                    kirimbaru   = input("Tanggal Kirim : ")
                    alamatbaru  = input("Alamat : ")
                    p[0] = namabaru                                               #P[0 - 5] adalah identitas sesuai
                    p[2] = jenisbaru                                              #dengan variabel nya
                    p[3] = belibaru
                    p[4] = kirimbaru
                    p[5] = alamatbaru+"\n"
                    pg = " - ".join(p)
                    data[index] = pg
                else:                                                             #Selain dari semua pilihan diatas 
                    print("Input anda salah!")                                    #Perintah dibawahnya akan berjalan
                    n += 1
                    print("\nTekan [Enter] untuk Menginput Ulang...")
                    input()
                    os.system('clear')
                    menu_owner()
            n += 1
        index += 1
    if(n == 0):                                         #jika n == 0 maka data tidak ada dan perintah dibawahnya akan
        print("Data tidak ditemukan!")                  #berjalan, dan file akan menutup
    file.close()

    file = open("DataKurban.txt","w")                   #Membuka kembali file txt dengan metode write
    data = file.writelines(data)
    file.close()
    
    print("\nTekan [Enter] untuk Kembali!")
    input()
    os.system('clear')
    menu_owner()                                        #Kembali ke menu owner
    

def hapus():
    system("cls")
    judul()

    print("Hapus Data".center(45))
    print("===============================================")
    nama = input("Masukkan nama yang ingin dihapus : ")
    
    file = open("DataKurban.txt")
    data = file.readlines()
    index = 0
    n = 0

    for i in data:
        p = i.split(" - ")
        if (p[0].lower()).find(nama.lower())+1 >= 1:
            print("\nDATA LAMA")
            print("ID              : %s" %(p[1]))
            print("Nama Costumer   : %s" %(p[0]))
            print("Jenis Hewan     : %s" %(p[2]))
            print("Tanggal Beli    : %s" %(p[3]))
            print("Tanggal Kirim   : %s" %(p[4]))
            print("Alamat          : %s" %(p[5]))

            n += 1

            confirm = input("Apakah anda akan menghapus data ini (Y/N)? ")
            if (confirm == "y") or (confirm == "Y"):
                data.remove(i)
    if n <= 0:
        print("Data tidak ditemukan!")
    file.close()

    file = open("DataKurban.txt","w")
    data = file.writelines(data)
    file.close()

    print("\nTekan [Enter] untuk kembali!")
    input()
    system('clear')
    menu_owner()

def selesai():
    system("cls")
    menu()

#Customer
def customer():
    system("cls")
    judul()
    nama = input("Masukkan nama Anda : ").capitalize()
    file = open("DataKurban.txt")
    data = file.readlines()
    file.close()
    for i in data:
        p = i.split(" - ")
        if (p[0].lower()).find(nama.lower())+1 >= 1:
            print("ID              : %s" %(p[1]))
            print("Nama Costumer   : %s" %(p[0]))
            print("Jenis Hewan     : %s" %(p[2]))
            print("Tanggal Beli    : %s" %(p[3]))
            print("Tanggal Kirim   : %s" %(p[4]))
            print("Alamat          : %s" %(p[5]))
            print("----------------------------------------------------")
        
        file.close()
    print("\nTekan [Enter] untuk Kembali ke Menu Utama!")
    input()
    system("cls")
    selesai()

menu()