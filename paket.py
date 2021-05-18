#mengimpor modul geometri2D
#yang berada di dalam paket matematika
import matematika.Geometri2D
def main():
 #bujur sangkar
 sisi = 5
 luas = matematika.Geometri2D.luasBujursangkar(sisi)
 print("BUJURSANGKAR")
 print("Panjang sisi\t: ", sisi)
 print("Luas\t\t= ", luas)
if __name__ == "__main__":
 main()