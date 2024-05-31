
def muk_sayi_bulma(sayi): #mükemmel sayı fonksiyonunu oluşturuyorum
    tam_bolen_sayilar = [] # tam bölen sayıları bir dizide topluyorum
    for i in range(1, sayi): # for döngüsünü oluşturup range ile bir aralık oluşturuyorum
        if sayi % i == 0 : #if koşulunu kullanarak sayısının tam bölenloerini buluyorum
            tam_bolen_sayilar.append(i) #bulduğum tam sayıları append ile diziye atıyorum
    toplam = sum(tam_bolen_sayilar) #bulduğum tam bölenleri topluyorum
    return toplam == sayi #açtığım muk_sayı_bulma fonksiyonundaki sayi değişkenini döndürüyorum

muk_sayilar = [] #mükemmel sayıları tutabileceğim bir dizi oluşturuyorum
sayi_girildi = True #bir daha sayı girilip girilmeyeceğine dair yaptığım kontrol

while sayi_girildi: # burada genel olarak baska sayı girildiğinde onun mükemmel sayı olup olmadığını kontrol ediyor aynı zamanda 0'a basarak döngğden cıkıyor.
    sayi = int(input('Sayı giriniz (Çıkmak için 0\'a basınız) : '))
    if sayi == 0:
        sayi_girildi = False
    elif muk_sayi_bulma(sayi):
        print(sayi, 'sayısı mükemmel bir sayıdır.')
        muk_sayilar.append(sayi)
    else:
        print(sayi, 'sayısı mükemmel bir sayı değildir.')

if muk_sayilar: #girilen mükemmel sayıları toplayıp ortalamasını alıyor aynı zamanda kac tane mükemmel sayı girildiğini gösteriyor eğer girilen sayılarda mükemmel sayı yoksa bunuda ekrana yazdırıyor.
    ortalama = sum(muk_sayilar) / len(muk_sayilar)
    print('Girilen mükemmel sayıların ortalaması:', ortalama)
    print('Toplam', len(muk_sayilar), 'adet mükemmel sayı girildi.')
else:
    print('Girilen sayılar arasında mükemmel sayı bulunmamaktadır.')

