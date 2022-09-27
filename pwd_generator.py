import secrets
import string


letter = string.ascii_letters # concatenation of letters lowercase and uppercase
digits = string.digits # the string containing the numbers 0 to 9:
special_char = string.punctuation #  constant is the string of all special characters

alphabet = letter + digits + special_char # concatenate the above string constants to get the alphabet.

pwd_lenght = 12 # the password string is of length 12



while True: # infinite loop
  pwd = ''
  for i in range(pwd_lenght):
    pwd += ''.join(secrets.choice(alphabet))
  
  if (any(char in special_char for char in pwd) and sum(char in digits for char in pwd)>=2):
    break

print(pwd)