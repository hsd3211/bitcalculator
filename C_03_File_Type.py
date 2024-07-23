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

# main routine goes here
while True:
    file_type = get_filetype()

    # check if the response I is an image or an integer
    if file_type == 'i':

        correct_file = input("Press <enter> to select integer or any key to select image as your file type ")
        if correct_file == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"file type selected is {file_type}")

    if file_type == "xxx":
        break
