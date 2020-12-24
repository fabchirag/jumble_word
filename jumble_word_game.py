import random

def choose():
    words = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "board"]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(player_1, player_2, player_1_points, player_2_points):
    print(player_1, "Your score is: ", player_1_points)
    print(player_2, "Your score is: ", player_2_points)
    print("Thank you for Playing")
    print("Have a nice day!")

def play():
    player_1 = input("Player 1, Enter your name: ")
    player_2 = input("Player 2, Enter your name: ")
    player_1_points = 0
    player_2_points = 0
    turn = 0
    correct_answers = []
    wrong_answers = []

    while(1): # 1 means True, always going to be True
        # following is a computer's Task
        picked_word = choose() # picked_word is a dictionary and choose() is a function. computer will pick the word from a dictionary and assigne it to picked_word
        # create a questions
        question = jumble(picked_word)
        print(question)

        # Player 1
        if turn % 2 == 0:
            print(player_1, " Your turn. ")
            answer = input("What is on my mind?: ")
            if answer == picked_word:
                correct_answers.append(answer)
                player_1_points = player_1_points + 1
                print("Your score is: ", player_1_points)
            else:
                wrong_answers.append(answer)
                print("That's incorrect, Try again..")
                answer = input("Try 2nd: ")
                if answer == picked_word:
                    correct_answers.append(answer)
                    player_1_points = player_1_points + 1
                    print("Your score is: ", player_1_points)
                else:
                    wrong_answers.append(answer)
                    print("Better luck next time, ", picked_word)
            c = int(input("Press 1 to 'Continue' and 0 to 'Quit': "))
            if c == 0:
                thank(player_1, player_2, player_1_points, player_2_points)
                break

        # Player 2
        else:
            print(player_2, " Your turn. ")
            answer = input("What is on my mind?: ")
            if answer == picked_word:
                correct_answers.append(answer)
                player_2_points = player_2_points + 1
                print("Your score is: ", player_2_points)
            else:
                wrong_answers.append(answer)
                print("Better luck next time. I thought: ", picked_word)
            c = int(input("Press 1 to 'Continue' and 0 to 'Quit': "))
            if c == 0:
                print("Correct Answers: ",correct_answers)
                print("Wrong Answers: ", wrong_answers)
                thank(player_1, player_2, player_1_points, player_2_points)
                break
        turn = turn + 1

play()

