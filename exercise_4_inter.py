def valid_integer_input(prompt, index):
    while True:
        try:
            prompt_message = prompt + " #" + str(index + 1) + ": " # to create correct output that increases index
            return int(input(prompt_message))
        except ValueError: # if invalid, print this
            print("Invalid input. Please enter an int.")

sum_result = 0

# get 5 valid integers from the user 
for i in range(5):
    user_input = valid_integer_input("Enter int", i)
    sum_result += user_input


print("Your sum is", sum_result)
