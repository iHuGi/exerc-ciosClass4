# Without Return
print("-> Without Return <-")
def person_gender(gender):
    gender = gender.lower().lstrip().strip()
    if gender == 'male':
        print('Your gender is Male')
    elif gender == 'female':
        print('You are a Female')
    else:
        print('Invalid Gender')

user_gender = input('What is your gender? ')
person_gender(user_gender)

print("")
print("-> With Return <-")

# With Return
def person_gender(gender):
    gender = gender.lower().lstrip().strip()
    if gender == 'male':
        return 'Male'
    elif gender == 'female':
        return 'Female'
    else:
        return 'Invalid Gender'

user_gender = input('What is your gender? ')
result = person_gender(user_gender)
print('Your gender is', result)

print("")
print(" -> M or F <-")

# With M or F
def person_gender(gender):
    gender = gender.strip().lstrip() 
    if gender == 'M':
        return 'Male'
    elif gender == 'F':
        return 'Female'
    else:
        return 'Invalid Gender'

while True:
    user_gender = input('What is your gender (F/M)? ')
    if user_gender.upper() in ('F', 'M'):
        result = person_gender(user_gender.upper())
        print('Your gender is', result)
        break
    else:
        print('Please enter either "F" or "M".')

print("")
print("-> Menu <-")

# With M or F but with more options
def menu_to_display():
    # User options to choose from
    print("Gender Menu:")
    print("1. Male (Enter 'M')")
    print("2. Female (Enter 'F')")
    print("3. Exit (Enter 'Q')")

# Unlimited choices (While True), user can leave the console by entering Q to exit
while True:
    menu_to_display()
    choice = input("Enter your choice: ").lstrip().strip().upper()

    if choice == 'M':
        print('Your gender is Male')
    elif choice == 'F':
        print('You are a Female')
    # Print Goodbay and Break out of the loop if the user enters Q
    elif choice == 'Q':
        print('Goodbye!')
        break 
    else:
        print('Invalid choice. Please select a valid option.')
