sayi= int(input("tek mi çift mi olduğunu merak ettiğiniz sayıyı giriniz: "))
if (sayi%2==1):
    print("girdiğiniz sayı tek sayıdır")
else :
   print("girdiğiniz sayı çift sayıdır")

print("**************************************")

sayilarlist=[]

sayi1= int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))
sayilarlist.append(sayi1)
sayi2= int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))
sayilarlist.append(sayi2)
sayi3= int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))
sayilarlist.append(sayi3)
sayi4= int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))
sayilarlist.append(sayi4)
sayi5= int(input("Asallığını kontrol etmek istediğiniz sayıyı giriniz: "))
sayilarlist.append(sayi5)

    
def Asal (sayi):
   adet=0
   for i in range(2,sayi+1):
     if sayi%i==0:
        adet+=1
   if adet==1:
        print (sayi, " asaldir")
   else:
        print (sayi," asal degildir")

for i in range(0,5):
    Asal(sayilarlist[i])

print("*************************************")
sayilar="0123456789"

ilk_string ="Ah5me4t"
ikinci_string = "M9eHm4eT"
ucuncu_string ="Ha3K5a1n"

temizlerlist=[]
  
def TemizVeri (text):
  for a in text:
    if  a in sayilar:
     text=text.replace(a,"")
  text=text.capitalize()
  temizlerlist.append(text)

TemizVeri(ilk_string)
TemizVeri(ikinci_string)
TemizVeri(ucuncu_string)


Birlesmis_deger=""
for kelime in temizlerlist:
    Birlesmis_deger=Birlesmis_deger+"-"+kelime
print(Birlesmis_deger)




