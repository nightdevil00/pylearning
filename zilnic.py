import sys
import os

def meniu():
    print('Ce doresti sa faci')
    alegere = input(str(''))
    if alegere == "raport" :
        cauta()
    if alegere == "quit" :
       sys.exit
    else:
        print('Poti selecta raport sau quit')

def cauta():
 fisier = input("Numele documentului si extensia: ")
 cuvant=input("Ce cuvant cauti: ? ")
 k = 0
     
 with open(fisier, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==cuvant):
                k=k+1
 print(F"Cuvantul " +  str(cuvant), "se repeta de: ")
 print(k, 'ori') 

meniu()

input('Apasa <enter> pt a iesi.')
