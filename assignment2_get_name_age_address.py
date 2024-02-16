print("\033[1;34;40mHi there! My name's Ella, may I now yours?")
def valid_name(prompt):
    while True:
        name = input(prompt)
        if not any(char.isdigit() for char in name):
            return name
        else:
            print("\033[1;31;40mInvalid name. Please enter a valid name without numbers")
firstname = valid_name("\033[1;30;40mPlease enter your first name: ")
middlename = valid_name("please enter your middle name: ")
surname = valid_name("Please type in your surname: ")
full_name = (f"{firstname} {middlename} {surname}")
print("\n\033[1;34;40mNice to meet you " + full_name + "!", "\nI'll be calling you by your given name then, " + firstname + ".")

print("\n\033[1;35;40mOh yeah, if you don't mind me asking, how old are you? ")
def user_age():
    age = input("Please enter your age: ")
    while not age.isdigit() or int(age) <= 3 or int(age) >+ 120:
        print("\033[1;31;40mInvalid age. Please enter a valid age number.")
        age = input("\033[1;35;40mPlease enter your age: ")
    
    if int(age) > 18:
        print("\033[1;35;40mSo you're my elder, I shall treat you with respect!")
    elif int(age) == 18:
        print("\033[1;35;40mOh my, we're the same age! Let's get along!")
    else:
        print("\033[1;35;40mSo you're " + age + ", I see. It seems you're younger than me, you can rely on me then!")
user_age()

print("\n\033[1;33;40mI'd like to know where you live as well, can you please tell me your address?")
def get_valid_input(prompt, error_message):
    while True:
        address = input(prompt)
        if not any(char.isdigit() for char in address):
            return address
        else:
            print(error_message)

def user_address():
    region = get_valid_input("\033[1;30;40mEnter your region: ", "\033[1;31;40mRegion cannot contain numbers. Please enter a valid input.")
    province = get_valid_input("\033[1;30;40mEnter your province: ", "\033[1;31;40mProvince cannot contain numbers. Please enter a valid input.")
    municipality = get_valid_input("\033[1;30;40mEnter your municipality: ", "\033[1;31;40mMunicipality cannot contain numbers. Please enter a valid input.")
    barangay = get_valid_input("\033[1;30;40mEnter your Barangay: ", "\033[1;31;40mBarangay cannot contain numbers. Please enter a valid input.")
    street_name_number = input("\033[1;30;40mEnter your street name and number: ")
    
    full_address = f"{street_name_number}, {barangay}, {municipality}, {province}, {region}"
    print("Full Address: " + full_address)
user_address()

print("\n\033[1;33;40mSo that's your address, I'll be sure to keep it in mind, " + firstname + "!")
print("It was nice meeting you, thank you so much for your time, see ya!\n")