def encrypt(text, n):
    result = ""
    for i in range (len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + n - 65) % 26 + 65)
        else:
            result += chr((ord(char) + n - 97) % 26 + 97)
    return result

# Encryption
a = "ArshSaxena"
n = 14
print (encrypt(a, n))

# # Decryption (just 26 - n)
# b = "OfgvGolsbo"
# r = 26 - n
# print (encrypt(b, r))

# i = 0
# while i < 20:
#     print(encrypt(encrypt(a, n), i))
#     i = i+1

i = 0
while i < 26:
    print(encrypt(encrypt(a, n), i) + " " + str(i))
    i = i + 1