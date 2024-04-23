def sng_game():
    print("GET READY TO PLAY SNAKE WATER GUN!!!!!")

    print(
        'SNAKE = S',
        '\nGUN = G',
        '\nWATER = W'
    )
    lst = ['S', 'W', 'G']
    import random
    comp_points = 0
    user_points = 0
    choice = 0


    while choice <= 9:
        # Here players enter their desired options among gun, snake and water
        user_choice = input("ENTER S or W or G : ").capitalize()
        comp_choice = random.choice(lst)
        
        # Here is logical statement where condition are given by which game is played
        if user_choice == 'S':
            choice += 1
            if comp_choice == "S":
                print("Its draw.")
            elif comp_choice == "W":
                user_points += 1
                print("You got a point.")    
            elif comp_choice == "G":
                comp_points += 1
                print("Computer got a point.")     
            continue
        elif user_choice == 'W':
            choice += 1
            if comp_choice == "S":
                comp_points += 1
                print("Computer got a point.") 
                print("Its draw.")
            elif comp_choice == "W":
                print("Its draw.")    
            elif comp_choice == "G":
                user_points += 1
                print("You got a point.")     
            continue
        elif user_choice == 'G':
            choice += 1
            if comp_choice == "S":
                user_points += 1
                print("You got a point.")
            elif comp_choice == "W":
                comp_points += 1
                print("Computer got a point.")    
            elif comp_choice == "G":
                print("Its draw.")     
            continue  
        #  Here it checks the validation of the entered choice
        valid = False
        while not valid:
            while user_choice not in ['S', 'W', 'G']:
                print("ERROR!!!! You can only enter S or W or G.")
                user_choice = input("ENTER S or W or G : ").capitalize()
                
            

            if user_choice in ['S', 'W', 'G']:
                valid = True
                choice += 1
            else:    
                print("You cannot go there. Go again.")



    print("COMPUTER GOT", comp_points, "POINTS.")

    print("USER GOT", user_points, "POINTS.")


    # Here it checks the conditions for a winner
    if comp_points > user_points:
        print(f'WINNER!!! IS COMPUTER WITH {comp_points} POINTS.')
    elif  user_points > comp_points:
        print(f'WINNER!!! IS USER WITH {user_points} POINTS.')


    print('GAME ENDED!!!!')

    
sng_game()






