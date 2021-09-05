import random
from typing import Match

class Substitution_Cipher:
    def __init__(self,message):
        self.message=message
        self.alphabets='abcdefghijklmnopqrstuvwxyz'
        self.listofalphabets=list(self.alphabets)
        self.maps={}
        self.key=[]
        self.letter_frequency= {
            'E' : 12.0,
            'T' : 9.10,
            'A' : 8.12,
            'O' : 7.68,
            'I' : 7.31,
            'N' : 6.95,
            'S' : 6.28,
            'R' : 6.02,
            'H' : 5.92,
            'D' : 4.32,
            'L' : 3.98,
            'U' : 2.88,
            'C' : 2.71,
            'M' : 2.61,
            'F' : 2.30,
            'Y' : 2.11,
            'W' : 2.09,
            'G' : 2.03,
            'P' : 1.82,
            'B' : 1.49,
            'V' : 1.11,
            'K' : 0.69,
            'X' : 0.17,
            'Q' : 0.11,
            'J' : 0.10,
            'Z' : 0.07 
            }

    
    
    def generate_keys(self):
        for letter in self.alphabets:
            forkey=self.listofalphabets.pop(random.randint(0,len(self.listofalphabets)-1))
            self.key.append(forkey)
            self.maps[letter]=forkey
      #  print(self.key)
        return self.maps



    def encryption(self):
        CipherText=""
        for letter in self.message:
            if letter in self.maps:
                CipherText+=self.maps[letter]
            else:
                CipherText+=letter

        return CipherText

  
    def decryption_key(self,cipher):
        Decryptionkey={}
        for letter in self.maps:
            Decryptionkey[self.maps[letter]]=letter

        return Decryptionkey

   
    def decryption(self,message,key):
        PlainText=""
        for letter in message:
            if letter in key:
                PlainText+=key[letter]
            else:
                PlainText+=letter

        return PlainText


    def cal_frequency(self,message):
        #we use frequency analysis to break this particular cipher)
        letter_frequencies={}
        for letter in self.alphabets:
            letter_frequencies[letter]=round(message.count(letter)/len(message),3)

        return letter_frequencies


    def sorting_our_dic(self,cipher):
       
        
        dic=self.cal_frequency(cipher)
        sort_orders = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return sort_orders


    def comparing_both(self,cipher):
        letter=[]
        myletter=[]
        for key in self.letter_frequency:
            letter.append(key)

        dic=self.sorting_our_dic(cipher)
        for key in dic:
            myletter.append(key)

        analysisList=zip(letter,myletter)
        return dict(analysisList)

        

message="""Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper.

The decision about what to put into your paragraphs begins with the germination of a seed of ideas; this “germination process” is better known as brainstorming. There are many techniques for brainstorming; whichever one you choose, this stage of paragraph development cannot be skipped. Building paragraphs can be like building a skyscraper: there must be a well-planned foundation that supports what you are building. Any cracks, inconsistencies, or other corruptions of the foundation can cause your whole paper to crumble.

So, let’s suppose that you have done some brainstorming to develop your thesis. What else should you keep in mind as you begin to create paragraphs? Every paragraph in a paper should be:

    Unified: All of the sentences in a single paragraph should be related to a single controlling idea (often expressed in the topic sentence of the paragraph).
    Clearly related to the thesis: The sentences should all refer to the central idea, or thesis, of the paper (Rosen and Behrens 119).
    Coherent: The sentences should be arranged in a logical manner and should follow a definite plan for development (Rosen and Behrens 119).
    Well-developed: Every idea discussed in the paragraph should be adequately explained and supported through evidence and details that work together to explain the paragraph’s controlling idea (Rosen and Behrens 119).
"""
              
mycipher=Substitution_Cipher(message)

key=mycipher.generate_keys()

cipher=mycipher.encryption()

print(cipher)

print(mycipher.comparing_both(cipher))

mydkey=mycipher.decryption_key(key)

mycipher.decryption(cipher,mydkey)


