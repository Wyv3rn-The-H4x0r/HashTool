'''

    Dev : Wyv3rn
    Tool : HashEnycrypter
    Version : 1.1
    Python : 2.7.5

'''
import hashlib

print("----------------------")
print("|   Hash-Enycrypter   |")
print("|      V 1.1          |")
print("|        by           |")
print("|       Wyv3rn        |")
print("----------------------")

def start():
    print("1- MD5  2- SHA1  3- SHA256  4- SHA512")
    print("5- whirlpool  6- ripemd160  7- BLAKE2b512")
    print("MD5 - not Recommend for Hash Messages -> (Not Secure!)")
    Hashtype = int(input("Enter Hashtype : Letters will Break the Tool : "))
    print(Hashtype)
    Hashcode = raw_input("Enter Code To Hash (Only 1 Line Max) : \n")
    if Hashtype == 1:
        h = hashlib.md5()
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    elif Hashtype == 2:
        h = hashlib.sha1()
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    elif Hashtype == 3:
        h = hashlib.sha256()
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    elif Hashtype == 4:
        h = hashlib.sha512()
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    elif Hashtype == 5:
        h = hashlib.new('whirlpool')
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    elif Hashtype == 6:
        h = hashlib.new('ripemd160')
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    elif Hashtype == 7:
        h = hashlib.new('BLAKE2b512')
        h.update(Hashcode)
        print("Hash : \n\n"+h.hexdigest())
    start()
start()