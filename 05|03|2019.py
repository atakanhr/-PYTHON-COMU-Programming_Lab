#verilen 2x2 , 3x3 , 4x4 matrislerin determinantini bulma

matris1=[[1,2],[3,4]]
matris2=[[1,2,3],[4,5,6],[7,8,9]]
matris3=[[13,2,3,4],[5,6,7,8],[92,10,31,42],[13,134,15,16]]

def det_from_2_by_2(m1):
    s1=m1[0][0]*m1[1][1]
    s2=m1[0][1]*m1[1][0]
    s3=s1-s2
    return s3
sonuc=det_from_2_by_2(matris1)
print(sonuc)


#rakamin satir ve sutununu silip kalan matrisi veriyor

def delete_row_col_from_matrix(m1,m,n):
    result=[]
    size1=len(m1)  #kac satir var
    size2=len(m1[0]) #kac sutun var

    for i in range(size1):
        if(i==m):
            continue
        row1=[]
        for j in range(size2):
            if(j==n):
                continue
            row1.append(m1[i][j])
        result.append(row1)
    return result

def det_from_3_by_3(m1):
    
    a1=m1[0][0]
    a2=delete_row_col_from_matrix(m1,0,0)
    a3=det_from_2_by_2(a2)
    a4=a1*a3

    b1=m1[0][1]
    b2=delete_row_col_from_matrix(m1,0,1)
    b3=det_from_2_by_2(b2)
    b4=b1*b3
   
    c1=m1[0][2]
    c2=delete_row_col_from_matrix(m1,0,2)
    c3=det_from_2_by_2(c2)
    c4=c1*c3
    
    return a4-b4+c4

sonuc3=det_from_3_by_3(matris2)
print(sonuc3)


def det_from_4_by_4(m1):
    
    a1=m1[0][0]
    a2=delete_row_col_from_matrix(m1,0,0)
    a3=det_from_3_by_3(a2)
    a4=a1*a3

    b1=m1[0][1]
    b2=delete_row_col_from_matrix(m1,0,1)
    b3=det_from_3_by_3(b2)
    b4=b1*b3
   
    c1=m1[0][2]
    c2=delete_row_col_from_matrix(m1,0,2)
    c3=det_from_3_by_3(c2)
    c4=c1*c3
    
    d1=m1[0][3]
    d2=delete_row_col_from_matrix(m1,0,3)
    d3=det_from_3_by_3(d2)
    d4=d1*d3
    
    return a4-b4+c4-d4

sonuc4=det_from_4_by_4(matris3)
print(sonuc4)
