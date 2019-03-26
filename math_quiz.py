import math_quiz_func as m
import json
import sys
from matplotlib import pyplot as plt

# Start the program.
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
start = input(
    "Welcome to the mental math quiz. To start press enter, to quit "
    "just type 'q': "
)

m.quit_quiz(start)

# Start the quiz.
while True:
    while True:
        # Select difficulty, loop if no proper difficulty is selected.
        difficulty =  input(
            "Please choose from the following difficulties."
            "\t 'e' - easy"
            "\t 'm' - medium"
            "\t 'h' - hard"
            "\nYou have selected: "
        )

        m.quit_quiz(difficulty)
        
        if difficulty == 'e':
            break
        elif difficulty == 'm':
            break
        elif difficulty == 'h':
            break
        else:
            print('Sorry, please try again.\n')
        
    start = input(
        "\nAre you ready to start the quiz? Press enter to start, press 'q' to "
        "quit anytime."
    )

    m.quit_quiz(start)

    score = 0
    for i in range(10):
        # For number of questions specified, generate a question.
        numbers = m.generate_numbers(difficulty)
        question, answer = m.generate_question(numbers)
        
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nScore:', score)
        print(question)
        
        # Loop for answering the question
        while True:
            attempt = input("Please type your answer: ")
            m.quit_quiz(attempt)
                
            # Add a point to score if correct.
            try:
                if int(attempt) == answer:
                    score += 1
            except:
                pass
            else:
                break
        
    print('\nCongratulations on finishing the quiz, your score was:', score)
    
    save = input('Would you like to save your score? (y/n): ')
    m.quit_quiz(save)
    if save == 'y': 
        # Check if the file exists
        filename = 'scores.json'
        exists = m.check_file_exists(filename)
        
        if exists:
            # If file exists save score under name. Can also view past scores
            name = input('Please type your name: ')
            m.save_score(filename, name, score)
            print('You score has been saved.')
            view_score = input('\nWould you like to view your scores? (y/n)')
            if view_score == 'y':
                m.view_score(filename, name)
                
        else:
            # Create new dictionary and json file and save scores
            scores = {}
            name = input('Please type your name: ')
            print(f'\nNice to meet you {name}!')
            scores[name] = [score]
            with open(filename, 'w') as f_obj:
                json.dump(scores, f_obj)        
       
    try_again = input('\nWould you like to try again? (y/n): ')
    m.quit_quiz(try_again)
    
    # Continue loop or exit program
    if try_again == 'n':
        print('See you next time!')
        sys.exit()
    
    continue

            
            

