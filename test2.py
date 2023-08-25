Menu = ['1. Report Data Siswa',
        '2. Menambahkan Data Siswa',
        '3. Mengubah Data Siswa',
        '4. Menghapus Data Siswa',
        '5. Exit']

Kontak = [
    {
        'Nama': 'Evan',
        'Gender': 'Pria',
        'Telp' : '+621255881149',
        'Email' : 'christopherevan2307@hotmail.com',
        'Kota' : 'Surabaya',
        'Alamat': 'Jalan Surabaya No 1'
    },
    {
        'Nama': 'Jason',
        'Gender': 'Pria',
        'Telp' : '+6281269692122',
        'Email': 'Jason@gmail.com',
        'Kota' : 'Surabaya',
        'Alamat': 'Jalan Kamboja No 5'
    }
]


def Main_Menu():
    Opsi = 5

    while (Opsi != '5'):
        print("\n==========Data Record Siswa Purwadhika=============\n")
        for i in Menu:
            print(i)
        Opsi = input("Silakan Pilih Main_Menu [1-5] : ")
        if Opsi == '1':
            Read_Data()
        elif Opsi == '2':
            Create_Data()
        elif Opsi == '3':
            Update_Data()
        elif Opsi == '4':
            Delete_Data()
        elif Opsi == '5':
            print('Thank you and Good Bye!!!')
            quit()
        else:
            print("*Pilihan yang anda Masukkan Salah** \n")

def Read_Data():
    read = True
    while read != '3':
        print("\n++++++Data Nomer Telepon+++++\n")
        print("1.Report Seluruh Data")
        print("2.Report Data Tertentu")
        print("3.Kembali ke Menu Utama")
        read = input("Silahkan Pilih Sub Menu Read Data [1-3] :")
        if read == '1':
            if len(Kontak) != 0:
                print(Kontak)
        
        if read == '2':
            telpon = input("Masukkan no telpon yang ingin dicari: ")
            print(telpon)
            for i in range(len(Kontak)):
                if Kontak[i]['Telp'] == telpon:
                     print (Kontak[i])

        if read == '3':
            Main_Menu()
        
        else: 
            print("\n*Pilihan yang anda Masukan Salah*")
            Read_Data()
                               
def Create_Data():
     create = True
     while create != '3':
        print('\n++++Data Nomer Telepon+++\n')
        print("1.Report Seluruh Data")
        print("2.Menambahkan Data") 
        print("3.Kembali ke Menu Utama") 
        read = input("Silahkan Pilih Sub Menu Read Data [1-3] :")
        if read == '1':
            if len(Kontak) != 0:
                print(Kontak)
        if read == '2':
            telpon = input("Masukkan no telpon yang ingin dicari: ")
            print(telpon)
            for i in Kontak:
                if i['Telp']== telpon:  # same "key": merge
                 new_list = {'Nama': input(),
                             'Telp': input(),
                             'Alamat': input()
                             }
                 print(new_list)

        if read == '3':
            Main_Menu()    
        else: 
            print("\n*Pilihan yang anda Masukan Salah*")
            Read_Data()    

def Update_Data():
    update = True
    while update != '3':
        print("\n+++++Data Nomer Telepon+++++\n")
        print("1.Report Seluruh Data")
        print("2.Memperbaharui Data")
        print("3.Kembali ke Menu Utama")
        read = input("Silahkan Pilih Sub Menu Read Data [1-3] :")
        if read == '1':
            if len(Kontak) != 0:
                print(Kontak)
        if read == '2':
            telpon = input("Masukkan no telpon yang ingin dicari: ")
            print(telpon)
            if len(Kontak)!= 0:
                input("Masukan Nama Baru: ")
                input("Masukan Telpon Baru: ")
                input("Masukan Alamat baru: ")
            
            
        if read == '3':
            Main_Menu()
        else: 
            print("\n*Pilihan yang anda Masukan Salah*")
            Read_Data()

def Delete_Data():
    delete = True
    while delete != '3':
        print("1.Report Seluruh Data")
        print("2.Menghapus Data")
        print("3.Kembali ke Menu Utama")
        read = input("Silahkan Pilih Sub Menu Read Data [1-3] :")
        if read == '1':
            print(Kontak) 
        if read == '2':
             telpon = input("Masukkan no telpon yang ingin dicari: ")
             print(telpon)
             for i in (Kontak):
                if Kontak[i]['Telp'] == telpon:
                    Kontak.remove(i)
                    break
        if read == '3':
            Main_Menu()
        else: 
            print("\n*Pilihan yang anda Masukan Salah*")
            Delete_Data()

Main_Menu()