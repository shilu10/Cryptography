#OneTimepad
# message + randomness(key)-> cipher
#cipher + randomness(key) -> message
import random

class OneTimePad:
    def __init__(self,message):
        self.message=message

    def key_stream(self):
        return bytes([random.randrange(0,256) for i in range(len(self.message))])

    def encrypt(self,key,message):
        length=min(len(message),len(key))
        return bytes([message[i] ^ key[i] for i in range(length)])

    

message="hello".encode()
onetimepad=OneTimePad(message)
key=onetimepad.key_stream()
print(key)
cipher=onetimepad.encrypt(key,message)
print(onetimepad.encrypt(message,cipher))
ourkey=(onetimepad.encrypt("hehee".encode(),cipher))
print(onetimepad.encrypt(ourkey,cipher))
