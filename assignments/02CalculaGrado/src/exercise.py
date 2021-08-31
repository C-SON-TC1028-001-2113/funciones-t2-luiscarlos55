def main():
    #escribe tu código abajo de esta línea
    print('Hello World!')
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    if x>1:
        print('score incorrecto')	
    elif x>=.9:
        print('A')
    elif x>=.8:
        print('B')
    elif x>=.7:
        print('C')
    elif x>=.6:
        print('D')
    elif x<=.5:
        print('F')
    else:
        print('Score incorrecto')
    
if __name__=='__main__':
    main()
