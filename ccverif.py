
import numpy as np
import random as r
import sys

def main():

    args = sys.argv[1:]

    def argVerif(args):
        if not args or not args[0].isnumeric():
            return False
        if args[0] == '-h' or args[0] == '--help' or len(args) >= 2:
            return False    
        else:
            return True
    def verifier(ccNum):
        a = np.empty((len(ccNum)),dtype=int)
        a[::2] = 2
        a[1::2] = 1
        b = ccNum * a
        b = [sum(list(map(int, str(n)))) if n > 9 else n for n in b]
        
        finalSum = sum(b)
        if finalSum%10 == 0:
            return True
        else:
            return False
    if(argVerif(args)):
        if verifier([int(x) for x in str(args[0])]):
            print(f'O Número {args[0]} é válido')
        else:
            print('Número Inválido')
    else:
        print ('''ccverif.py [NÚMERO]
        --help ou -h para mostrar essa mensagem''')
         
main()
