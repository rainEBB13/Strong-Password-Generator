import os
import secrets
import string
from cryptography.fernet import Fernet

def creating_a_password(size_of_strength_password):
    password = ""
    for i in range(size_of_strength_password):
        # Alphabet = 0, Numbers = 1, Symbols = 2.
        random_temporary_number = random_generator.randrange(3)
        if random_temporary_number == 0:
            password += random_generator.choice(alphabet)
        elif random_temporary_number == 1:
            password += random_generator.choice(numbers)
        elif random_temporary_number == 2:
            password += random_generator.choice(symbols)
    return password


def confering_strong_password(password, size_of_strength_password):
    while True:
        ok1 = False
        if (any(alphabet for k in password)
                and any(numbers for k in password)
                and any(symbols for k in password)):
            ok1 = True
    
        size_of_password = len(password)
        character = {
            "lower_letter": 0, 
            "upper_letter": 0,
            "numbers": 0,
            "symbols":0
        }
        min_distribution = 0.1 * size_of_password
        max_distribution = 0.4 * size_of_password

        for i in password:
            if i in alphabet and i.islower():
                character["lower_letter"] += 1
            elif i in alphabet and i.isupper():
                character["upper_letter"] += 1
            elif i in numbers:
                character["numbers"] += 1
            elif i in symbols:
                character["symbols"] += 1
    
        ok2 = False
        if ((character["lower_letter"] >= min_distribution
                    and character["lower_letter"] <= max_distribution)
                        and (character["upper_letter"] >= min_distribution
                            and character["upper_letter"] <= max_distribution)
                        and (character["numbers"] >= min_distribution
                            and character["numbers"] <= max_distribution)
                        and (character["symbols"] >= min_distribution
                            and character["symbols"] <= max_distribution)):
                    ok2 = True
    
        if ok1 and ok2:
            break

        password = creating_a_password(size_of_strength_password)

    return password


def confering_the_strength(password):
    size_of_password = len(password)
    character = {
        "lower_letter": 0, 
        "upper_letter": 0,
        "numbers": 0,
        "symbols":0
    }
    min_distribution = 0.1 * size_of_password
    max_distribution = 0.4 * size_of_password

    for i in password:
        if i in alphabet and i.islower():
            character["lower_letter"] += 1
        elif i in alphabet and i.isupper():
            character["upper_letter"] += 1
        elif i in numbers:
            character["numbers"] += 1
        elif i in symbols:
            character["symbols"] += 1
    
    if size_of_password < 8:
        return 1
    elif size_of_password >= 8 and size_of_password < 10:
        if (character["lower_letter"] == size_of_password
                or character["upper_letter"] == size_of_password
                or character["numbers"] == size_of_password
                or character["symbols"] == size_of_password):
            return 1
        else:
            return 2
    elif size_of_password >= 10 and size_of_password < 12:
        if (character["lower_letter"] == size_of_password
                or character["upper_letter"] == size_of_password
                or character["numbers"] == size_of_password
                or character["symbols"] == size_of_password):
            return 1
        elif (character["lower_letter"] > 0
                and character["upper_letter"] > 0
                and character["numbers"] > 0
                and character["symbols"] > 0):
            return 3
        else:
            return 2
    elif size_of_password >= 12:
        if (character["lower_letter"] == size_of_password
                or character["upper_letter"] == size_of_password
                or character["numbers"] == size_of_password
                or character["symbols"] == size_of_password):
            return 1
        elif (character["lower_letter"] > 0
                and character["upper_letter"] > 0
                and character["numbers"] > 0
                and character["symbols"] > 0):
            if ((character["lower_letter"] >= min_distribution
                 and character["lower_letter"] <= max_distribution)
                    and (character["upper_letter"] >= min_distribution
                        and character["upper_letter"] <= max_distribution)
                    and (character["numbers"] >= min_distribution
                        and character["numbers"] <= max_distribution)
                    and (character["symbols"] >= min_distribution
                        and character["symbols"] <= max_distribution)):
                return 4
            else:
                return 3
        else:
            return 2


def create_key():
    key = Fernet.generate_key()
    return key


def encrypt(password, key):
    password = password.encode()
    encrypt_password = Fernet(key).encrypt(password)
    encrypt_password = encrypt_password.decode()
    return encrypt_password


def decrypt(password, key):
    password = password.encode()
    decrypt_password = Fernet(key).decrypt(password)
    decrypt_password = decrypt_password.decode()
    return decrypt_password

# MAIN FUNCTION
# Language selection menu
print("#----------------------------------------------------#")
print("Select Language:")
print("1. Portuguese")
print("2. English")
print("#----------------------------------------------------#")
print()

