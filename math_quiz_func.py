from random import randint as r
import json
import sys
from matplotlib import pyplot as plt

def generate_numbers(difficulty):
    """
    Function for generating pairs of random numbers in descending order
    to create equations.

    Different sets of numbers are generated at each difficulty.
        Easy: Two small numbers for addition and subtraction
        Medium: Two large numbers for addition and subtraction
        Hard: Four numbers addition, subtraction, multiplication and division
    
    """

    if difficulty == 'e':
        # 1 to 20 for easy
        numbers = [r(2,20), r(2,20)]
        return sorted(numbers, reverse=True)

    elif difficulty == 'm':
        # 1 to 100 for medium
        numbers = [r(2,100), r(2,100)]    
        return sorted(numbers, reverse=True)
    
    elif difficulty == 'h':
        # 2 to 12 for hard multiplication and division
        numbers = [r(2,100), r(2,100), r(2,12), r(2,100)]
        numbers[0:2] = sorted(numbers[0:2], reverse=True)
        numbers[2:4] = sorted(numbers[2:4], reverse=True)
        return numbers

def addition(n1, n2):
    """ Returns question string and answer integer """
    question = f'{n1} + {n2}'
    answer = n1 + n2
    return question, answer

def subtraction(n1, n2):
    """ Returns question string and answer integer """
    question = f'{n1} - {n2}'
    answer = n1 - n2
    return question, answer

def multiplication(n1, n2):
    """ Returns question string and answer integer """
    question = f'{n1} * {n2}'
    answer = n1 * n2
    return question, answer

def division(n1, n2):
    """ Returns question string and answer integer """
    question = f'{n1} / {n2}'
    answer = int(n1 / n2)               # Convert float back into integer
    return question, answer


def generate_question(numbers):
    """
    Function for generating questions based off numbers from generate_numbers.
    
    An operator is selected at random and then a string is produced to be
    displayed to the user. 
    
    The function returns both the integer representing the operator and the
    string representation of the question.
    
    """
    if len(numbers) == 4 and numbers[2] % numbers[3] != 0:    
        operator = r(0, len(numbers)-2)
    else:
        operator = r(0, len(numbers)-1)
   
    if operator == 0:
        question, answer = addition(numbers[0], numbers[1])
        return question, answer

    elif operator == 1:
        question, answer = subtraction(numbers[0], numbers[1])
        return question, answer

    elif operator == 2:
        question, answer = multiplication(numbers[2], numbers[3])
        return question, answer

    elif operator == 3:
        question, answer = division(numbers[2], numbers[3])
        return question, answer

def check_file_exists(filename):
    """ Check if the json file exists """
    try:
        with open(filename) as f_obj:
            scores = json.load(f_obj)
    except FileNotFoundError:
        return False
    else: 
        return True

def save_score(filename, name, score):
    """ 
    Check if the name exists in json file.
    
    If name exists, append or else create new data entry.

    Seeks file to the start which can then be dumped into json.
    
    """
    with open(filename, 'r+') as f_obj:
        scores = json.load(f_obj)
        if name in scores.keys():
            print(f'\nWelcome back {name}!')
            scores[name].append(score)
        else:
            print(f'\nNice to meet you {name}!')
            scores[name] = [score]
        # Seek to start and save file
        f_obj.seek(0)
        json.dump(scores, f_obj)

def view_score(filename, name):
    """ 
    Converts scores into str and joins them. 
    
    Counts frequency of each score and plots it in a bar chart.

    """
    with open(filename) as f_obj:
        scores = json.load(f_obj)
        scores_string = [str(i) for i in scores[name]]
        score_list = ', '.join(scores_string)
        print(f'{name}: {score_list}')

        # Plot scores onto bar chart        
        x_axis = []
        scores_list = []
        for i in range(11):
            x_axis.append(i)
            scores_list.append(scores[name].count(i))
        
        plt.bar(x_axis, scores_list)
        plt.title(f"{name}'s Test Scores")
        plt.xlabel('Number of correct answers')
        plt.ylabel('Frequency')
        plt.show()
 

def quit_quiz(string):
    """ End quiz if 'q' is pressed. """
    try:
        string.lower()
    except:
        pass
    else:
        if string.lower() == 'q':
            print('Hope you enjoyed the quiz, see you next time!')
            sys.exit()