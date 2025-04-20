# star_pyramid.py
# This script prints left, right, and center-aligned pyramids using stars (*),
# with exception handling for user input, and loops to keep generating pyramids.
# The user can exit the loop by entering '0'.

print("hwak tuah START")

while True:
    try:
        n = int(input("enter number of rows: "))  # Get number of rows from the user
    except ValueError:
        print("invalid input")  # Handle non-integer input
    else:
        print("number of rows = " + str(n))  # Display the number of rows
        print("here's you fucking pyramid")
        
        # Left-aligned pyramid
        for i in range(n):
            print("*"*(i+1))
        
        print("here's fucking right pyramid")
        
        # Right-aligned pyramid
        for j in range(n):
            print(" " * (n-(j+1)), end="")  # Spaces for right alignment
            print("*" * (j+1))
        
        print('TS why is end="" used??')
        
        # Display without `end=""`
        print('\nWithout end=""')
        print("Hello")
        print("world")        
        
        # Display with `end=""`
        print('\nWith end=""')
        print("Hello", end="")
        print("World")

        print("\nThis shit gettin interstin")
        print("\n lesgooo centre pyramid")
        
        # Center-aligned pyramid (odd number of stars)
        for k in range(n):
            print(" " *(n - k - 1), end="")  # Spaces for center alignment
            print("*" * (2*k+1))  # Odd number of stars
    
    finally:  
        # Exit condition
        exit = input("\nPress any key to continue\nPress 0 to exit\nYour input: ")
        
        if exit == "0":
            print("bye bxtch")  # Exit message
            break
        else:
            continue

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
