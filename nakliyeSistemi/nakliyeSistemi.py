
sozluk={
    "Gebze":60,
    "Istanbul":110,
    "Edirne":380,
    "Tekirdag":220,
    "Bursa":240,
    "Izmir":520,
    "Aydin":660,
    "Kars":1450,
    "Erzurum":1210
}
mesafe={
    "1km-50km":5,
    "51km-100km":8,
    "101km-300km":12,
    "301km-700km":18,
    "700'den buyuk":20
}
sonuc_sozluk={}
for i in range(3):

    il = input("Hedefiniz: ")

    if il=="Gebze":
         odeme_miktari={sozluk["Gebze"]*5}
         print("Miktar:".format(sozluk["Gebze"]*5))


    elif il=="Istanbul":
         odeme_miktari={sozluk["Istanbul"]*12}
         print("Miktar:{}tl".format(sozluk["Istanbul"]*12))



    elif il=="Izmir":
         odeme_miktari={sozluk["Istanbul"]*18}
         print("Miktar:{}tl".format(sozluk["Izmir"]*18))
         sonuc_sozluk["Izmir"]=sozluk["Izmir"]*5

    else:
        print("Invalid Input")
toplam=0
for k,v in sonuc_sozluk.items():
    toplam=toplam+v
    print("Toplam odeme miktari:",toplam)
































