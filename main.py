from mulTwoInt import mul
from addTwoInt import add
import sys

if __name__ == "__main__":
	reponse= input("Avez vous besoin de multiplier ?(oui/non)")
	print(reponse)
	if(reponse == "oui"):
		if(len(sys.argv)==3):
			print(sys.argv)
			x = int(sys.argv[1])
			y = int(sys.argv[2])
			print(mul(x,y))
		elif(len(sys.argv)==2):
			x = int(sys.argv[1])
			y = int(input("Entrez la troisieme valeur svp ? "))
			print(mul(x,y))
		elif(len(sys.argv)==1):
			x = int(input("Entrez la deuxieme valeur svp ? "))
			y = int(input("Entrez la troisieme valeur svp ? "))
			print(mul(x,y))
		else:
			print("Erreur")

            if(reponse == "non"):
                if(len(sys.argv)==3):
                        print(sys.argv)
                        x = int(sys.argv[1])
                        y = int(sys.argv[2])
                        print(add(x,y))
                elif(len(sys.argv)==2):
                        x = int(sys.argv[1])
                        y = int(input("Entrez la troisieme valeur svp ? "))
                        print(add(x,y))
                elif(len(sys.argv)==1):
                        x = int(input("Entrez la deuxieme valeur svp ? "))
                        y = int(input("Entrez la troisieme valeur svp ? "))
                        print(add(x,y))
                else:
                        print("Erreur")

	else:
            		print("Aurevoir")
