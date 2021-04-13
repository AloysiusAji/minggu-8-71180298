#Aloysius Gonzaga Ardhian Krisna Aji
#71180298

# Membuat program inputan biodata yang berisi nama, alamat, jenis kelamin, hobi.
# Namun untuk merahasiakan nya kamu membuat inputan tersebut berubah menjadi panjang setiap karakter.

# input 
# nama, alamat, jenis kelamin, hobi 

# output
# angka (panjang karakternya)

f = open("Biodata.txt","w")

masukan = input("Masukan Nama: ")
masukana = input("Masukan Alamat: ")
masukanb = input("Masukan Jenis Kelamin(Pria / Wanita): ")
masukanc = input("Masukan Hobi: ")

f.write("Nama:")
berubah = str(len(masukan))
f.write(str(berubah))
f.write("\n")
f.write("Alamat:")
berubaha = str(len(masukana))
f.write(str(berubaha))
f.write("\n")
f.write("Jenis Kelamin (Pria / Wanita):")
berubahb = str(len(masukanb))
f.write(str(berubahb))
f.write("\n")
f.write("Hobi:")
berubahc = str(len(masukanc))
f.write(str(berubahc))
f.write("\n")
f.close()

