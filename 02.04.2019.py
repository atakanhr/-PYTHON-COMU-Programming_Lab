import math
def string_search (text, string):
     return string in text, text.find(string), text.find(string)+len(string)-1

def complete_string_search(text, string):
    indices = []
    while string in text:
        indice = text.find(string)
        indices.append(indice)
        text = text[indice+len(string)-1:]
    return indices

string_search('Onsekiz Mart Universitesi', 'iversi')

#complete_string_search('Onsekiz Mart Universitesi Mart Ayi Icersinde', 'Mart')
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('WOW'))
print(is_palindrome('CANSOZBIR'))
from math import sqrt
def char_to_matrix(word):
    n = sqrt(len(word))
    if n != int(n):
        return -1
    n = int(n)
    matrix = [[word[n*i+j] for j in range(n)]for i in range(n)]
    return matrix
char_to_matrix('CANSOZBIR')
def standart_sapma(liste):
    ort = sum(liste)/len(liste)
    sum_list = 0
    for x in liste:
        sum_list += (x-ort)**2
    return math.sqrt(sum_list/(len(liste)-1))
standart_sapma(range(10))
def del_col(A,col):
    newMatrix = []
    for i in range (len(A)):
        newMatrix.append([])
        for j in range(len(A[i])):
            if j != col:
                newMatrix[i].append(A[i][j])
    return newMatrix
    def det(A):
    sum_det = 0
    if len(A)==2:
        return A[0][0]*A[1][1] - A[1][0]*A[0][1]
    for i in range (len(A[0])):
        sum_det += ((-1)**(i+2))*A[0][i]*det(del_col(A[1:],i))
    return sum_det

A = [[1,2,3],[4,8,9],[4,1,7]]
det(A)
def is_singular(matrix):
    return det(matrix)==0

is_singular([[1,0],[1,0]])
def esolon (m):
    pass
def max_row(matrix):
    row_sum = sum(matrix[0])
    maximum = 0
    for row in matrix:
        if sum(row) > row_sum:
            maximum=row
            
    return maximum

def get_col(matrix, colNo):
    col = []
    for i in range (len(matrix)):
        col.append([matrix[i][colNo]])
    return col

def max_col(matrix):
    maxCol = []
    maxSum = 0
    for i in range(len(matrix)):
        col = get_col(matrix,i)
        tempSum = sum([row[0] for row in matrix ]) 
        if tempSum > maxSum:
            maxSum = tempSum
            maxCol = col
    return col
        
    
A = [[1,2],[4,5]]
print('max row:', max_row(A))
print('max col:', max_col(A))
def count_zeros(matrix):
    counter = 0
    for row in matrix:
        counter += row.count(0)
    return counter/(len(matrix)*len(matrix[0]))

deneme = [[1,2,0],[0,1,2],[1,2,3]]
count_zeros(deneme)
from random import randint
def create (m:int, n:int):
    return [[randint(0,10) for j in range(n)] for i in range(m)]

def print_array(my_list):
    for row in my_list:
        for element in row:
            print(element, end = ' ')
        print()
            
def convert_to_hash(my_list):
    my_dict = {}
    if count_zeros(my_list) < 0.3:
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                my_dict[(i, j)] = my_list[i][j]
        return my_dict
    else:
        print('HASH DONUSUMU YAPILMADI')
        return my_list

                        
def print_hash(my_hash_list):
    print ('  ')
    for key in my_hash_list:
        print(my_hash_list[key], end = ' ')

array = create(4,5)
print_array(array)
array = convert_to_hash(array)

if type(array) != list:
    print_hash(array)
else:
    print (array)

def convert_to_list(hashdict):
    matrix = [[0 for j in range(5)]for i in range (4)]
    for key, value in hashdict.items():
        matrix[key[0]][key[1]] = value
    return matrix

convert_to_list(array)
def my_sqrt(sayi):
    epsilon = 1e-15
    t = sayi
    while abs(t - sayi/t) > epsilon*t:
        t = (sayi/t + t) / 2.0
    return t
my_sqrt(9)
hash1 = convert_to_hash(create(3,4))
hash2 = convert_to_hash(create(3,4))

def hash_toplama(hash1, hash2):
    hash3 = {}
    for key in hash1:
        hash3[(key[0], key[1])] = hash1[(key[0], key[1])] + hash2[(key[0], key[1])]
    return hash3

hash3 = hash_toplama(hash1, hash2)
print_hash(hash1)
print_hash(hash2)
print('\n'+'_'*30+'+')
print_hash(hash3)
