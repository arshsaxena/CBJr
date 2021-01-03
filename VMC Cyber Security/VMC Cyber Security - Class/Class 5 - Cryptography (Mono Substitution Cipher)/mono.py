key = { 
    "a" : "z", 
    "b" : "a", 
    "c" : "q", 
    "d" : "x", 
    "e" : "s", 
    "f" : "w", 
    "g" : "c", 
    "h" : "d", 
    "i" : "e", 
    "j" : "v", 
    "k" : "f", 
    "l" : "r", 
    "m" : "b", 
    "n" : "g", 
    "o" : "t", 
    "p" : "n", 
    "q" : "h", 
    "r" : "y", 
    "s" : "m", 
    "t" : "j", 
    "u" : "u", 
    "v" : "k", 
    "w" : "i", 
    "x" : "l", 
    "y" : "o", 
    "z" : "p", 
    " " : " " 
}

#This function allows us to make cipher text.
def mono_encode(key, plainText):
    plainText = plainText.lower()
    cipherText= ""
    for i in plainText:
        cipherText = cipherText + key[i]
    return cipherText

def mono_decode(key, cipherText):
    cipherText = cipherText.lower()
    plainText = ""
    listKey = list(key.keys()) # This keys() will give me all the keys of the dic.
    listValues = list(key.values()) # This values() will give me all the values of the dic.
    for i in cipherText:
        plainText += listKey[listValues.index(i)]
    return plainText

# print(mono_encode(key, "Arsh Saxena"))
print(mono_decode(key, "zymd mzlsgz"))