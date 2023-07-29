import random
def main():
    while True:
        print("Enter the choice\n 1. rock \n 2. paper \n 3. scissor \n")
        choice = int(input("User turn : "))
        while choice > 3 or choice < 1:
            choice = int(input("Enter valid input:"))
        if choice == 1:
            choice_name = "rock"
        elif choice == 2:
            choice_name = "paper"
        else:
            choice_name = "scissor"
        print(f"User choice is : {choice_name}")
        print("\nNow it is computer'sturn.......")
        comp_choice = random.randint(1, 3)
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)
        if comp_choice == 1:
            comp_choice_name = "rock"
        elif comp_choice == 2:
            comp_choice_name = "paper"
        else:
            comp_choice_name = "scissor"
        print(f"Computer choice is :{comp_choice_name}")
        print(f"{choice_name} V/s {comp_choice_name}")
        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print("paper wins =>", end="")
            result = "paper"
        elif (choice == 1 and comp_choice ==3) or (choice == 3 and comp_choice == 1):
            print("rock wins =>",end="")
            result = "rock"
        else:
            print("scissor wins =>",end="")
            result = "scissor"
        if result == choice_name:
            print("<== So User wins ==>")
        else:
            print("<== So Computer wins ==>")
        print("Do you want to play again? (Y/N)")
        ans = input()
        if ans =="n" or ans =="N":
            break                
if __name__=="__main__":
    main()             