from os import system
       
def menu () :
    system('cls')
    print('|===================================================|')
    print('|                PROGRAM KALKULATOR                 |')
    print('|===================================================|')
    print('|                1. JUMLAH                          |') 
    print('|                2. KALI                            |') 
    print("|                3. PENGURANGAN                     |")
    print("|                4. PEMBAGIAN                       |")    
    print('|===================================================|')
    print('*KETIK 5 UNTUK KELUAR')
    print('---------------------------------------------------') 
    menupilih = (input('Pilih Menu  : '))
    
    if menupilih == '1'   :
        Jumlah ()
    elif menupilih == '2' :
        Kali ()
    elif menupilih == '3' :
        pengurangan ()
    elif menupilih == '4' :
        pembagian ()        
    elif menupilih == '5' :
        exit ()
    else:
     system('cls')
     menu ()

def Jumlah () :
    x = int (input('Masukan Angka Pertama : ')) 
    y = int (input('Masukan Angka Kedua : '))

    z = x + y 
    print (f'Hasil {z}')
    kembali = input('Hapus tekan [enter]')
    menu  ()
    Jumlah ()

def Kali () :
    x = int (input('Masukan Angka Pertama : ')) 
    y = int (input('Masukan Angka Kedua : '))

    z = x * y 
    print (f'Hasil {z}')
    kembali = input('Hapus tekan [enter]')
    menu ()
    Kali  ()

def pengurangan () :
    x = int (input('Masukan Angka Pertama : ')) 
    y = int (input('Masukan Angka Kedua : '))

    z = x - y 
    print (f'Hasil {z}')
    kembali = input('Hapus tekan [enter]')
    menu ()
    pengurangan () 

def pembagian () :
    x = int (input('Masukan Angka Pertama : ')) 
    y = int (input('Masukan Angka Kedua : '))

    z = x / y 
    print (f'Hasil {z}')
    kembali = input('Hapus tekan [enter]')
    menu ()
    pembagian ()  
                   
menu () 