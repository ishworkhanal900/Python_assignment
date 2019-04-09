plainText = input("text to encrypt : ") 
distance = int(input("distance: ")) 
code = "" 
for ch in plainText:    
    ordValue = ord(ch)  
    cipherValue = ordValue + distance   
    if cipherValue > ord('z'):      
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code = code + chr(cipherValue)
print(code)
