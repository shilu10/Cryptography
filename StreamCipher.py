#Streamcipher
# In streamcipher  we can generate a pseduo randomness,which means the algorithm can provide a same set of value for the same initial value or seed we can say
# we will use LCG (Linear Contrigueal Generator for pseudo randomness)
from random import seed


class StreamCipher:
    def __init__(self,seed):
        self.seed=1

    def key_stream(self):
        self.next=self.seed=(1103515245*self.seed+12345)%2**31
        return self.next
    
    def get_key_stream(self):
        return self.key_stream()%256

def encrypt(message):
    print(streamcipher.get_key_stream())
    return bytes([message[i] ^ streamcipher.get_key_stream() for i in range(len(message))])


streamcipher=StreamCipher(1)
message="hello".encode()
cipher=(encrypt(message))
print(cipher)
streamcipher=StreamCipher(1)
print(encrypt(cipher))
