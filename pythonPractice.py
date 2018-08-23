import random
import string
import requests
from bs4 import BeautifulSoup as bs


def char_input():
    name = str(input('What is your name? \n'))
    age = int(input('What is your age? \n'))
    random_num = int(input('Enter another number.\n'))
    current_year = 2018
    date = (100-age) + current_year
    for i in range(random_num):
         print('You will turn 100 in year {}'.format(date))

def odd_even():
    num = int(input('Please enter a number \n'))
    EVEN_MESSAGE = 'You entered an even number'
    ODD_MESSAGE = 'You entered an odd number'
    MULTIPLE_OF_FOUR = 'You entered a multiple of four'
    print(EVEN_MESSAGE) if num % 2 == 0 else print(ODD_MESSAGE)

    if num % 4 == 0:
        print(MULTIPLE_OF_FOUR)
    else:
        print('Not a multiple of four')

def less_Than_Ten():
    nums = [int(x) for x in input('enter numbers \n')]
    answer_list = list(filter(lambda x: x < 5, nums))
    print(answer_list)

def divisors():
    try:
        answer = []
        num = int(input('Please enter a number \n'))
        for i in range(1, num+1):
            if num % i == 0:
                answer.append(i)
    except ValueError as error:
        print(error)

    print(answer)


def list_Overlap():
    nums = [int(x) for x in input('enter numbers \n')]
    nums2 = [int(x) for x in input('enter numbers \n')]

    return_list = [value for value in a if value in b]
    print(return_list)

def palindrome():
    user_string = input('Enter a word \n').replace(' ', '')
    print('Palindrome') if user_string[::-1] == user_string else print('Not palindrome')

def even_List_Comprehension():
    a = [1,4,9,16,25,36,49,64,81,100]
    new_list = [x for x in a if x%2==0]
    print(new_list)

def rock_Paper_Scissors():
    options = {
            1: 'Rock',
            2: 'Paper',
            3: 'Scissors'
        }
    message = 'Player take your turn by playing rock (1), paper (2), or scissors (3) \n'
    new_game_message = 'Would you like to play again? (Y/N)'
    while True:
        p1 = int(input(message))
        p2 = int(input(message))

        print('Player one picked {} , player two picked {}'.format(options.get(p1), options.get(p2)))

        if p1 and p2 not in [1,2,3]:
            print('Please enter either 1,2,3')

        if p1 == p2:
            print('You have tied this round. Pick again')

        a = options.get(p1)
        b = options.get(p2)

        difference = int(p1-p2)

        if difference in [1,-2]:
            print('Player One has won!')
            rematch = input(new_game_message).upper()
            if rematch not in 'Y N'.split():
                rematch = input('Please choose either Y or N \n').upper()
            if rematch == 'Y':
                continue
            elif rematch == 'N':
                break

        if difference in [-1, 2]:
            print('Player Two has won!')
            rematch = input(new_game_message).upper()
            if rematch not in 'Y N'.split():
                rematch = input('Please choose either Y or N \n').upper()
            if rematch == 'Y':
                continue
            elif rematch == 'N':
                break

    print('Thanks for playing')

def guessing_Game():
    num = random.randint(1,9)
    play_again = ''
    while True:
        try:
            user_guess = int(input('Guess a number \n '))
            if user_guess < num:
                print('Too Low')
            elif user_guess > num:
                print('Too high')
            elif user_guess == num:
                print('You got it! ')
                play_again = input('Would you like to play again? (Y / N) \n').upper()
                if play_again not in 'Y N'.split():
                    play_again = input('Please enter either Y or N \n ')
                if play_again == 'Y':
                    continue
                elif play_again == 'N':
                    break
        except ValueError as err:
            print(err)
    print('Thanks for playing the guessing game')

def list_Overlap_Comprehension():
    num = random.randint(5,10)
    num2 = random.randint(5,10)
    l1 = set()
    l2 = set()
    for _ in range(num):
        num_to_add = random.randint(5,10)
        num2_to_add = random.randint(5,10)
        l1.add(num_to_add)
        l2.add(num2_to_add)
    return_list = [x for x in l1 if x in l2]
    print('First list is {} \nSecond list is {}'.format(l1,l2))
    print('Overlapping set is {}'.format(return_list))

def list_ends(a = [1,2,3,4]):
    answer = []
    answer.append(a[0])
    answer.append(a[-1])
    print(answer)

def get_fibonnaci_length():
    try:
        numbers = int(input('How many fibonnaci numbers would you like? \n'))
        return numbers
    except ValueError as error:
        return(error)

def fibonnaci(n):
    a = 1
    b = 1
    li = []
    for i in range(1, n + 1):
        s = a + b
        li.append(a)
        (a,b) = (b, s)
    print(li)

def list_remove_duplicates(a):
    answer = set(a)
    print('original list: {}'.format(a))
    print('unique list {}'.format(answer))

def reverse_order():
    try:
        word_to_reverse = input('Enter a long string of words and I will reverse it for you \n ').split()
        print(' '.join(word_to_reverse[::-1]))

    except KeyError as error:
        print(error)

def password_Generator():
    symbols = ['!', '@', '#', '%', '$', '^', '&', '*', '*', '-', '+', '|', '~']
    letters = [s for s in string.ascii_letters]
    range_of_nums = random.randint(1,10)
    password = ''
    for _ in range(1, range_of_nums):
        index = random.randint(1,range_of_nums)
        password += symbols[index]
        password += letters[index]
    print(password)

def scrape_NewYork_Times():
    url = 'https://nytimes.com'
    r = requests.get(url)
    titles = []
    soup = bs(r.text, 'html.parser')
    title = soup.find_all('h2', {'class': 'story-heading'})
    for row in title:
        titles.append(row.text.strip())
    answer_titles = list(filter(None, titles))
    return str(answer_titles)

def elementSearch(li, num):
    return num in li

def writeToAFile():
    try:
        name_of_file = input('What would you like the file to be called? \n')
        with open(name_of_file + '.txt', 'w') as file:
            file.write(scrapeNewYorkTimes())
            file.close()
    except ValueError as e:
        print(e)

def readFromFile():
     with open('namelist.txt', 'r') as file:
         data = file.read().splitlines()
         answer = {}
         for element in data:
             if element in answer:
                 answer[element] += 1
             else:
                answer[element] = 1
         print(answer)
         file.close()

def fileOverlap():
    with open('happynums.txt', 'r') as file1:
        data = file1.read().splitlines()
        file1.close()
    with open('primes.txt', 'r') as file2:
        data2 = file2.read().splitlines()
        file2.close()
    answer = [int(x) for x in data if x in data2]
    print(answer)

def horizLine(board_size):
    print('---' * board_size)

def verticalLine(board_size):
    print('|  ' * (board_size + 1))

def printGameBoard():
    try:
        size = int(input('How big would you like the board to be? \n '))
        for i in range(size):
            horizLine(size)
            verticalLine(size)
    except ValueError as e:
        print(e)

def checkTicTacToeWinner():
    '''
    winner_is_2 = [[1,0,0],
                    [], []]
    '''



if __name__ == '__main__':
    printGameBoard()
