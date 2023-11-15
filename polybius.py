import random
    # This function generates a 7x7 polybius square
    # The square contains 49 unique characters as follows:
    # A-Z | 0-9 | space | symbols  ,.,''-_%+*@?()
    # Def: A Polybius Square is a table that allows someone to convert letters into numbers.
    # The device is used for fractionating plaintext characters so that they can be represented by a smaller set of symbols, which is useful for telegraphy, steganography, and cryptography.
    # According to Polybius' Histories, the device was invented by Cleoxenus and Democleitus, and further developed by Polybius himself.
    # The original square used the 24 Greek alphabets and space. (5x5)
def polybius():
    map_alpha = random.sample(range(65, 91), 26)
    map_alpha = [chr(x) for x in map_alpha]
    map = ''
    for i in range(len(map_alpha)):
        t = ord(map_alpha[i]) - 64
        map += map_alpha[i]
        if (t > 0 and t < 10):
            map += str(t)
        elif (t == 10):
            map += '0'
    mapsym = ' .,\'-_%+*@?()'
    mapf = ''
    print("Map: ",map)
    j = 0
    order = random.sample(range(36), 13)
    ordersym = random.sample(range(13), 13)
    mapsym_r = [None] * 13
    for i in range(len(ordersym)):
        mapsym_r[ordersym[i]] = mapsym[i]
    #print ("order: ",order)    
    #print ("ordersym: ",ordersym)
    #print ("Mapsym_r: ",mapsym_r)
    for i in range(len(map)):
        mapf += map[i]
        if (i in order):  
            mapf += mapsym_r[j]
            #print(mapf,j)
            j += 1
    file=open('polybius.txt', 'w')
    file.write(mapf)
    file.close()
polybius()