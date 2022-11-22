from random import randint


print("\n")

print("O's Count as Emtpy Spaces, 0's as R and 5's as Crosses")

print("\n")

A = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
B = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
C = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
D = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
E = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
F = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)

print("\n")

x = 1 #Movement Variable
y = 'B' #Player (0 / 5) Sign Variable
finish = False # Finished Game Variable
restart = True # True While the Player keeps Restarting
aux = 0 # Variable to Store Restart Options
z = 0 # Variable to check if The next tile is empty or not

while(restart==True):
# While to Iterate until the Game is Finished
    while(finish==False):

    #Player Indicator  
        if(y == 'B'):
            print("Playing as BLUE")
        else: print("Playing as RED")

        print("\n")

    # Input to Register the Position where the Player wants to place its Token

        move = int(input("Select the number of column where you want to place the token"))
        print("\n")

    # Conditions Separated by Movement Chosen by the Player
        if(move == 1):
            if(A[0] == 'O'):
                z = z + 1
                if(B[0] == 'O'):
                    z = z + 1
                    if(C[0] == 'O'):
                        z = z + 1
                        if(D[0] == 'O'):
                            z = z + 1
                            if(E[0] == 'O'):
                                z = z + 1
                                if(F[0] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[0] = y

            if(z == 2):
                B[0] = y

            if(z == 3):
                C[0] = y

            if(z == 4):
                D[0] = y
            
            if(z == 5):
                E[0] = y
            
            if(z == 6):
                F[0] = y

    # Conditions Separated by Movement Chosen by the Player
        if(move == 2):
            if(A[1] == 'O'):
                z = z + 1
                if(B[1] == 'O'):
                    z = z + 1
                    if(C[1] == 'O'):
                        z = z + 1
                        if(D[1] == 'O'):
                            z = z + 1
                            if(E[1] == 'O'):
                                z = z + 1
                                if(F[1] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[1] = y

            if(z == 2):
                B[1] = y

            if(z == 3):
                C[1] = y

            if(z == 4):
                D[1] = y
            
            if(z == 5):
                E[1] = y
            
            if(z == 6):
                F[1] = y

    # Conditions Separated by Movement Chosen by the Player
        if(move == 3):
            if(A[2] == 'O'):
                z = z + 1
                if(B[2] == 'O'):
                    z = z + 1
                    if(C[2] == 'O'):
                        z = z + 1
                        if(D[2] == 'O'):
                            z = z + 1
                            if(E[2] == 'O'):
                                z = z + 1
                                if(F[2] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[2] = y

            if(z == 2):
                B[2] = y

            if(z == 3):
                C[2] = y

            if(z == 4):
                D[2] = y
            
            if(z == 5):
                E[2] = y
            
            if(z == 6):
                F[2] = y

    # Conditions Separated by Movement Chosen by the Player
        if(move == 4):
            if(A[3] == 'O'):
                z = z + 1
                if(B[3] == 'O'):
                    z = z + 1
                    if(C[3] == 'O'):
                        z = z + 1
                        if(D[3] == 'O'):
                            z = z + 1
                            if(E[3] == 'O'):
                                z = z + 1
                                if(F[3] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[3] = y

            if(z == 2):
                B[3] = y

            if(z == 3):
                C[3] = y

            if(z == 4):
                D[3] = y
            
            if(z == 5):
                E[3] = y
            
            if(z == 6):
                F[3] = y

    # Conditions Separated by Movement Chosen by the Player
        if(move == 5):
            if(A[4] == 'O'):
                z = z + 1
                if(B[4] == 'O'):
                    z = z + 1
                    if(C[4] == 'O'):
                        z = z + 1
                        if(D[4] == 'O'):
                            z = z + 1
                            if(E[4] == 'O'):
                                z = z + 1
                                if(F[4] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[4] = y

            if(z == 2):
                B[4] = y

            if(z == 3):
                C[4] = y

            if(z == 4):
                D[4] = y
            
            if(z == 5):
                E[4] = y
            
            if(z == 6):
                F[4] = y

    # Conditions Separated by Movement Chosen by the Player
        if(move == 6):
            if(A[5] == 'O'):
                z = z + 1
                if(B[5] == 'O'):
                    z = z + 1
                    if(C[5] == 'O'):
                        z = z + 1
                        if(D[5] == 'O'):
                            z = z + 1
                            if(E[5] == 'O'):
                                z = z + 1
                                if(F[5] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[5] = y

            if(z == 2):
                B[5] = y

            if(z == 3):
                C[5] = y

            if(z == 4):
                D[5] = y
            
            if(z == 5):
                E[5] = y
            
            if(z == 6):
                F[5] = y

    # Conditions Separated by Movement Chosen by the Player
        if(move == 7):
            if(A[6] == 'O'):
                z = z + 1
                if(B[6] == 'O'):
                    z = z + 1
                    if(C[6] == 'O'):
                        z = z + 1
                        if(D[6] == 'O'):
                            z = z + 1
                            if(E[6] == 'O'):
                                z = z + 1
                                if(F[6] == 'O'):
                                    z = z + 1
                

            if(z == 0):
                print("This column is full, you cannot place a token here, please choose a different one")
            
            if(z == 1):
                A[6] = y

            if(z == 2):
                B[6] = y

            if(z == 3):
                C[6] = y

            if(z == 4):
                D[6] = y
            
            if(z == 5):
                E[6] = y
            
            if(z == 6):
                F[6] = y


    # Changing players
        if(z != 0):
            if(y == 'B'):
             y = 'R'
            else: y = 'B'
        
    # Reset move variable
        z = 0

    # Win Conditions (Horizontal Win)

        if(A[0] == 'B' and A[1] == 'B' and A[2] == 'B' and A[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(A[1] == 'B' and A[2] == 'B' and A[3] == 'B' and A[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(A[2] == 'B' and A[3] == 'B' and A[4] == 'B' and A[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(A[3] == 'B' and A[4] == 'B' and A[5] == 'B' and A[6] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(B[0] == 'B' and B[1] == 'B' and B[2] == 'B' and B[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[1] == 'B' and B[2] == 'B' and B[3] == 'B' and B[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[2] == 'B' and B[3] == 'B' and B[4] == 'B' and B[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[3] == 'B' and A[4] == 'B' and A[5] == 'B' and B[6] == 'B'):
            finish = True
            print ("BLUE Wins")
            


        if(C[0] == 'B' and C[1] == 'B' and C[2] == 'B' and C[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[1] == 'B' and C[2] == 'B' and C[3] == 'B' and C[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[2] == 'B' and C[3] == 'B' and C[4] == 'B' and C[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[3] == 'B' and C[4] == 'B' and C[5] == 'B' and C[6] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(D[0] == 'B' and D[1] == 'B' and D[2] == 'B' and D[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(D[1] == 'B' and D[2] == 'B' and D[3] == 'B' and D[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(D[2] == 'B' and D[3] == 'B' and D[4] == 'B' and D[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(D[3] == 'B' and D[4] == 'B' and D[5] == 'B' and D[6] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(E[0] == 'B' and E[1] == 'B' and E[2] == 'B' and E[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(E[1] == 'B' and E[2] == 'B' and E[3] == 'B' and E[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(E[2] == 'B' and E[3] == 'B' and E[4] == 'B' and E[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(E[3] == 'B' and E[4] == 'B' and E[5] == 'B' and E[6] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(F[0] == 'B' and F[1] == 'B' and F[2] == 'B' and F[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(F[1] == 'B' and F[2] == 'B' and F[3] == 'B' and F[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(F[2] == 'B' and F[3] == 'B' and F[4] == 'B' and F[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(F[3] == 'B' and F[4] == 'B' and F[5] == 'B' and F[6] == 'B'):
            finish = True
            print ("BLUE Wins")





        if(A[0] == 'R' and A[1] == 'R' and A[2] == 'R' and A[3] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(A[1] == 'R' and A[2] == 'R' and A[3] == 'R' and A[4] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(A[2] == 'R' and A[3] == 'R' and A[4] == 'R' and A[5] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(A[3] == 'R' and A[4] == 'R' and A[5] == 'R' and A[6] == 'R'):
            finish = True
            print ("BLUE Wins")



        if(B[0] == 'R' and B[1] == 'R' and B[2] == 'R' and B[3] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(B[1] == 'R' and B[2] == 'R' and B[3] == 'R' and B[4] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(B[2] == 'R' and B[3] == 'R' and B[4] == 'R' and B[5] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(B[3] == 'R' and A[4] == 'R' and A[5] == 'R' and B[6] == 'R'):
            finish = True
            print ("BLUE Wins")
            


        if(C[0] == 'R' and C[1] == 'R' and C[2] == 'R' and C[3] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(C[1] == 'R' and C[2] == 'R' and C[3] == 'R' and C[4] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(C[2] == 'R' and C[3] == 'R' and C[4] == 'R' and C[5] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(C[3] == 'R' and C[4] == 'R' and C[5] == 'R' and C[6] == 'R'):
            finish = True
            print ("BLUE Wins")



        if(D[0] == 'R' and D[1] == 'R' and D[2] == 'R' and D[3] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(D[1] == 'R' and D[2] == 'R' and D[3] == 'R' and D[4] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(D[2] == 'R' and D[3] == 'R' and D[4] == 'R' and D[5] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(D[3] == 'R' and D[4] == 'R' and D[5] == 'R' and D[6] == 'R'):
            finish = True
            print ("BLUE Wins")



        if(E[0] == 'R' and E[1] == 'R' and E[2] == 'R' and E[3] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(E[1] == 'R' and E[2] == 'R' and E[3] == 'R' and E[4] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(E[2] == 'R' and E[3] == 'R' and E[4] == 'R' and E[5] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(E[3] == 'R' and E[4] == 'R' and E[5] == 'R' and E[6] == 'R'):
            finish = True
            print ("BLUE Wins")



        if(F[0] == 'R' and F[1] == 'R' and F[2] == 'R' and F[3] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(F[1] == 'R' and F[2] == 'R' and F[3] == 'R' and F[4] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(F[2] == 'R' and F[3] == 'R' and F[4] == 'R' and F[5] == 'R'):
            finish = True
            print ("BLUE Wins")

        if(F[3] == 'R' and F[4] == 'R' and F[5] == 'R' and F[6] == 'R'):
            finish = True
            print ("BLUE Wins")



    # Win Conditions (Vertical Win)

        if(A[0] == 'B' and B[0] == 'B' and C[0] == 'B' and D[0] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[0] == 'B' and C[0] == 'B' and D[0] == 'B' and E[0] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[0] == 'B' and D[0] == 'B' and E[0] == 'B' and F[0] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(A[1] == 'B' and B[1] == 'B' and C[1] == 'B' and D[1] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[1] == 'B' and C[1] == 'B' and D[1] == 'B' and E[1] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[1] == 'B' and D[1] == 'B' and E[1] == 'B' and F[1] == 'B'):
            finish = True
            print ("BLUE Wins")


        
        if(A[2] == 'B' and B[2] == 'B' and C[2] == 'B' and D[2] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[2] == 'B' and C[2] == 'B' and D[2] == 'B' and E[2] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[2] == 'B' and D[2] == 'B' and E[2] == 'B' and F[2] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(A[3] == 'B' and B[3] == 'B' and C[3] == 'B' and D[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[3] == 'B' and C[3] == 'B' and D[3] == 'B' and E[3] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[3] == 'B' and D[3] == 'B' and E[3] == 'B' and F[3] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(A[4] == 'B' and B[4] == 'B' and C[4] == 'B' and D[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[4] == 'B' and C[4] == 'B' and D[4] == 'B' and E[4] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[4] == 'B' and D[4] == 'B' and E[4] == 'B' and F[4] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(A[5] == 'B' and B[5] == 'B' and C[5] == 'B' and D[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[5] == 'B' and C[5] == 'B' and D[5] == 'B' and E[5] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[5] == 'B' and D[5] == 'B' and E[5] == 'B' and F[5] == 'B'):
            finish = True
            print ("BLUE Wins")



        if(A[6] == 'B' and B[6] == 'B' and C[6] == 'B' and D[6] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(B[6] == 'B' and C[6] == 'B' and D[6] == 'B' and E[6] == 'B'):
            finish = True
            print ("BLUE Wins")

        if(C[6] == 'B' and D[6] == 'B' and E[6] == 'B' and F[6] == 'B'):
            finish = True
            print ("BLUE Wins")





        if(A[0] == 'R' and B[0] == 'R' and C[0] == 'R' and D[0] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[0] == 'R' and C[0] == 'R' and D[0] == 'R' and E[0] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[0] == 'R' and D[0] == 'R' and E[0] == 'R' and F[0] == 'R'):
            finish = True
            print ("RED Wins")



        if(A[1] == 'R' and B[1] == 'R' and C[1] == 'R' and D[1] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[1] == 'R' and C[1] == 'R' and D[1] == 'R' and E[1] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[1] == 'R' and D[1] == 'R' and E[1] == 'R' and F[1] == 'R'):
            finish = True
            print ("RED Wins")


        
        if(A[2] == 'R' and B[2] == 'R' and C[2] == 'R' and D[2] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[2] == 'R' and C[2] == 'R' and D[2] == 'R' and E[2] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[2] == 'R' and D[2] == 'R' and E[2] == 'R' and F[2] == 'R'):
            finish = True
            print ("RED Wins")



        if(A[3] == 'R' and B[3] == 'R' and C[3] == 'R' and D[3] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[3] == 'R' and C[3] == 'R' and D[3] == 'R' and E[3] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[3] == 'R' and D[3] == 'R' and E[3] == 'R' and F[3] == 'R'):
            finish = True
            print ("RED Wins")



        if(A[4] == 'R' and B[4] == 'R' and C[4] == 'R' and D[4] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[4] == 'R' and C[4] == 'R' and D[4] == 'R' and E[4] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[4] == 'R' and D[4] == 'R' and E[4] == 'R' and F[4] == 'R'):
            finish = True
            print ("RED Wins")



        if(A[5] == 'R' and B[5] == 'R' and C[5] == 'R' and D[5] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[5] == 'R' and C[5] == 'R' and D[5] == 'R' and E[5] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[5] == 'R' and D[5] == 'R' and E[5] == 'R' and F[5] == 'R'):
            finish = True
            print ("RED Wins")



        if(A[6] == 'R' and B[6] == 'R' and C[6] == 'R' and D[6] == 'R'):
            finish = True
            print ("RED Wins")

        if(B[6] == 'R' and C[6] == 'R' and D[6] == 'R' and E[6] == 'R'):
            finish = True
            print ("RED Wins")

        if(C[6] == 'R' and D[6] == 'R' and E[6] == 'R' and F[6] == 'R'):
            finish = True
            print ("RED Wins")


    # Printing Result
        print("\n")

        print(A)
        print(B)
        print(C)
        print(D)
        print(E)
        print(F)

    # Asking for a Restart
        print("\n")
        if(finish == True):
            aux = int(input("Do you want to Restart the game? (1 to restart ; 0 to stop) "))
            if(aux == 1):
                finish = False
                y = 'B'
                A = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
                B = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
                C = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
                D = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
                E = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
                F = ['O', 'O', 'O', 'O', 'O', 'O', 'O'] 
            else:
                print("Game is Finished. Thanks for playing")
