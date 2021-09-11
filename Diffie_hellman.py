#diffie hellman key exchange

#1. step generate large prime and largest primitive root of that prime .primitive root is nothing but
#when the number is mod with the prime number it wil give all th possible number 
#prime number is proportinal to the primitive root number  
#prime number (p)  and primitive root(g)

#2.generate prime number for the personal private key x,y< prime number (p) for both users

#3.we will produce a private key for the exchange purpose using the modular exponention
# formula a**g mode p  ->>  g **x mod p( ,g**Y mod p

#and both will exchange the key with each other ,attacker can have all of these things
#but he cant able to break the inverse of modular exponentation (discrete logarithm)

#4.using that both can have the same private key with each other......by using the formula of 
#modular exponentation with the (key ** x,y mod p)--->>>> this will give same key for both of them in conversation

#we can generate the given number is prime or not using the fermat little theorem but fermat theorem is not proven
#fermat little theorem  -->>  a**p-1 mod p=1  where p is the prime number a is not divisable of p
#and fermat little theorem is probablistic which means we need some iteration for the confirmation that it is really a prime  number

import random


def is_prime(number):
    if number<2:
        return False
    for _ in range(10):
    
        a=random.randint(2,number)-1
        if pow(a,number-1,number) !=1:
            
            return False
    return True


def primitive_root(prime):
    num_to_check = 0
    p_minus_1_range = range(1,prime)
    primitive_roots = []
    for each in range(1, prime):
	    num_to_check += 1
	    candidate_prim_roots = []
	    for i in range(1, prime):
		    modulus = (num_to_check ** i) % prime
		    candidate_prim_roots.append(modulus)
		    cleanedup_candidate_prim_roots = set(candidate_prim_roots)
		    if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
			    primitive_roots.append(num_to_check)
    return primitive_roots[len(primitive_roots)-1]


def generating_prime_and_primitive_root(start,end):
    number=random.randint(start,end)
    
    while not is_prime(number):
        number=random.randint(start,end)
    primitive_rootno=primitive_root(number)
    return number,primitive_rootno


def diffie_hellman(start,end):
    prime,primitive_root=generating_prime_and_primitive_root(start,end)
    user1_Pkey=random.randint(1,prime)
    user2_Pkey=random.randint(1,prime)

    private_key1=pow(primitive_root,user1_Pkey,prime)
    private_key2=pow(primitive_root,user2_Pkey,prime)
    
    key=pow(private_key2,user1_Pkey,prime)
    key2=pow(private_key1,user2_Pkey,prime)

    print(f"key1 -->{key}  ,key2-->{key2}")



diffie_hellman(1,67)