language = int(input("Choose your language (1/2): "))

if language == 1:
    # Portuguese Menu
    print("#----------------------------------------------------#")
    print('# MENU DO PROJETO "STRONG-PASSWORD-GENERATOR":"')
    print("    1. Conferir a força de uma senha qualquer.")
    print("    2. Gerar uma senha forte aleatória.")
    print("    3. Gerar uma senha forte criptografada.")
    print("    4. Descriptografar uma senha.")
    print("    5. Criptografar uma senha com uma chave específica.")
    print("#----------------------------------------------------#")
    print()
elif language == 2:
    # English Menu
    print("#----------------------------------------------------#")
    print('# MENU FOR THE PROJECT "STRONG-PASSWORD-GENERATOR":')
    print("    1. Check the strength of any password.")
    print("    2. Generate a random strong password.")
    print("    3. Generate an encrypted strong password.")
    print("    4. Decrypt a password.")
    print("    5. Encrypt a password with a specific key.")
    print("#----------------------------------------------------#")
    print()

# Creating an instance of SystemRandom
random_generator = secrets.SystemRandom()

alphabet = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

user_input = int(input("Choose an option (1/2/3/4/5): "))

entrada_valida = False
while not entrada_valida:
    match user_input:
        case 1:
            entrada_valida = True
            senha_do_usuario = input("Digite a senha (Digit the password): ")
            password_strength = confering_the_strength(senha_do_usuario)
            if password_strength == 1:
                print("Nível 1: Fraca (Weak)\n")
            elif password_strength == 2:
                print("Nível 2: Moderada (Moderate)\n")
            elif password_strength == 3:
                print("Nível 3: Semi-Forte (Semi-Strong)\n")
            elif password_strength == 4:
                print("Nível 4: Forte (Strong)\n")
        case 2:
            entrada_valida = True
            print()
            print("Português: Qual tamanho você deseja (Obrigatório 16+ caracteres)? ")
            print("English: What size you wish (Mandatory 16 characters or more)? ")
            size_of_strength_password = int(input("R = "))
            while size_of_strength_password < 16:
                print("Português: Entrada inválida. A senha deve conter 16 ou mais caracteres!")
                print("English: Invalid input. The password must contain 16 characters or more!")
                size_of_strength_password = int(input("Digite um tamanho válido (Digit a valid size): "))
            password = creating_a_password(size_of_strength_password)
            password_confered = confering_strong_password(password, size_of_strength_password)
            print("A senha forte criada é (The strong password created is): {0}".format(password_confered))
        case 3:
            entrada_valida = True
            print()
            print("Português: Qual tamanho você deseja (Obrigatório 16+ caracteres)? ")
            print("English: What size you wish (Mandatory 16 characters or more)? ")
            size_of_strength_password = int(input("R = "))
            while size_of_strength_password < 16:
                print("Português: Entrada inválida. A senha deve conter 16 ou mais caracteres!")
                print("English: Invalid input. The password must contain 16 characters or more!")
                size_of_strength_password = int(input("Digite um tamanho válido (Digit a valid size): "))
            password = creating_a_password(size_of_strength_password)
            key = create_key()
            print()
            print("Português: Atenção, a chave de criptografia usada é de extrema importância. Guarde-a com todo o cuidado possível!")
            print("English: Attention, the encryption key used is extremely important. Keep it with the utmost care!\n")
            print("Key: {0}".format(key))
            encrypt_password = encrypt(password, key)
            print("Senha criptografada (Encrypted password): {0}".format(encrypt_password))
        case 4:
            entrada_valida = True
            print()
            password = input("Por favor, digite a senha criptografada (Please, enter the encrypted password): ")
            key = input("Por favor, digite a chave de criptografia dentro de b' ' (Please, enter the encryption key inside b' '): ")
            decrypt_password = decrypt(password, key)
            print()
            print("Password: {0}".format(decrypt_password))
        case 5:
            entrada_valida = True
            password = input("Por favor, digite a senha (Please, enter the password): ")
            key = input("Por favor, digite a chave de criptografia dentro de b' ' (Please, enter the encryption key inside b' '): ")
            encrypt_password = encrypt(password, key)
            print("Senha criptografada (Encrypted password): {0}".format(encrypt_password))
        case _:
            print("Português: Entrada inválida. Por favor, digite 1, 2, 3, 4 ou 5 para uma entrada válida.")
            print("English: Invalid input. Please, enter 1, 2, 3, 4 or 5 for a valid input.")
            user_input = int(input("Escolha uma opção (1/2/3/4/5): "))

#--------------------------------------------------------------------------
