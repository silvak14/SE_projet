import sys
def add(a,b):
    return a+b
if __name__=="__main__":
    
     print(sys.argv)
if(len(sys.argv)==3):
    x = int( sys.argv[1] )
    y = int( sys.argv[2] )
    print (add(x,y))
elif(len(sys.argv)==2):
    x=int(sys.argv[1])
    y=int(input("veuillez entrer la troisieme valeur:"))
    print(add(x,y))
elif (len(sys.argv)==1):
    x=int(input("veuillez entrer la deuxieme  valeur:"))
    y=int(input("veuillez entrer la troisieme valeur:"))
    print(add(x,y))
else:
    print("erreur")
