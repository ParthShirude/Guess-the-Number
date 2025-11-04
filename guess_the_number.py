import random

line = "-" * 100
loop = True

while loop:
    guess_the_number = str(input("Do you want to play the game (y/n): ").lower().strip())
    
    if (guess_the_number == 'y' or guess_the_number == 'yes'):
        while (guess_the_number == 'y' or guess_the_number == 'yes'):
            print("There are two lucky numbers from 1 to 10 always changes if played once.")
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)

            try:
                number_to_guess = int(input("Enter your guess between [1 to 10]: "))

                if (number_to_guess == num1 or number_to_guess == num2):
                    print("You WON!!!! CONGRATULATIONS..........")
                    print(line)
                
                elif (number_to_guess > 10 or number_to_guess < 1):
                    print("Invalid input!!! Enter number between 1 to 10")
                    print(line)

                else:
                    print("You LOSS!!!! please try again ")
                    print(f"The lucky numbers was : {num1},{num2}")
                    print(line)
            
            except (ValueError):
                print("Invalid input!!! Please try again")
                print(line)
                continue

            guess_the_number = str(input("Do you want to play again (y/n): ").lower().strip())

            if (guess_the_number == 'n' or guess_the_number == 'no'):
                print("Thank you!!! for playing our Game.......")
                print(line)
                loop = False
                break
       
            elif (guess_the_number != 'y'and'yes'and'n'and'no'):
                print("Invalid input!!! Please try again")
                print(line)
                continue

    elif (guess_the_number == 'n' or guess_the_number == 'no'):
        print("Thank you!!! for playing our Game.......")
        print(line)
        break

    else:
        print("Invalid input!!! Please try again")
        print(line)