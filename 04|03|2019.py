matrix1=[[4,6,3],[8,5,3]]
matrix2=[[5,2,3],[6,2,9]]

def my_matrix_addition(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]+m2[row][column])
    return result
#print(my_matrix_addition(matrix1,matrix2))

def my_matrix_substraction(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]-m2[row][column])
    return result
#print(my_matrix_substraction(matrix1,matrix2))

def my_matrix_scalar_product(sayi,m2):
    result=[]
    for row in range(len(m2)):
        result.append([])
        for column in range(len(m2[0])):
            result[row].append(m2[row][column]*alpha)
    return result
alpha=10
#print(my_matrix_scalar_product(alpha,matrix1))

def f1(m1,i):
    return m1[i]

def f2(m1,j):
    my_j_th_col=[]
    for row in m1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col

def my_Vectors_Inner_Product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+my_result[i]
    return t

def my_matrix_multiply(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m2[0])):
            a=f1(m1,row)
            b=f2(m2,column)
            c=my_Vectors_Inner_Product(a,b)
            result[row].append(c)
    return result
