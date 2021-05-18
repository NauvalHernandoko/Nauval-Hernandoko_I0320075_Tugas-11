# Mengimport modul geometri2D
from matematika import Geometri2D

#persegi panjang
p = 10
l = 8
luas = Geometri2D.luasPersegiPanjang(p, l)
kel = Geometri2D.kelilingPersegiPanjang(p, l)
print("PERSEGI PANJANG")
print("Panjang\t:", p)
print("lebar\t:", l)
print("Luas\t:", luas)
print("Keliling\t=", kel)
#lingkaran
jarijari = 3
luas = Geometri2D.luasLingkaran(jarijari)
kel = Geometri2D.kelilingLingkaran(jarijari)
print("\nLINGKARAN")
print("jari-jari\t:", jarijari)
print("Luas\t:", luas)
print("Keliling\t:", kel)