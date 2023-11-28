import math

#   This is an encryption system using ACDFGVX ciper (A modified version of ADFGVX, which is upgraded version of ADFGX)
#   The ADFGVX Cipher was used by the German Army during World War I as a field cipher. 
#   It was an extension of the earlier ADFGX Cipher which worked in a very similar way. 
#   It was invented by Colonel Fritz Nebel, and it combines an adapted Polybius Square with Columnar Transposition.
#   It uses a 7x7 polybius square instead of the 6x6 in the original (or 5x5 in case of ADFGX).
#  Source: Wikipedia, CRYPTO CORNER.

m='ACDFGVX'
def sort_function(array): #O(n(log n))
    def partition(array, begin, end ):
        pivot=array[0][end]
        i = begin - 1
        for j in range(begin,end):
            if pivot>=array[0][j]:
                i=i+1
                print('i,j=',i,j)
                (array[0][i], array[0][j]) = (array[0][j], array[0][i])
                (array[1][i], array[1][j]) = (array[1][j], array[1][i])
        (array[0][i + 1], array[0][end]) = (array[0][end], array[0][i + 1])
        (array[1][i + 1], array[1][end]) = (array[1][end], array[1][i + 1])
        return i+1
    def quicksort(array, begin, end ):
        if begin < end:
            pivot = partition(array, begin,end)
            quicksort(array, begin, pivot - 1)
            quicksort(array, pivot + 1, end)
    array=[array]+[list(range(len(array)))]
    quicksort(array,0,len(array[1])-1)
    return array[1]

def permute(m):
    res=[]
    for x, y in ((x, y) for x in m for y in m):
        res+=[[x,y]]
    return list(res)
        
def polybius():
    mapping = (permute(m))
    with open("polybius.txt", "r") as file:
        poly = file.read()
    for i in range(len(mapping)):  
        mapping[i].append(poly[i])
    return mapping

def arrange(r,substitute):
    result=['']*len(r)
    c=0
    for i in substitute:
        result[c]=r[i]
        c=c+1
    return result

def convert(input):
    for i in range(len(input)):
        if input[i]=='A':    
            input[i]=1
        elif input[i]=='C':
            input[i]=2
        elif input[i]=='D':
            input[i]=3
        elif input[i]=='F':
            input[i]=4
        elif input[i]=='G':
            input[i]=5
        elif input[i]=='V':
            input[i]=6
        elif input[i]=='X':
            input[i]=7
        elif input[i]==' ':
            input[i]=0
    return input

def encrypt(plaintext,key):
    plaintext=plaintext.upper()
    l=len(plaintext)
    message_s=''
    mapping=polybius()
    print(mapping)
    #print(mapping[2][2])
    for i in plaintext:
        print("\n",i)
        for j in range(49):
            if mapping[j][2] == i:
                message_s += mapping[j][0]+mapping[j][1]
    print(message_s)
    keyl = len(key)
    padl = math.ceil((l * 2) / keyl) * keyl
    message_s = message_s.ljust(padl)
    row_n = padl // keyl
    # Encryption
    cipher_i = [message_s[i:i+keyl] for i in range(0, len(message_s), keyl)]
    subs_table=sort_function(list(key))
    print(subs_table)
    for row in cipher_i:
       new_row=arrange(row,subs_table)
       convert(new_row)
            
    #This portion is incomplete

def decrypt(ciphertext,key):
    pass 
    #this portion hasn't been developed yet
