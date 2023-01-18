import random
import re
import datetime


def game_name():
    # Game header GUI
    print('\n\n*********** LUCKY NUMBER GAME ***********')



def get_name():
    # Players full name
    first_name = input('Please enter your first name: ').strip()
    last_name = input('Now, write your family name: ').strip()
    return first_name + ' ' + last_name


def validate_name(full_name):
    is_valid = True
    # First check so neither firstname or family name is empty
    #if full_name[0] == " " or full_name[-1] == " ":
        #print('Make sure you write both your first and last name, try again....')
        #is_valid = False
    #else:
        # Check that name is written with valid characters
    check_format = re.match('^[a-zåäöé]+ [a-zåäöé]+$', full_name, flags=re.IGNORECASE)
    if check_format is None:
        print('Something went wrong, you can only use letters for your name!!!\n'
            'And you have to wright both a first AND last name, try again.....')
        is_valid = False
    return is_valid



def get_birthdate():
    birthdate = input("Enter birthdate in the format 'yyyymmdd': ").strip()
    return birthdate


def validate_birthdate(birthdate):
    # Split birthdate into components
    year = birthdate[:4]
    month = birthdate[4:6]
    day = birthdate[6:8]
    is_valid = True
    # Check with datetime if it's a valid date
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print("Wrong format, try again 'yyyymmdd'!!!")
        is_valid = False
    return is_valid



def get_age(birthdate):
    # Get today from datetime
    today = datetime.date.today()

    # Check if player will have or already had his birthday
    one_or_zero = ((today.month, today.day) < (int(birthdate[4:6]), int(birthdate[6:8])))

    year_difference = today.year - int(birthdate[:4])
    # Return age corrected for if player had his birtday this year or not
    return year_difference - one_or_zero


def validate_age(player_age):
    # Player has to be atleast 18 to play
    if player_age < 18:
        print("Sorry you're too young to play, please update your birthdate!")
        return False
    else:
        return True



def generate_lucky_list():
    # Empty lucky list and create new
    lucky_list.clear()
    for _ in range(9):
        # Make sure no duplicates
        valid = True
        while True:
            new_number = random.randrange(101)
            for number in lucky_list:
                if new_number == number:
                    valid = False
                    break
                else:
                    valid = True
            if valid:
                break
        lucky_list.append(new_number)
    return lucky_list


def generate_lucky_number(lucky_list):
    # Make sure lucky number not already in lucky list
    while True:
        lucky_number = random.randrange(101)
        for number in lucky_list:
            if lucky_number == number:
                valid = False
                break
            else:
                valid = True
        if valid:
            break
    return lucky_number


def print_list(num_list):
    # This list will be lucky list or shorter list after shorter_lucky_list function
    text_list = ''
    for num in num_list:
        text_list += str(num) + ' '
    return f'Choose a number from the following list: {text_list}'


def get_input(num_list):
    # User input validated directly with type cast, numeric range and in lucky list
    while True:
        try:
            player_input = int(input("Your input: "))
        except ValueError:
            print('Not a valid number, try again...')
        else:
            if -1 < player_input < 101:
                if player_input in num_list:
                    break
                else:
                    print('Not in the list! Choose a number from the list please...')
            else:
                print('It has to be a number from 0 to and including 100, try again...')
    return player_input

'''
def shorter_lucky_list(lucky_list, lucky_number, num_of_attempts, player_input):
    # After first wrong guess, list will be shorten by numeric range +/- 10
    if num_of_attempts == 1:
        for num in lucky_list:
            if num < lucky_number - 10 or num > lucky_number + 10:
                lucky_list.remove(num)
        return lucky_list
    else:
        # Second and following attempts, the wrong number guessed will be removed
        lucky_list.remove(player_input)
    return lucky_list

'''
def shorter_lucky_list(lucky_list, lucky_number, num_of_attempts, player_input):
    # Local variable
    shorter_lucky_list = []
    # After first wrong guess, list will be shorten by numeric range +/- 30
    if num_of_attempts == 1:
        lucky_list.remove(player_input)
        for num in lucky_list:
            if num >= lucky_number - 30 and num <= lucky_number + 30:
                shorter_lucky_list.append(num)
    else:
        # Second and following attempts, the wrong number guessed will be removed
        lucky_list.remove(player_input)
        shorter_lucky_list = lucky_list
    return shorter_lucky_list

    
def let_the_game_begin(player_name):
    # GUI game description
    print(f'\n*********** Let the game begin ***********\nHi {player_name} :-)\n'
          'The computer will generate a list of ten numbers ranging'
          ' from 0 to 100. One of the numbers is the "Lucky number"\n'
          'Try to find it!!! For every try the range will narrow down....\n'
          'When the list only contains two numbers, you will loose!')


def game_logic(lucky_list, lucky_number, player_name):
    # Print list and takes players input
    num_of_attempts = 0
    print("Now it's time for you to play!")
    while True:
        num_of_attempts += 1
        print(f"\n{print_list(lucky_list)}")
        player_input = get_input(lucky_list)

        # Now let us score player input
        # If player choose correct number
        if player_input == lucky_number:
            print(f'Congrats, game is over! And you got lucky number {lucky_number} from try {num_of_attempts} :)')
            break
        else:
            # If player choose wrong number
            print("Unfortunately you didn't choose the 'lucky number'.", end=" ")
            lucky_list = shorter_lucky_list(lucky_list, lucky_number, num_of_attempts, player_input)
            # When there's only two numbers left in lucky list
            if len(lucky_list) <= 2:
                print(f"Sorry {player_name.split()[0]}, as there are only two or less numbers left you loose :-( "
                      f"The 'lucky number' was {lucky_number} !!!")
                break
            print("Try again from a narrower list...")


def play_again(player_name):
    player_choice = bool
    # GUI play again?
    re_run = input(f"\nSo {player_name.split()[0]}, do you like to play again? (Input y: Yes, and n:NO): ").strip()
    # The loop will validate input by only checking first character
    while True:
        if re_run[0].lower() == 'y':
            player_choice = True
            break
        elif re_run[0].lower() == 'n':
            player_choice = False
            break
        else:
            re_run = input("Try to enter JUST 'y' or 'n': ").strip()
    return player_choice

# 'Main' section to be run
if __name__ == "__main__":
    # Global variable
    lucky_list = []

    game_name()

    # Loop will continue until player inputs are correct
    while True:
        player_name = get_name()
        if validate_name(player_name):
            break
    
    # Loop will continue until age 18 or older
    while True:
        # Loop will continue until player inputs are correct format
        while True:
            birthdate = get_birthdate()
            if validate_birthdate(birthdate):
                break
        player_age = get_age(birthdate)
        if validate_age(player_age):
            break
    
    # Loop will continue until player choose 'no' when asked to play again
    while True:
        # Generate lucky list and number
        lucky_list = generate_lucky_list()
        lucky_number = generate_lucky_number(lucky_list)
        lucky_list.append(lucky_number)
        # Shuffle list to not display lucky number last
        random.shuffle(lucky_list)

        # Start of game
        let_the_game_begin(player_name)
        # Game logic
        game_logic(lucky_list, lucky_number, player_name)
        # Play again?
        if not play_again(player_name):
            raise exit()
