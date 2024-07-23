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


for item in range(0, 2):
    integer = int_check(question="Integer: ", low=0)
    print(integer)

print()

for item in range(0, 2):
    height = int_check(question="Height: ", low=1)
    print(height)


print()

for item in range(0, 2):
    width = int_check(question="Width: ", low=1)
    print(width)