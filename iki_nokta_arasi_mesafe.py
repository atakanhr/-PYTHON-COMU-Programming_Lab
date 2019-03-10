dizi=[[7,4],[1,2],[3,4],[2,8],[1,4],[1,6],[3,9]]
def yazdir(i,j):
    print(i+1," ile",(j+1),"arasındaki mesafe :",end="" )

def uzaklık(dizi1,dizi2):
    return (((dizi2[0]-dizi1[0])**2)+((dizi2[1]-dizi1[1])**2))**(1/2)

def enkucuk_bul(dizi3):
    kucuk = uzaklık(dizi3[0],dizi3[1])
    tutucu = 0
    s1=1
    s2=2
    for i in range(len(dizi)-1):
        for j in range(i+1,len(dizi)):
            tutucu=uzaklık(dizi3[i],dizi3[j])
            if(tutucu<kucuk):
                kucuk=tutucu
                s1=i+1
                s2=j+1
    print("EN KISA MESAFE",s1,"ILE",s2,"ARASINDAKI MESAFEDIR :",kucuk)

def dizi_cagir(dizi):
    for i in range(len(dizi)-1):
        for j in range(i+1,len(dizi)):
            yazdir(i,j)
            print(uzaklık(dizi[i],dizi[j]))

print(dizi)         
dizi_cagir(dizi)
enkucuk_bul(dizi)
