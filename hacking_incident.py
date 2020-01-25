import string
alphabet = string.ascii_lowercase

print(alphabet)
print(list(alphabet))

def encrypt(string,key):
    '''input string is encrypted'''

    encr=list(range(len(string)))
    f=alphabet[:key]
    s=alphabet[key:]
    newalpha=s+f

    for i,letter in enumerate(string.lower()):
        if letter in alphabet:
            l_index=alphabet.index(letter)
            n_letter=newalpha[l_index]
            encr[i]=n_letter
        else:
            encr[i]=letter
    
    print( ''.join(encr))
    return ''.join(encr)


def decrypt(encr,key):
    ''' decrypt the string'''
    decr=list(range(len(encr)))
    f=alphabet[:key]
    s=alphabet[key:]
    newalpha=s+f

    for i,letter in enumerate(encr.lower()):
        if letter in alphabet:
            index=newalpha.index(letter)
            o_letter=alphabet[index]
            decr[i]=o_letter
        else:
            decr[i]=letter
    print(''.join(decr))
    
        
#------------------------------------------
string=input('input string')
key=int(input('input key'))
a=encrypt(string,key)

decrypt(a,key)
#-------------------------------------------


    
        
        

