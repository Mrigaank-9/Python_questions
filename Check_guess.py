def check_guess(input_by_user, random_char_selected): 
    if(input_by_user == random_char_selected):
        print("\nThe Character Guessed correctly  ")
        return 0 
    elif(input_by_user<random_char_selected):
        print("\nThe Character is greater than the Guessed Charcter")
        return -1
    else:
        print("\nThe Character is Smaller than the Guessed Charcter ")
        return 1 
    