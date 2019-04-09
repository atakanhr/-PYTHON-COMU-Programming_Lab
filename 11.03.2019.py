#Sayinin carpanlarini bulup asallik kontrolu yapan fonksiyon
from math import sqrt as sqrt
def is_prime(num):
    if num < 2:
        return False , [num]
    carpanlar = [1]
    i=2
    while(num > 1):
        if num%i== 0:
            carpanlar.append(i)
            num /= i
        else:
            i += 1
    if len(carpanlar) > 2:
        return False, carpanlar
    else :
        return True, carpanlar
        
is_prime(42)
is_prime(41)
is_prime(1)
#Bir listede elemanlari ardisik olarak toplayarak bulunabilecek maksimum sayi
list = [-4,-3,-2,-1,21,22,-2,-6,-5]
def max_sequential (liste):
    maxSum = liste[0]
    maxSumIndexs = []
    for i in range (len(liste)):
        sum_n=0
        for j in range (i,len(liste)):
            sum_n += liste[j]
            if maxSum < sum_n :
                maxSum = sum_n
                
    return maxSum
max_sequential(list)
