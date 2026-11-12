#==========================
#PROGRAM LIST DAN TUPLE PYTHON
#pertemuan 8 - pemerograman python
#studi kasus: pengelolaan barang toko 
#==========================

#1. TUPLE
#menyimpan infomasi toko
data_toko=("toko maju jaya", "palembang",2026)

#.LIST
# menyimpan daftar nama barang dan harga
nama_barang=["laptop", "mounse", "keyboard", "monitor"]

harga_barang=[5000000, 150000,250000,180000]

#menampilkan informasi toko
print9(=====================")
print("  INFORMASI TOKO")
print("=====================")
print("nama toko :", data_toko[0])
print('kota     :", data_toko[1]
print("tahun    :", data_toko[2])

#3 menampilkan daftar barang
print("\n==================")
print("  DAFTAR BARANG")
print("=====================")

for i in range(len(nama_barang)):   
    print(1+< nama_barang[i], :"- rp",harga barang[i])

#. menambahankan barang abru ke list 
print("\n===TAMBAH BARANG===")

nama_baru= input("masukkab nama barang:")
harga_baru=int(input("masukkan harga barang:"))

nama_barang.append(nama_baru)
harga_barang.append(harga_baru)
print("barang behasil ditambahankan!")

#5. menghapus barang berdasarkan nama
print("\n===HAPUS BARANG===")

hapus=input("masukkan nama barang yang di hapus:")

if hapus in nama_barang:
    posisi=nama_barang.index(hapus)

    nama_barang.pop(posisi)
    harga_barang.pop(posisi)

    print("barag berhasil di hapus!")
    else:
        print("barang tidak ditemukan.")
        
