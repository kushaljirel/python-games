from random import *


def play():

    print("*******STARTING THE GAME*********\n")
    print(
        "P for Paper\n",
        "S for Scissor\n",
        "R for Rock"
    )
    r_choices = ["S", "P", "R"]

    user_point = 0
    robo_point = 0
    executation = 0
    while executation <= 9:
        robo_choice = choice(r_choices)
        user_choice = input("Enter P, S or R: ").capitalize()
        if user_choice == "S":
            executation += 1
            if robo_choice == "R":
                robo_point += 1
                print("Robot got point.")
            elif robo_choice == "P":
                user_point += 1
                print("User got a point.")
            else:
                print("Its a draw")
            continue

        if user_choice == "P":
            executation += 1
            if robo_choice == "R":
                user_point += 1
                print("User got a point.")
            elif robo_choice == "S":
                robo_point += 1
                print("Robot got point.")
            else:
                print("Its a draw")
            continue

        if user_choice == "R":
            executation += 1
            if robo_choice == "S":
                user_point += 1
                print("User got a point.")
            elif robo_choice == "P":
                robo_point += 1
                print("Robot got point.")

            else:
                print("Its a draw")
            continue

        valid = False
        while not valid:
            while user_choice not in r_choices:
                print(f"Error!! Please enter the from {r_choices}")
                user_choice = input("Enter P, S or R: ").capitalize()

            if user_choice in ['S', 'W', 'G']:
                valid = True
                executation += 1
            else:
                print("You cannot go there. Go again.")

    print(
        f"User got {user_point} points  and robot got {robo_point} points.\n")
    if user_point > robo_point:
        print(f"User is the winner with {user_point} points.\n")
    elif robo_point > user_point:
        print(f"Robot is the winner with {robo_point} points.\n")
    else:
        print(f"Its a draw with {user_point} and {robo_point} points each.\n")

    print("******************GAME OVER*********************")
    print("************THANK YOU FOR PLAYING***************")


if __name__ == "__main__":
    play()
