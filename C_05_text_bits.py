# Calculates number of bits needed to represent text in ascii
def calc_text_bits():

    # get text from user
    response = input("Enter some text: ")

    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # set up answer and return it
    answer = f"{response} has {num_chars} characters." \
             f" \nWe need {num_chars} x 8 bits to represent it which is {num_bits} bits"
    print(answer)




# main routine goes here
text_ans = calc_text_bits()