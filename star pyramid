print("hwak tuah START")

while True:
    try:
        n = int(input("enter number of rows: "))
    except ValueError:
        print("invalid input")
    else:
        print("number of rows = " + str(n))
        print("here's you fucking pyramid")
        
        #left pyramid
        for i in range(n):
            #print("loop started")
            print("*"*(i+1))
            
        print("here's fucking right pyramid")
        
        for j in range(n):
            print(" " * (n-(j+1)), end="") #WHY TS en=""
            print ("*" * (j+1))
            
        print('TS why is end="" used??')
        
        print('\nWithout end=""')
        print("Hello")
        print("world")        
        
        print('\nWith end=""')
        print("Hello", end="")
        print("World")
    
    
        print("\nThis shit gettin interstin")
        print("\n lesgooo centre pyramid")
        
        
        '''
        #here the spaces are correct but number of stars is wrong therefore
        #it doenst look centre alligned
        for k in range(n):
            print(" " *(n - k - 1), end="")
            print("*" * k)
        
        '''
        
        
        for k in range(n):
            print(" " *(n - k - 1), end="")
            print("*" * (2*k+1))  #odd number of stars
            
    finally:  
        exit = input("\nPress any key to continue\nPress 0 to exit\nYour input: ")
        
        if exit == "0":
            print("bye bxtch")
            break
        else:
            continue
