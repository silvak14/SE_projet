import sys

print(sys.argv)
    
if(len(sys.argv)==3):
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(x+y)
elif(len(sys.argv)==2):
    x = int(sys.argv[1])
    y = (input("Entrez la troisieme valeur svp ? "))
    print(x+y)
elif(len(sys.argv)==1):
    x = (input("Entrez la deuxieme la valeur svp ? "))
    y = (input("Entrez la troixieme valeur svp ? "))
    print(x+y)
else:
    print("Desoler erreur")

