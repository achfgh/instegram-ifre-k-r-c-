import random
import string
import time
print("Şifre kırıcı HECK")
print("[01] Instagram")
print("[02] Facebook")
print("[03] YoTube (E-posta zorunlu)")
input("E-POSYTA YADA KULANICI ADI GİRİN: ")
input("Lütfen secimçim yap")
print("lütfen uzun bir süre bekleyin")
print("LOADİNG....")
print("HECK...")
print("LOADİNG....")
print("BEKLEYİN")
def rastgele_sifre_uret(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

def dosyayaz(dosya_adi="Heck.txt"):
    try:
        with open(dosya_adi, "a") as dosya:
            while True:
                for _ in range(20000):
                    yeni_sifre = rastgele_sifre_uret()
                    dosya.write(yeni_sifre + "\n")
                print(f"Dosyaya 20000 yeni şifre yazıldı. Dosya adı: {dosya_adi}")
                time.sleep(1) # Saniyede bir toplu yazma işlemi yapar
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    print("Rastgele şifreler üretilip 'sifreler.txt' dosyasına yazılıyor (sonsuza kadar sürebilir!).")
    print("Durdurmak için Ctrl+C tuşlarına basabilirsiniz.")
    dosyayaz()
