#!/usr/bin/python3
from hashlib import pbkdf2_hmac

lower_case_letters = list("abcdefghijklmnopqrstuvwxyz")
upper_case_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
special_characters = list("#!"§$%&/()=?`':;_–…∞*#")
password_characters = lower_case_letters + upper_case_letters + numbers + special_characters
salt = "pepper"
def convert_bytes_to_password (hashed_bytes, length):
                          number = int.from_byts (hashed_bytes, byteorder = "big")
                          password = ""
                          while number >0 and len(password) < length :
                          password = password + password_charcters [number % len(password_characters)]
                          number = number // len(password_characters)
                          return password
                          
