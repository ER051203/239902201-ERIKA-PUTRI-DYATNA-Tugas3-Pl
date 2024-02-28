print ("---MEMBACA ANGKA DAN MNCETAK BESAR, KECIL, DAN SEDANG---") 

#cetak angka kurang dari 100 kecil
#cetak angka 101 sampai 199 sedang
#cetak angka lebih dari 200 besar

angka = float (input("Masukan Angka : "))

if angka <100 :
    print ("Kecil")
elif angka >=200 :
    print ("Besar")
else :
    print ("Sedang")


