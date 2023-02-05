file_path = 'text_folder/pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your bithday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
