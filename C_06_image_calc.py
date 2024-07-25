# Ask user for width until they enter a number larger than zero

def int_check(question, low):

    error = f"please input a number larger that is more than or equal to {low}\n"

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

# Main routine goes here


# calculates how many bits are needed to represent an integer
def image_calc():
    height = int_check(question="Height: ", low=1)
    width = int_check(question="Width: ", low=1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    # setup answer and return it
    answer = f"Number of pixels: {width} x {height} = {num_pixels} \nNumber of bits: {num_pixels} x 24 = {num_bits}"

    return answer

# main routine goes here
image_ans = image_calc()
print(image_ans)