from BitVector import *
import time
import secrets
Sbox = (
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
)

InvSbox = (
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]
InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


def substitute_word_Sbox(word):
    substituted_word = ""
    for i in range(0,len(word),2):
        temp=hex(Sbox[int(word[i:i+2],16)])[2:]
        temp=format_hex(temp)
        substituted_word +=temp
    return substituted_word

def substitute_matriix_Sbox(matrix):
    for i in range(0,4):
        for j in range(0,4):
            temp=Sbox[int(matrix[i][j][0],16)][int(matrix[i][j][1],16)]
            temp=format_hex(str(hex(temp))[2:])
            matrix[i][j]=temp
    return matrix 

def substitute_matriix_inverse_Sbox(matrix):
    for i in range(0,4):
        for j in range(0,4):
            temp=InvSbox[int(matrix[i][j][0],16)][int(matrix[i][j][1],16)]
            temp=format_hex(str(hex(temp))[2:])
            matrix[i][j]=temp
    return matrix

def format_hex(hex_string):
    if len(hex_string) == 1:
        return "0" + str(hex_string)
    else:
        return str(hex_string)

def convert_to_hex(string):
    hex_string = ""
    for char in string:
        temp=hex(ord(char))[2:]
        hex_string += format_hex(temp)
    return hex_string

def convert_to_string(hex_string):
    string = ""
    for i in range(0,len(hex_string),2):
        string+=chr(int(hex_string[i:i+2],16))
    return string
rvtAW 


def calculate_round_constant(prev):
    if prev == 0x00:
        return 0x01
    elif prev < 0x80:
        return 2 * prev
    else:
        return (2 * prev) ^ 0x11B
    

def generate_g(string,roundConstant):
    # circular left shiift of string
    string= string[2:] + string[0]+string[1]
    substituted_string = ""
    for i in range(0,len(string),2):
        temp=hex(Sbox[int(string[i],16)][int(string[i+1],16)])[2:]
        temp=format_hex(temp)
        substituted_string +=temp
    # adding round constant 
    firstbyte= hex(int(substituted_string[0:2],16) ^ int( roundConstant))[2:]
    firstbyte=format_hex(firstbyte)
    substituted_string = firstbyte + substituted_string[2:]
    return substituted_string

def column_major_convert(string):
    # 4x4 matrix declared
    matrix = [[0 for x in range(4)] for y in range(4)]
    for i in range(0,len(string),2):
        # column major conversion
        matrix[int((i%8)/2)][int(i/8)]=string[i:i+2]
    return matrix

def column_major_to_string(matrix):
    string=""
    for i in range(0,4):
        for j in range(0,4):
            string+=matrix[j][i]
    return string
    

def xOr_twoWords(word1,word2):
    result=""
    for i in range(0,len(word1),2):
        temp=hex(int(word1[i:i+2],16) ^ int(word2[i:i+2],16))[2:]
        temp=format_hex(temp)
        result +=temp
    return result

