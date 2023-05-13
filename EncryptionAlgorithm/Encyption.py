# This program takes a string and outputs the encrypted string and decrypted string using a reverse process
# algorithm

import sys
import random

# Seed that tells the binary seed how much to shift
seeds1 = ['18165746555744039310692854252066022296258061822172', '63535052180631612988039930478077544821925318426882',
'48888621758155184322879918916203565711850687771895', '08766812872527359745615704611913454817611302771714',
'83628970418952347684717361125015253142099666134226'] 

# Binary seed that determines whether the cipher will shift the required amount
seeds2 = ['10111110101110100101011110001001001110000000110011', '11011001101010111000000010111111000010010101011000',
    '00110110000001000011111111111000111001110011001011', '01111010010110001111000000100100100011001100101101', 
    '11010011100011101010101011100100011110001011110101']

# Key to the encrypted string
encryption_key = [];

# Encrypts the string s
def encrypt(s):
    rand1 = random.randint(0, 4)
    rand2 = random.randint(0, 4)
    seed1 = seeds1[rand1]
    seed2 = seeds1[rand2]
    encrypted = ''
    for i in range(len(s)):
        if (i >= len(seed1)):
            addTo = int(seed1[i % len(seed1)])
            upOrDown = int(seed2[i % len(seed2)])
        else:
            addTo = int(seed1[i])
            upOrDown = int(seed2[i])
        
        if (upOrDown > 0):
            encrypted += chr(ord(s[i]) + addTo)
        else:
            encrypted += chr(ord(s[i]) - addTo)
    
    # Adds the seed index values to the key for decryption
    encryption_key.append(rand1)
    encryption_key.append(rand2)

    return encrypted

# Decrypts the string s using the encryption key optained in the encryption algorithm
def decrypt(s, encryption_key = []):
    # Tests the length of the encryption key to ensure it is not empty
    if (len(encryption_key) > 0):
        seed1 = seeds1[encryption_key[0]]
        seed2 = seeds1[encryption_key[1]]
        decrypted = ''
        for i in range(len(s)):
            if (i >= len(seed1)):
                addTo = int(seed1[i % len(seed1)])
                upOrDown = int(seed2[i % len(seed2)])
            else:
                addTo = int(seed1[i])
                upOrDown = int(seed2[i])
            
            if (upOrDown > 0):
                decrypted += chr(ord(s[i]) - addTo)
            else:
                decrypted += chr(ord(s[i]) + addTo)
        
        return decrypted
   
   # Only if no key is given for the decrypt function
    else:
        print('NO KEY GIVEN FOR DECRYPTION')

def main():
    print('Enter a string for encryption: ')
    s = sys.stdin.readline()
    encrypted_string = encrypt(s)
    print('Encrypted String: ' + encrypted_string)
    decrypted_string = decrypt(encrypted_string, encryption_key)
    if (decrypted_string != None):
        print('Decrypted String: ' + decrypted_string)
main()