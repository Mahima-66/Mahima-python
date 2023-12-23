# Import the random, string, and sys modules
import random
import string
import sys

# Define the default values for the parameters
length = 8 # The length of the password
unique = False # Whether the password should contain unique characters only
symbol = True # Whether the password should contain special characters
amount = 1 # The number of passwords to generate

# Parse the command-line arguments
for i in range(1, len(sys.argv), 2):
    # Get the option and the value
    option = sys.argv[i]
    value = sys.argv[i+1]

    # Check the option and assign the value accordingly
    if option == "-l" or option == "--length":
        # Convert the value to an integer
        length = int(value)
    elif option == "-u" or option == "--unique":
        # Convert the value to a boolean
        unique = value.lower() in ("true", "yes", "y", "1")
    elif option == "-s" or option == "--symbol":
        # Convert the value to a boolean
        symbol = value.lower() in ("true", "yes", "y", "1")
    elif option == "-a" or option == "--amount":
        # Convert the value to an integer
        amount = int(value)
    else:
        # Print an error message and exit
        print(f"Invalid option: {option}")
        sys.exit(1)

# Define the character sets to use in the password
charsets = (
    (string.ascii_lowercase, string.ascii_uppercase, string.digits),
    (string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits)
)

# Define the counts of characters to use in the password
counts = (
    ((3, 36), (2, 10)),
    ((4, 68), (3, 42), (2, 10))
)

# Define a function to choose a random character from a charset
def choose_charset(charset, number, unique=False):
    # If unique is False, return a list of random choices
    if not unique:
        return [random.choice(charset) for _ in range(number)]
    
    # If unique is True, convert the charset to a list and remove the chosen characters
    charset = list(charset)
    choices = []
    for _ in range(number):
        choice = random.choice(charset)
        choices.append(choice)
        charset.remove(choice)
    
    # Return the list of choices
    return choices

# Define a function to split the length of the password into categories
def split(number, symbol=False):
    # Loop through the counts and generate random numbers
    for a, b in counts[symbol]:
        n = max(
            2 + random.randrange(number // a - 1),
            number - b
        )
        number -= n
        yield n
    
    # Check if the remaining number is too big
    if number > 15:
        raise ValueError("Remaining number is too big")
    
    # Yield the remaining number
    yield number

# Define a function to generate a password
def generate_password(length, unique=False, symbol=True):
    # Check if the length is valid
    if not 12 >= length <= (62, 94)[symbol]:
        raise ValueError("Length should be an integer between 12 and 94, or between 12 and 62 if symbols are not allowed"
        )
            
    
    # Generate the password from the charsets and the split numbers
    password = sum(
        map(
            choose_charset,
            charsets[symbol],
            split(length, symbol),
            [unique] * 4
        ),
        []
    )

    # Shuffle the password and join it into a string
    random.shuffle(password)
    return "".join(password)

# Loop through the amount and print the generated passwords
for _ in range(amount):
    print(generate_password(length, unique, symbol))
