#python3
#RabinKarp - Apply

from random import randint
import math
import sys

def areEqual(S1, S2):
    if len(S1) != len(S2):
        return False
    else:
        for i in range(len(S1)):
            if S1[i] != S2[i]:
                return False
        return True

def polyHash1(S, prime, x):
    h = 0
    for i in range(len(S))[::-1]:
        h = (h*x + ord(S[i])) % prime

    return h

def PreComputeHash(T,prime, x, p_len,m):
    H = [None]*(len(T)-p_len + 1)
    S = T[len(T) - p_len:len(T):]
    H[len(T) - p_len] = polyHash1(S,prime,x)

    y = 1
    for i in range(1,len(P)+1):
        y = (y*x)%prime
    i = len(T) - p_len - 1
    while i >= 0:
        H[i] = (x*H[i+1] + (ord(T[i]) - y*ord(T[i+p_len])))%prime
        i -= 1

    for i in range(len(H)):
        H[i] = H[i]%m

    return H


def isPrime(n):
    i = 2
    while i <= math.sqrt(n)+1 :
        if n%i == 0:
            return False
        else:
            i+=1
    return True


def bigPrime(size):
    size = size*10
    num = size
    while not isPrime(num):
        num += 1
    return num


def RabinKarp(T, P):
    #prime = bigPrime(len(P)*len(T))
    prime = 1000000007
    x = min(1000, prime)
    x = randint(0,x)
    m = 100*len(P)

    pHash = polyHash1(P,prime,x)
    pHash = pHash%m

    result = []

    H = PreComputeHash(T,prime,x,len(P),m)

    for i in range(len(T) - len(P) + 1):
        tHash = H[i]
        if tHash != pHash:
            continue
        elif areEqual(T[i:i+len(P):], P):
            print(i, end = " ")

    return

if __name__ == '__main__':
    #data = list(map(str, input().split()))
    data = list(map(str, sys.stdin.read().split()))
    P = data[0]
    T = data[1]

    RabinKarp(T, P)
