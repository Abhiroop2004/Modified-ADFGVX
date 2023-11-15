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
    quicksort(array)
    return array[0],array[1]

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

def encrypt(c,key):
    l=len(c)
    message_s=''
    mapping=polybius()
    for i in range(l):
        t = c[i]
        for j in range(49):
            if mapping[j][2] == t:
                message_s += mapping[j][0:2]
    keyl = len(key)
    padl = math.ceil((l * 2) / keyl) * keyl
    message_s = message_s.ljust(padl)
    print(message_s)
    row_n = padl // keyl
    # Encryption
    cipher_i = [message_s[i:i+keyl] for i in range(0, len(message_s), keyl)]
    cipher_j = sort_function(key, cipher_i, keyl)
    cipher_final = ''.join(cipher_j)
    print("Cipher Text: \n%s" % cipher_final)


def acdfgvx(c,key,choice):
    if choice == 1:
        # This is the code for encrypting data
        c = c.upper()
        encrypt(c,key)
    elif choice == 2:
        l = len(c)
        keyl = len(key)
        padl = math.ceil((l) / keyl) * keyl
        c = [c[i:i+keyl] for i in range(0, len(c), keyl)]
        pt = sort_function(key, c, keyl)
        pt_final = ''.join(pt)
        # This portion hasn't been developed yet



