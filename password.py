import random
import string

charVal = string.ascii_letters + string.digits + string.punctuation
pass_len = 12

# password = ""
# for i in range(pass_len):
#     password += random.choice(charVal)


# using list comprehension
password = "".join([random.choice(charVal) for i in range(pass_len)])
print("Your random password is: " , password)