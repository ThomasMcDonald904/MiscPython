import secrets
import bcrypt as bcrypt
import pandas as pd
import logging

logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S', filename="data.log")

supposedly_secret_pepper = b'zs0\x84\xbe\x02\xec\xa2\xbc\xae$\xa3\x8ei\x81d'


def generate_new_user(_username, pepper):
    logging.info(f"New user {_username}")
    password = input("Entrée votre nouveau mot de passe: ").encode("UTF-8")

    full_pass = pepper + password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(full_pass, salt)
    user_data_line = f"\n{_username}:{salt}:{hashed_password}"

    userdata = open("userdata.txt", "a+")
    userdata.write(user_data_line)


def check_user(_data, _username):
    password = input("Entrée votre mot de passe: ")
    hashed_password = _data.loc[_username]
    # result = bcrypt.checkpw(password, hashed_password)
    print(hashed_password)

try:
    data = pd.read_csv("userdata.txt", sep=":")
except pd.errors.EmptyDataError:
    logging.info("No user data created yet, caught 'EmptyDataError'")

print("Bonjour, bienvenue à la banque GROSSE-COMPANIE")
customer_status = input("Êtes-vous nouveau à la compagnie (Y/N): ")
if customer_status.lower() == "y":
    username = input("Entrée votre nouveau nom utilisateur: ")
    if data['username'].str.contains(username).any():
        print("Votre compte existe déjà")
        check_user(data)
    else:
        generate_new_user(username, supposedly_secret_pepper)
else:
    username = input("Entrée votre nom utilisateur: ")
    if data['username'].str.contains(username).any():
        check_user(data, username)
    else:
        print("Ce compte n'existe pas", "Crée en un", sep="\n")
        generate_new_user(username, supposedly_secret_pepper)
