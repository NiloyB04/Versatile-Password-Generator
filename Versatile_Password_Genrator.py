import random
import string
import time
print("Are you someone who has the same password for everything?\nAre you afraid of getting hacked or having insecure passwords?\nWorry no longer! This usefull tool will generate 10 unique passwords according to your specifications!\nNow lets get started!")
time.sleep(5)
password = []
alphabet_uppercase = list(string.ascii_uppercase)
alphabet_lowercase = list(string.ascii_lowercase)
digits = list(string.digits)
special_characters = list("!@#$%^&*")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
length = int(input("How long must the password be, please enter an integer: "))
alphabets_count = int(input("Enter minimum alphabetical letters required: "))
digits_count = int(input("Enter minimum number of digits required: "))
special_characters_count = int(input("Enter minimum number of special characters required: "))
characters_count = alphabets_count + digits_count + special_characters_count
def generate_password():
    if characters_count > length:
        print("Characters total count is greater than the password length")
        return
    for i in range(alphabets_count):
        password.append(random.choice(alphabet_lowercase + alphabet_uppercase))
    for i in range(digits_count):
        password.append(random.choice(digits))
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)
    print("Here are 10 possible passwords for you!:")
    print("".join(password))
    password.clear()

generate_password()
generate_password()
generate_password()
generate_password()
generate_password()
generate_password()
generate_password()
generate_password()
generate_password()
generate_password()
