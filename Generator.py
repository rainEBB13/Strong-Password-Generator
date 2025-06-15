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

def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")

# MAIN FUNCTION
# Language selection menu
print("#----------------------------------------------------#")
print("Select Language:")
print("1. Portuguese")
print("2. English")
print("3. Spanish")
print("#----------------------------------------------------#")
print()

language = int(input("Choose your language (1/2/3): "))

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
elif language == 3:
    # Spanish Menu
    print("#----------------------------------------------------#")
    print('# MENU DEL PROYECTO "STRONG-PASSWORD-GENERATOR":')
    print("    1. Comprueba la fortaleza de cualquier contraseña.")
    print("    2. Genera una contraseña segura y aleatoria.")
    print("    3. Genera un contraseña segura y cifrada.")
    print("    4. Descifra una contraseña.")
    print("    5. Cifra una contraseña con una llave específica.")
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
            if language == 1:
                senha_do_usuario = input("Digite a senha: ")
            if language == 2:
                senha_do_usuario = input("Digit the password: ")
            if language == 3:
                senha_do_usuario = input("Introduce la contraseña: ")
            password_strength = confering_the_strength(senha_do_usuario)
            if password_strength == 1:
                if language == 1:
                    print("Nível 1: Fraca\n")
                if language == 2:
                    print("Level 1: Weak\n")
                if language == 3:
                    print("Nivel 1: Débil\n")
            elif password_strength == 2:
                if language == 1:
                    print("Nível 2: Moderada\n")    
                if language == 2:
                    print("Level 2: Moderate\n")
                if language == 3:
                    print("Nivel 2: Moderado\n")            
            elif password_strength == 3:
                if language == 1:
                    print("Nível 3: Semi-Forte\n")
                if language == 2:
                    print("Level 3: Semi-Strong\n")
                if language == 3:
                    print("Level 3: Semi-Fuerte\n")
            elif password_strength == 4:
                if language == 1:
                    print("Nível 4: Forte\n")
                if language == 2:
                    print("Level 4: Strong\n")
                if language == 3:
                    print("Nivel 4: Fuerte\n")
        case 2:
            entrada_valida = True
            print()
            if language == 1:
                print("Português: Qual tamanho você deseja (Obrigatório 16+ caracteres)? ")
            if language == 2:
                print("English: What size you wish (Mandatory 16 characters or more)? ")
            if language == 3:
                print("Español: Qué tamaño deseas (Obligatorio 16 caracteres o mas)? ")
            size_of_strength_password = int(input("R = "))
            while size_of_strength_password < 16:
                if language == 1:
                    print("Português: Entrada inválida. A senha deve conter 16 ou mais caracteres!")
                    size_of_strength_password = int(input("Digite um tamanho válido: "))
                if language == 2:
                    print("English: Invalid input. The password must contain 16 characters or more!")
                    size_of_strength_password = int(input("Digit a valid size: "))
                if language == 3:
                    print("Español: Entrada invalida. La contraseña debe contener 16 caracteres o más!")
                    size_of_strength_password = int(input("Introduzca un tamaño válido: "))
            password = creating_a_password(size_of_strength_password)
            password_confered = confering_strong_password(password, size_of_strength_password)
            if language == 1:
                print("A senha forte criada é: {0}".format(password_confered))
                save_option = input("Você deseja salvar essa senha em um arquivo? (sim/nao): ").strip().lower()
            if language == 2:
                print("The strong password created is: {0}".format(password_confered))
                save_option = input("Do you want to save the password to a file? (yes/no): ").strip().lower()
            if language == 3:
                print("La contraseña segura creada es: {0}".format(password_confered))
                save_option = input("Quieres guarda la contraseña en un archivo? (si/no): ").strip().lower()
            if save_option == 'yes' or save_option == 'sim' or save_option == 'si':
                save_password_to_file(password_confered)
                if language == 1:
                    print("Sua senha foi salva em um arquivo.")
                if language == 2:
                    print("Password has been saved to file.")
                if language == 3:
                    print("La contraseña ha sido guardada en un archivo.")
        case 3:
            entrada_valida = True
            print()
            if language == 1:
                print("Português: Qual tamanho você deseja (Obrigatório 16+ caracteres)? ")
            if language == 2:
                print("English: What size you wish (Mandatory 16 characters or more)? ")
            if language == 3:
                print("Español: Qué tamaño deseas (Obligatorio 16 caracteres o mas)? ")
            size_of_strength_password = int(input("R = "))
            while size_of_strength_password < 16:
                if language == 1:
                    print("Português: Entrada inválida. A senha deve conter 16 ou mais caracteres!")
                    size_of_strength_password = int(input("Digite um tamanho válido: "))
                if language == 2:
                    print("English: Invalid input. The password must contain 16 characters or more!")
                    size_of_strength_password = int(input("Digit a valid size: "))
                if language == 3:
                    print("Español: Entrada invalida. La contraseña debe contener 16 caracteres o más!")
                    size_of_strength_password = int(input("Introduzca un tamaño válido: "))
            password = creating_a_password(size_of_strength_password)
            key = create_key()
            print()
            if language == 1:
                print("Português: Atenção, a chave de criptografia usada é de extrema importância. Guarde-a com todo o cuidado possível!")
            if language == 2:
                print("English: Attention, the encryption key used is extremely important. Keep it with the utmost care!\n")
            if language == 3:
                print("Español: Atención, la llave de cifrado es extremadamente importante. Guardala en un sitio seguro!\n")
            print("Key: {0}".format(key))
            encrypt_password = encrypt(password, key)
            if language == 1:
                print("Senha criptografada: {0}".format(encrypt_password))
                save_option = input("Você deseja salvar essa senha em um arquivo? (sim/nao): ").strip().lower()
            if language == 2:
                print("Encrypted password: {0}".format(encrypt_password))
                save_option = input("Do you want to save the password to a file? (yes/no): ").strip().lower()
            if language == 3:
                print("Contraseña cifrada: {0}".format(encrypt_password))
                save_option = input("Quieres guarda la contraseña en un archivo? (si/no): ").strip().lower()            
            if save_option == 'yes' or save_option == 'sim' or save_option == 'si':
                save_password_to_file(password_confered) # Fix bug: save_password_to_file(password)
                if language == 1:
                    print("Sua senha foi salva em um arquivo.")
                if language == 2:
                    print("Password has been saved to file.")
                if language == 3:
                    print("La contraseña ha sido guardada en un archivo.")                   
        case 4:
            entrada_valida = True
            print()
            if language == 1:
                password = input("Por favor, digite a senha criptografada: ")
                key = input("Por favor, digite a chave de criptografia dentro de b' ':" )
            if language == 2:
                password = input("Please, enter the encrypted password: ")
                key = input("Please, enter the encryption key inside b' ': ")
            if language == 3:
                password = input("Porfavor, introduzca la contraseña cifrada: ")
                key = input("Porfavor, introduzca la llave de cifrado dentro de b' ': ")            
            decrypt_password = decrypt(password, key)
            print()
            if language == 1:
                print("Senha: {0}".format(decrypt_password))
            if language == 2:
                print("Password: {0}".format(decrypt_password))
            if language == 3:
                print("Contraseña: {0}".format(decrypt_password))               
        case 5:
            entrada_valida = True
            if language == 1:
                password = input("Por favor, digite a senha criptografada: ")
                key = input("Por favor, digite a chave de criptografia dentro de b': '" )
            if language == 2:
                password = input("Please, enter the encrypted password: ")
                key = input("Please, enter the encryption key inside b' ': ")
            if language == 3:
                password = input("Porfavor, introduzca la contraseña cifrada: ")
                key = input("Porfavor, introduzca la llave de cifrado dentro de b' ': ")  
            encrypt_password = encrypt(password, key)
            if language == 1:
                print("Senha criptografada: {0}".format(encrypt_password))
                save_option = input("Você deseja salvar essa senha em um arquivo? (sim/nao): ").strip().lower()
            if language == 2:
                print("Encrypted password: {0}".format(encrypt_password))
                save_option = input("Do you want to save the password to a file? (yes/no): ").strip().lower()
            if language == 3:
                print("Contraseña encriptada: {0}".format(encrypt_password))
                save_option = input("Quieres guarda la contraseña en un archivo? (si/no): ").strip().lower()
            if save_option == 'yes' or save_option == 'sim' or save_option == 'si':            
                save_password_to_file(password_confered)
                if language == 1:
                    print("Sua senha foi salva em um arquivo.")
                if language == 2:
                    print("Password has been saved to file.")
                if language == 3:
                    print("La contraseña ha sido guardada en un archivo.")
        case _:
            if language == 1:
                print("Português: Entrada inválida. Por favor, digite 1, 2, 3, 4 ou 5 para uma entrada válida.")
                user_input = int(input("Escolha uma opção (1/2/3/4/5): "))
            if language == 2:
                print("English: Invalid input. Please, enter 1, 2, 3, 4 or 5 for a valid input.")
                user_input = int(input("Choose an option (1/2/3/4/5): "))
            if language == 3:
                print("Español: Entrada invalida. Porfavor, introduce 1, 2, 3, 4 or 5 para una entrada válida.")
                user_input = int(input("Escoge una opción (1/2/3/4/5): "))               