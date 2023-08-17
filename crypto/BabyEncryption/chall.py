import string
#from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

def decryption():
    encrypted_text = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
    ct = bytes.fromhex(encrypted_text)

    result = ""
    
    #brute force ascii vals. answer restricted to 33-126 ascii vals
    #do encryption process. compare if each is equal to the next encrypted
    #val. proves what it was before. 
    for char in ct:
        for asc_val in range(33, 126):
            if ((123 * asc_val + 18) % 256) == char:
                result+= chr(asc_val)
                break
    return result
        
        

#ct = encryption(MSG)
ct = decryption()
print(ct)
#f = open('./msg.enc','w')
#f.write(ct.hex())
#f.close()





