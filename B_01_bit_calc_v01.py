# asks user for file type (integer / image / text / xxx)

def get_filetype():
    while True:
        response = input("File Type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check of it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check of it's an image
        elif response in ['image', 'img', "picture", "p"]:
            return "image"

        # check of it's a text document
        elif response in ['text', 'txt', 't']:
            return "text"

        # if response invalid output error
        else:
            print("Please enter a valid file type")

# Generates a title


def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

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
    return answer

# Ask user for width until they enter a number larger than zero


def int_check(question, low):

    error = f"please input a number larger that is more than or equal to {low}"

    while True :

        try:
            # ask user for a number
            response = int(input(question))

            # check that number is more than zero
            if response >= low:
                return response
            else:
                print(error)
        # checks that number is valid
        except ValueError:
            print(error)

# calculates the number of bits in an image


def image_calc():
    width = int_check(question="Width: ", low=1)
    print()
    height = int_check(question="Height: ", low=1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    # setup answer and return it
    answer = f"Number of pixels: {width} x {height} = {num_pixels} \nNumber of bits: {num_pixels} x 24 = {num_bits}"

    return answer

# calculates how many bits are needed to represent an integer


def integer_calc():
    integer = int_check(question="Integer: ", low=0)

    # convert the integer into binary

    raw_binary = bin(integer)

    # remove the 0b
    bin_integer = raw_binary[2:]
    bit_length = len(bin_integer)

    # setup answer and return it
    answer = f"{integer} in binary is {bin_integer}. We need {bit_length} bits to represent it."

    return answer

# Asks user if they want to see the instructions


def instructions():
    statement_generator(statement="Instructions", decoration="-")

    print('''- Type in the file type you'd like to calculate bits from (e.g image, text, integer)
- Type in the dimensions of the image, or the text/integer you'd like to calculate
- If you want to stop the program, type "xxx" when it asks you for a file type.''')


# main routine goes here

statement_generator("BIT CALCULATOR", "~")

# asks if the user wants to see the instructions
want_instructions = input("\nPress <enter> to read the instructions or any key to continue ")

# if they press enter without typing anything extra, display instructions
if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        print("Thank you for using the bit calculator")
        break

    # check if the response I is an image or an integer
    if file_type == 'i':

        correct_file = input("Press <enter> to select integer or any key to select image as your file type ")
        if correct_file == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"file type selected is {file_type}")

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
        print()
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
        print()
    elif file_type == "text":
        text_ans = calc_text_bits()
        print(text_ans)
        print()


