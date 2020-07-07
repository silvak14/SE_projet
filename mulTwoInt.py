import sys

print(sys.argv)

x = int( sys.argv[1] )
y = int( sys.argv[2] )

if(len(sys.argv)==3):
    print(x+y)
else:
    print("Erreur")

