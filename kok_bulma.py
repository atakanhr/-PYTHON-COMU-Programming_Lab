a=int(input("ikinci dereceden terimn kat sayısı:"))
b=int(input("birinci dereceden terimin kat sayısı:"))
c=int(input("sabit sayı:"))
delta=(b**2)-(4*a*c)
if(delta>0):
      x1=(-b-((delta)**(1/2)))/(2*a)
      x2=(-b+((delta)**(1/2)))/(2*a)
      print("iki farklı kok var")
      print("1. kok:"+str(x1))
      print("2. kok:"+str(x2))
elif(delta==0):
      x1=x2=-b/(2*a)
      print("tek katlı kok var:"+str(x1))
else:
     print("sabit kok yok")
