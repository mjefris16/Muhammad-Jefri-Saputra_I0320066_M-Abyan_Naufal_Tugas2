#Menghitung luas persegi pangjang
def Persegi_panjang():
    print("Menghitung Luas Persegi Panjang")
    p = int(input("masukkan panjangnya : "))
    l = int(input("masukkan lebarnya : "))
    luas = p*l
    print("luas persegi panjang adalah : ",luas)

Persegi_panjang()

#Menghitung luas lingkaran
def Lingkaran():
    print("Menghitung Luas Lingkaran")
    r = float(input("masukkan panjang jari-jarinya : "))
    phi = 3.14
    luas = phi * r * r
    print("luas lingkaran adalah : " + str(luas))

Lingkaran()

#Menghitung luas kubus
def Kubus():
    print("Menghitung Luas Kubus")
    rusuk = int(input("masukkkan panjang rusuknya : "))
    luas = 6*rusuk*rusuk
    print("luas kubus adalah : ", luas)

Kubus()

#Konversi suhu celcius ke farenheit
print("Konversi Suhu Celcius ke Farenheit")
celcius = float(input("masukkan suhu : "))
farenheit = 9/5*celcius+32
print("celcius : ", celcius)
print("farenheit :", farenheit)


#Menghitung suhu reamur ke kelvin
print("Konversi Suhu Reamur ke Kelvin")
reamur = float(input("masukkan suhu : "))
kelvin = 5/4*reamur+273
print("reamur : ", reamur)
print("kelvin :", kelvin)



