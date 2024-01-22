def count_letters(user_input):
    letter_count = {}

    for char in user_input:
       
        if char.isalpha() and not char.isspace(): # check if character is a letter or not space
            # turn char into lowercase letter
            lowercase_char = char.lower()

            # add char to letter_count
            letter_count[lowercase_char] = letter_count.get(lowercase_char, 0) + 1

    return letter_count

user_input = input("Enter a string: ")

result_dict = count_letters(user_input)

print(result_dict)