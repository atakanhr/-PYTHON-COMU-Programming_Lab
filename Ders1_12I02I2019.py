################################################
#Boyutu n olan tek boyutlu bir dizi uretin#
import random
def generate_an_array(n):
    my_array=[]
    for  i in range(n):
        s=random.randint(0,100)
        my_array.append(s)
    return my_array
################################################
#Test satiri
sayilar=generate_an_array(10) 
print("dizi1 ",sayilar)
################################################
#Bu diziyi bubble sort ile siralayiniz#
def bubble_sort(my_arr) :
    for i in range (len(my_arr)-1, 0, -1) :
        for j in range (i):
            if (my_arr[j] > my_arr[j+1]):
                t = my_arr[j]
                my_arr[j] = my_arr[j+1]
                my_arr[j+1] = t
################################################
#Test satiri
bubble_sort(sayilar)
print("buble sort dizi1" ,sayilar)
################################################
#Selection short#
def selection_sort (arr):
    for i in range (len(arr)-1): #selected
        smallest =i
        for j in range (i+1,len(arr)):
            if (arr[j] < arr[smallest]):
                smallest = j
        arr[i],arr[smallest] = arr[smallest],arr[i]
################################################
#Test#
sayilar2=generate_an_array(10)
print("yeni olusan dizi2",sayilar2)
selection_sort(sayilar2)
print("selection short dizi2 test",sayilar2)

################################################
#Dizi uzerinde arama islemi yapan fonksiyonu yaziniz#
def my_search_c(array_2,item):
  found=False
  indis =-1
  step=0
  for i in range(len(array_2)):
    step+=1
    #if(i==item):
      #found =True
    if (array_2[i]==item):
      found=True
      indis=i
      break
  return found,indis,step
################################################
#Test Satiri#
arama_yapilacak  =10
print("Dizi1 icerisinde ",arama_yapilacak,"sayisinin dönüsü",my_search_c(sayilar,arama_yapilacak))
################################################
#Siralanmis dizi uzerinde binary search#
def binary_search (arr,item) :
    hamle= 0
    alt  = 0
    ust  = len(arr)
    while (alt != ust) :
        if (item < arr[int((alt+ust)/2)]):
            ust=(alt+ust)/2
            hamle += 1
        elif (item > arr[int((alt+ust)/2)]):
            alt=(alt+ust)/2
            hamle += 1
        else :
            return (True , hamle )
    return False
################################################
#Test#
print("dizi 1 uzerinde binary search ",arama_yapilacak,"aramasi",binary_search(sayilar,arama_yapilacak))
