#kendisine verilen listenin frekans tablosunu liste ve sozluk yapisini kullanarak bulan iki fonksiyon

list=[2,3,2,5,8,2,5,7,13,13,13,1,1,7,8,9]
#print(list)

def my_freq(my_list):
    freq_dict={}
    for item in list:
        if(item in freq_dict):
            freq_dict[item]=freq_dict[item]+1
        else:
            freq_dict[item]=1
    return freq_dict
print(my_freq(list))

def my_freq_list(my_list):
    freq_list=[]
    for i in range(len(my_list)):
        s=False
        for j in range(len(freq_list)):
            if(my_list[i]==freq_list[j][0]):
                freq_list[j][1]=freq_list[j][1]+1
                s=True
        if(s==False):
            freq_list.append([my_list[i],1])
    return freq_list
print(my_freq_list(list))
