
 
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

cauta()

input('Apasa <enter> pt a iesi.')
