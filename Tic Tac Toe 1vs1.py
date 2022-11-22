print("\n")

print("8's Count as Emtpy Spaces, 0's as Circles and 5's as Crosses")

print("\n")

A = [8, 8, 8] 
B = [8, 8, 8]
C = [8, 8, 8]

print(A)
print(B)
print(C)

print("\n")

x = 1 #Movement Variable
y = 0 #Player (0 / 5) Sign Variable
finish = False # Finished Game Variable
restart = True # True While the Player keeps Restarting
aux = 0 # Variable to Store Restart Options

while(restart==True):
# While to Iterate until the Game is Finished
    while(finish==False):

    #Player Indicator  
        if(y == 0):
            print("Playing as Circles")
        else: print("Playing as Crosses")

        print("\n")

    # Input to Register the Position where the Player wants to place its Movement
        move = int(input("Please enter movement number {} ".format(x))) 

        print("\n")

    # Conditions Separated by Movement Chosen by the Player
        if(move == 1):
            if(A[0]==8):
                A[0] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 2):
            if(A[1] == 8):
                A[1] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 3):
            if(A[2] == 8):
                A[2] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 4):
            if(B[0] == 8):
                B[0] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 5):
            if(B[1] == 8):
                B[1] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 6):
            if(B[2] == 8):
                B[2] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 7):
            if(C[0] == 8):
                C[0] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 8):
            if(C[1] == 8):
                C[1] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

        if(move == 9):
            if(C[2] == 8):
                C[2] = y
                x = x+1
                if(y == 0):
                    y = 5
                else: y = 0

    # Circles Win Conditions
        if(A[0] == 0 and A[1] == 0 and A[2] == 0):
            finish = True
            print("Circles Win")

        if(B[0] == 0 and B[1] == 0 and B[2] == 0):
            finish = True
            print("Circles Win")

        if(C[0] == 0 and C[1] == 0 and C[2] == 0):
            finish = True
            print("Circles Win")

        if(A[0] == 0 and B[0] == 0 and C[0] == 0):
            finish = True
            print("Circles Win")

        if(A[1] == 0 and B[1] == 0 and C[1] == 0):
            finish = True
            print("Circles Win")

        if(A[2] == 0 and B[2] == 0 and C[2] == 0):
            finish = True
            print("Circles Win")
    
        if(A[0] == 0 and B[1] == 0 and C[2] == 0):
            finish = True
            print("Circles Win")

        if(A[2] == 0 and B[1] == 0 and C[0] == 0):
            finish = True
            print("Circles Win")

    #Crosses Win Conditions
        if(A[0] == 5 and A[1] == 5 and A[2] == 5):
            finish = True
            print("Crosses Win")

        if(B[0] == 5 and B[1] == 5 and B[2] == 5):
            finish = True
            print("Crosses Win")

        if(C[0] == 5 and C[1] == 5 and C[2] == 5):
            finish = True
            print("Crosses Win")

        if(A[0] == 5 and B[0] == 5 and C[0] == 5):
            finish = True
            print("Crosses Win")

        if(A[1] == 5 and B[1] == 5 and C[1] == 5):
            finish = True
            print("Crosses Win")

        if(A[2] == 5 and B[2] == 5 and C[2] == 5):
            finish = True
            print("Crosses Win")
    
        if(A[0] == 5 and B[1] == 5 and C[2] == 5):
            finish = True
            print("Crosses Win")

        if(A[2] == 5 and B[1] == 5 and C[0] == 5):
            finish = True
            print("Crosses Win")

    # Tie Condition
        if(A[0] != 8 and A[1] != 8 and A[2] != 8 and B[0] != 8 and B[1] != 8 and B[2] != 8 and C[0] != 8 and C[1] != 8 and C[2] != 8):
            finish = True
            print("It's a Tie!")
        
    # Printing Result
        print("\n")

        print(A)
        print(B)
        print(C)

    # Asking for a Restart
        print("\n")
        if(finish == True):
            aux = int(input("Do you want to Restart the game? (1 to restart ; 0 to stop) "))
            if(aux == 1):
                x = 1
                finish = False
                y = 0
                A = [8, 8, 8] 
                B = [8, 8, 8]
                C = [8, 8, 8]
            else:
                print("Game is Finished. Thanks for playing")