def xOR_two_matrix(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            # Ensure that matrix elements are valid hexadecimal strings
            try:
                val1 = int(matrix1[i][j], 16)
                val2 = int(matrix2[i][j], 16)
            except ValueError:
                raise ValueError("Invalid hexadecimal representation in matrices")

            # XOR the values and convert back to hexadecimal
            temp = hex(val1 ^ val2)[2:]
            
            # Pad with zero if needed
            temp = temp.zfill(2)

            row.append(temp)
        result_matrix.append(row)
    return result_matrix


def generate_w_XOR(string1,string2):
    w1=string1[0:8]
    w2=string1[8:16]
    w3=string1[16:24]
    w4=string1[24:32]
    w=""
    w5=xOr_twoWords(w1,string2[0:8])
    w6=xOr_twoWords(w2,w5)
    w7=xOr_twoWords(w3,w6)
    w8=xOr_twoWords(w4,w7)
    w=w5+w6+w7+w8
    return w

def shift_rows(matrix):
    for i in range(0,4):
        matrix[i]=matrix[i][i:]+matrix[i][0:i]
    return matrix

def inverse_shift_rows(matrix):
    for i in range(0,4):
        matrix[i]=matrix[i][4-i:]+matrix[i][0:4-i]
    return matrix
def mix_column(matrix):
    AES_modulus = BitVector(bitstring='100011011')
    result_matrix = [[0 for x in range(4)] for y in range(4)]
    for i in range(0,4):
        for j in range(0,4):
            # galois multiplication
            ans=BitVector(hexstring="00")
            for k in range(0,4):
                temp1=Mixer[i][k]
                temp2=BitVector(hexstring=matrix[k][j])
                temp3=temp1.gf_multiply_modular(temp2,AES_modulus,8)
                ans=ans.__xor__(temp3)
            result_matrix[i][j]=ans.get_bitvector_in_hex()
    return result_matrix


def inverse_mix_column(matrix):
    AES_modulus = BitVector(bitstring='100011011')
    result_matrix = [[0 for x in range(4)] for y in range(4)]
    for i in range(0,4):
        for j in range(0,4):
            # galois multiplication
            ans=BitVector(hexstring="00")
            for k in range(0,4):
                temp1=InvMixer[i][k]
                temp2=BitVector(hexstring=matrix[k][j])
                temp3=temp1.gf_multiply_modular(temp2,AES_modulus,8)
                ans=ans.__xor__(temp3)
            result_matrix[i][j]=ans.get_bitvector_in_hex()
    return result_matrix


def key_resizing(key):
    key=str(key)
    length=len(key)
    if length<16:
        for i in range(0,16-length):
            key+="~"
    elif length>16:
        key=key[0:16]
    return key


def message_block(plaintext):
    plaintext=str(plaintext)
    length=len(plaintext)
    if length%16!=0:
        for i in range(0,16-(length%16)):
            plaintext+=" "
    plaintext=convert_to_hex(plaintext)
    message=[]
    for i in range(0,len(plaintext),32):
        message.append(plaintext[i:i+32])
    return message

def ciphertext_resize(plaintext):
    plaintext=str(plaintext)
    message=[]
    for i in range(0,len(plaintext),32):
        message.append(plaintext[i:i+32])
    return message
   
def generate_keys(key):
    key=str(key)
    start_time=time.time()
    roundKeys = []
    roundKeys.append(key[0:32])
    previousRoundConstant=0x00
    for i in range(0,10):
        previousRoundConstant = calculate_round_constant(previousRoundConstant)
        gOfInput=generate_g(key[24:32],previousRoundConstant)
        roundkey=generate_w_XOR(key[0:32],gOfInput)
        roundKeys.append(roundkey)
        key=roundkey
    end_time=time.time()
    print("time to key schedule    :",(end_time-start_time)*1000,"ms")
    return roundKeys
    

def encryption(roundKeys,IV,message):

    state = column_major_convert(message)
    iv=column_major_convert(IV)
    state=xOR_two_matrix(state,iv)
    round_key_matrix=column_major_convert(roundKeys[0])
    # add round key
    state=xOR_two_matrix(state,round_key_matrix)
    # rounds
    for i in range(0,10):
        state=substitute_matriix_Sbox(state)
        state=shift_rows(state)
        if i!=9:
            state=mix_column(state)
        state=xOR_two_matrix(state,column_major_convert(roundKeys[i+1]))

    cipherTextToRelay=column_major_to_string(state)
    return cipherTextToRelay
   
   
def decryption(roundKeysDecr,IV,message):
    cipherMatrix = column_major_convert(message)
    cipherMatrix=xOR_two_matrix(cipherMatrix,column_major_convert(roundKeysDecr[10]))
    # rounds
    for i in range(9,0,-1):
        cipherMatrix=inverse_shift_rows(cipherMatrix)
        cipherMatrix=substitute_matriix_inverse_Sbox(cipherMatrix)
        cipherMatrix=xOR_two_matrix(cipherMatrix,column_major_convert(roundKeysDecr[i]))
        cipherMatrix=inverse_mix_column(cipherMatrix)

    cipherMatrix=inverse_shift_rows(cipherMatrix)
    cipherMatrix=substitute_matriix_inverse_Sbox(cipherMatrix)
    cipherMatrix=xOR_two_matrix(cipherMatrix,column_major_convert(roundKeysDecr[0]))
    iv=column_major_convert(IV)
    plaint_text=xOR_two_matrix(cipherMatrix,iv)
    text=column_major_to_string(plaint_text)
    return text







def task1_encryption():
    key=input("Enter the key    :")
    key=key_resizing(key)
    print("Key in ASCII     :",key)
    key=convert_to_hex(key)
    print("Key in HEX   :",key)
    input_IV=input("Enter the IV value     :")
    input_IV=key_resizing(input_IV)
    input_IV=convert_to_hex(input_IV)
    IV=input_IV
    plaintext=input("Enter the message  : ")
    print("Message in ASCII     :",plaintext)
    print("Message in HEX   :",convert_to_hex(plaintext))
    message=message_block(plaintext)
    cipher_text=[]
    keys=generate_keys(key)
    start_time=time.time()
    for i in range(0,len(message)):
        temp=encryption(keys,IV,message[i])
        IV=temp
        cipher_text.append(temp)
    cipherTextToRelay=input_IV
    for i in range(0,len(cipher_text)):
        cipherTextToRelay+=cipher_text[i]
    end_time=time.time()
    print("time req to encrypt :",(end_time-start_time)*1000,"ms")
    print("Cipher Text in HEX   :",cipherTextToRelay)
    print("Cipher Text in ascii     :",convert_to_string(cipherTextToRelay))
    
def task1_decryption():
    key=input("Enter the key for decryption     : ")
    key=key_resizing(key) 
    print("Key in ASCII    :",key)
    key=convert_to_hex(key)
    print("Key in HEX :",key)
    ciphertext=input("Enter the ciphertext for decryption   :")
    IV=ciphertext[0:32]
    ciphertext=ciphertext[32:]
    ciphertext=ciphertext_resize(ciphertext)
    plaintext_array=[]
    keys=generate_keys(key)
    start_time=time.time()
    for i in range(0,len(ciphertext)):
        temp=decryption(keys,IV,ciphertext[i])
        IV=ciphertext[i]
        plaintext_array.append(temp)
    plaintext=""
    for i in range(0,len(plaintext_array)):
        plaintext+=convert_to_string(plaintext_array[i])
        
    end_time=time.time()
    print("time req to decrypt :",(end_time-start_time)*1000,"ms")
    print("Message in HEX     :",convert_to_hex(plaintext))
    print("Message Received :",plaintext)
        
    
def task3_encryption(key):
    key=key_resizing(key)
    key=convert_to_hex(key)
    input_IV=secrets.token_hex(16)
    # print("IV in HEX   :",input_IV)
    input_IV=key_resizing(input_IV)
    input_IV=convert_to_hex(input_IV)
    IV=input_IV
    plaintext=input("Enter the message  : ")
    # print("Message in ASCII     :",plaintext)
    # print("Message in HEX   :",convert_to_hex(plaintext))
    message=message_block(plaintext)
    cipher_text=[]
    keys=generate_keys(key)
    
   
    for i in range(0,len(message)):
        temp=encryption(keys,IV,message[i])
        IV=temp
        cipher_text.append(temp)
    cipherTextToRelay=input_IV
    for i in range(0,len(cipher_text)):
        cipherTextToRelay+=cipher_text[i]
    print("Cipher Text in HEX   :",cipherTextToRelay)
    return cipherTextToRelay  
    
def task3_decryption(key,ciphertext):
    key=key_resizing(key)
    key=convert_to_hex(key)
    IV=ciphertext[0:32]
    ciphertext=ciphertext[32:]
    ciphertext=ciphertext_resize(ciphertext)
    plaintext_array=[]
    keys=generate_keys(key)
    for i in range(0,len(ciphertext)):
        temp=decryption(keys,IV,ciphertext[i])
        IV=ciphertext[i]
        plaintext_array.append(temp)
    plaintext=""
    for i in range(0,len(plaintext_array)):
        plaintext+=convert_to_string(plaintext_array[i])
    return plaintext
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
task1_encryption()
task1_decryption()


