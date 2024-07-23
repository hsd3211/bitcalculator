# generates headings (e.g: ----- Heading ----- )
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator(statement="Instructions", decoration="-")

    print('''
Instructions go here.
- instruction 1
- instruction 2
etc''')

# main routine goes here


# asks if the user wants to see the instructions
want_instructions = input("\nPress <enter> to read the instructions or any key to continue ")

# if they press enter without typing anything extra, display instructions
if want_instructions == "":
    instructions()

print("program continues")