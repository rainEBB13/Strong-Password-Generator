import os
import secrets
import string
from cryptography.fernet import Fernet

#--------------------------------------------------------------------------#
#Função feita para criar uma senha Forte:
def creating_a_password(size_of_strength_password):
    password = ""
 
    for i in range(size_of_strength_password):
        #Alphabet = 0, Numbers = 1, Simbols = 2.
        random_temporary_number = random_generator.randrange(3)

        if random_temporary_number == 0:
            password += random_generator.choice(alphabet)
        elif random_temporary_number == 1:
            password += random_generator.choice(numbers)
        elif random_temporary_number == 2:
            password += random_generator.choice(simbols)
        
    return password
#--------------------------------------------------------------------------#
#Função feita para conferir se a senha é forte segundo as características de senhas fortes:
def confering_strong_password(password, size_of_strength_password):
    #CARACTERÍSTICAS DE SENHAS FORTES:
    # - 12 a 16 caracteres.
    # - Letras maiúsculas (ABCD).
    # - Letras minúsculas (abcd).
    # - Números (0-9).
    # - Caracteres especiais (!@#$%^&*, etc.).
    # - Equilíbrio na distribuição de tipos de caracteres.
    while True:
        ok1 = False
        if (any(alphabet for k in password)
                and any(numbers for k in password)
                and any(simbols for k in password)):
            ok1 = True
    
        #Conferindo o equilíbrio da distribuição de tipos de caracteres (10% a 40% de cada um dos 4 tipos)
        #4 tipos: maiúsculas, minúsculas, números e simbolos
        size_of_password = len(password)
        character = {
            "lower_letter": 0, 
            "upper_letter": 0,
            "numbers": 0,
            "simbols":0
        }
        #Limites para ser uma senha forte:
        min_distribution = 0.1 * size_of_password
        max_distribution = 0.4 * size_of_password

        for i in password:
            if i in alphabet and i.islower():
                character["lower_letter"] += 1
            elif i in alphabet and i.isupper():
                character["upper_letter"] += 1
            elif i in numbers:
                character["numbers"] += 1
            elif i in simbols:
                character["simbols"] += 1
    
        ok2 = False
        if ((character["lower_letter"] >= min_distribution
                    and character["lower_letter"] <= max_distribution)
                        and (character["upper_letter"] >= min_distribution
                            and character["upper_letter"] <= max_distribution)
                        and (character["numbers"] >= min_distribution
                            and character["numbers"] <= max_distribution)
                        and (character["simbols"] >= min_distribution
                            and character["simbols"] <= max_distribution)):
                    ok2 = True
    
        if ok1 and ok2:
            break

        password = creating_a_password(size_of_strength_password)

    return password
#--------------------------------------------------------------------------#
#Função feita para conferir a força de uma senha:
def confering_the_strength(password):
    # Senhas divididas em 4 níveis: Fraca, Moderada, Semi-Forte e Forte.
        # Nível 1) Fraca: Menos de 8 caracteres, apenas letras minúsculas e números.
        # Nível 2) Moderada: 8 a 10 caracteres, combina pelo menos 2 tipos de caracteres.
        # Nível 3) Semi-Forte: 10 a 12 caracteres, inclui letras maiúsculas, minúsculas, números e simbolos.
        # Nível 4) Forte: Mais de 16 caracteres, distribuição aleatória e equilibrada de todos os tipos de caracteres.
    # Equilíbrio do Nível 4: Distribuição de 10% a 40% de cada um dos 4 tipos de caracteres(maiúsculas, minúsculas, números e simbolos)
    # Para veredito final será considerado um compilado das características acima mencionadas.

    size_of_password = len(password)
    character = {
        "lower_letter": 0, 
        "upper_letter": 0,
        "numbers": 0,
        "simbols":0
    }
    #Limites para ser uma senha forte:
    min_distribution = 0.1 * size_of_password
    max_distribution = 0.4 * size_of_password


    for i in password:
        if i in alphabet and i.islower():
            character["lower_letter"] += 1
        elif i in alphabet and i.isupper():
            character["upper_letter"] += 1
        elif i in numbers:
            character["numbers"] += 1
        elif i in simbols:
            character["simbols"] += 1
    
    if size_of_password < 8:
        #Nível 1.
        return 1
    elif size_of_password >= 8 and size_of_password < 10:
        if (character["lower_letter"] == size_of_password
                or character["upper_letter"] == size_of_password
                or character["numbers"] == size_of_password
                or character["simbols"] == size_of_password):
            #Nível 1 (Feito somente com 1 tipo de caracter, apesar de seu tamanho).
            return 1
        else:
            #Nível 2 (Feito com 8 a 10 caracteres, independentemente da variedade de tipos de caracteres).
            return 2
    elif size_of_password >= 10 and size_of_password < 12:
        if (character["lower_letter"] == size_of_password
                or character["upper_letter"] == size_of_password
                or character["numbers"] == size_of_password
                or character["simbols"] == size_of_password):
            #Nível 1 (Feito somente com 1 tipo de caracter, apesar de seu tamanho).
            return 1
        elif (character["lower_letter"] > 0
                and character["upper_letter"] > 0
                and character["numbers"] > 0
                and character["simbols"] > 0):
            #Nível 3 (Todas as características do nível 3: tamanho e tipos de caracteres).
            return 3
        else:
            #Nível 2 (Não tem todos os tipos de caracteres para ser nível 3 e tem tamanho aceitável para nível 2)
            return 2
    elif size_of_password >= 12:
        if (character["lower_letter"] == size_of_password
                or character["upper_letter"] == size_of_password
                or character["numbers"] == size_of_password
                or character["simbols"] == size_of_password):
            #Nível 1 (Feito somente com 1 tipo de caracter, apesar de seu tamanho).
            return 1
        elif (character["lower_letter"] > 0
                and character["upper_letter"] > 0
                and character["numbers"] > 0
                and character["simbols"] > 0):
            #Conferindo se há equilíbrio na distribuição dos tipos de caracteres.
            if ((character["lower_letter"] >= min_distribution
                 and character["lower_letter"] <= max_distribution)
                    and (character["upper_letter"] >= min_distribution
                        and character["upper_letter"] <= max_distribution)
                    and (character["numbers"] >= min_distribution
                        and character["numbers"] <= max_distribution)
                    and (character["simbols"] >= min_distribution
                        and character["simbols"] <= max_distribution)):
                #Nível 4.
                return 4
            else:
                #Nível 3. Não há equilíbrio, mas devido ao tamanho e tipos de caracteres se enquadra em nível 3.
                return 3
        else:
            #Nível 2, tem um tamanho bom, porém não tem todos os tipos de caracteres.
            return 2
#--------------------------------------------------------------------------#
#Função feita para gerar uma chave de criptografia:
def create_key():
    key = Fernet.generate_key()
    return key
#--------------------------------------------------------------------------#
#Função feita para criptografar uma senha
def encrypt(password, key):
    #Convertendo os 2 argumentos em Bytes para a criptografia
    password = password.encode()

    encrypt_password = Fernet(key).encrypt(password)

    #Convertendo novamente para uma string
    encrypt_password = encrypt_password.decode()
    return encrypt_password
#--------------------------------------------------------------------------#
#Função feita para descriptografar uma senha
def decrypt(password, key):
    #Convertendo os 2 argumentos em Bytes para a descriptografia
    password = password.encode()

    decrypt_password = Fernet(key).decrypt(password)

    #Convertendo novamente para uma string
    decrypt_password = decrypt_password.decode()
    return decrypt_password
#--------------------------------------------------------------------------#
#FUNÇÃO PRINCIPAL:

#MENU:
print("#----------------------------------------------------#")
print("Português:")
print('# MENU DO PROJETO "STRONG-PASSWORD-GENERATOR":"')
print("    1. Conferir a força de uma senha qualquer.")
print("    2. Gerar uma senha forte aleatória.")
print("    3. Gerar uma senha forte criptografada.")
print("    4. Descriptografar uma senha.")
print("    5. Criptografar uma senha com uma chave específica.")
print()
print()
print("English:")
print('# MENU FOR THE PROJECT "STRONG-PASSWORD-GENERATOR":')
print("    1. Check the strength of any password.")
print("    2. Generate a random strong password.")
print("    3. Generate an encrypt strong password.")
print("    4. Decrypt a password.")
print("    5. Encryp a password with a especific key.")
print("#----------------------------------------------------#")
print()

#Criando uma instância (objeto) para a classe SystemRandom 
random_generator = secrets.SystemRandom()

alphabet = string.ascii_letters
numbers = string.digits
simbols = string.punctuation

user_input = int(input("Qual entrada você deseja(1/2/3/4/5) ? [What option you wish(1/2/3/4/5) ?] "))

entrada_valida = False
count = 0
while (not entrada_valida):
    match user_input:
        case 1:
            entrada_valida = True
            senha_do_usuario = input("Digite a senha(Digit the password): ")
            password_strength = confering_the_strength(senha_do_usuario)
            if password_strength == 1:
                print("Nível 1: Fraca(Weak)\n")
            elif password_strength == 2:
                print("Nível 2: Moderada(Moderate)\n")
            elif password_strength == 3:
                print("Nível 3: Semi-Forte(Semi-Strength)\n")
            elif password_strength == 4:
                print("Nível 4: Forte(Strength)")
        case 2:
            entrada_valida = True
            #Tamanho de entrada desejado pelo usuário:
            print()
            print("Português: Qual tamanho você deseja (Obrigatório 16+ caracteres)? ")
            print("English: What size you wish (Obrigatory 16 characters or more)? ")
            size_of_strength_password = int(input("R = "))
            while True:
                if size_of_strength_password >= 16:
                    break
                else:
                    print("Português: Entrada inválida. A senha deve conter 16 ou mais caracteres!")
                    print("English: Invalid input. The password must contain 16 characters or more")
                    size_of_strength_password = int(input("Digite um tamanho válido(Digit a valid size): "))
            # Criando a senha:
            password = creating_a_password(size_of_strength_password)
            # Conferindo se é forte. Se não for, faz uma senha forte:
            password_confered = confering_strong_password(password, size_of_strength_password)
            print("A senha forte criada é(The strength password created is): {0}".format(password_confered))
        case 3:
            entrada_valida = True
            #Tamanho de entrada desejado pelo usuário:
            print()
            print("Português: Qual tamanho você deseja (Obrigatório 16+ caracteres)? ")
            print("English: What size you wish (Obrigatory 16 characters or more)? ")
            size_of_strength_password = int(input("R = "))
            while True:
                if size_of_strength_password >= 16:
                    break
                else:
                    print("Português: Entrada inválida. A senha deve conter 16 ou mais caracteres!")
                    print("English: Invalid input. The password must contain 16 characters or more")
                    size_of_strength_password = int(input("Digite um tamanho válido(Digit a valid size): "))
            # Criando a senha:
            password = creating_a_password(size_of_strength_password)
            #Criando uma chave da criptografia:
            key = create_key()
            print()
            print("Português: Atenção, a chave de criptografia usada é de extrema importância. Guarde-a com todo o cuidado possível!")
            print("English: Attention, the encryption key used is extremely important. Keep it with the utmost care!\n")
            print("Key: {0}".format(key))
            #Criptografando com chave criada:
            encrypt_password = encrypt(password, key)
            print("Senha criptografada (encrypt password): {}".format(encrypt_password))
        case 4:
            entrada_valida = True
            print()
            password = input("Por favor, digite a senha criptografada(Please, digit the encrypt password): ")
            key = input("Por favor, digite a chave de criptografia dentro de b' ' (Please, digit the encrypt key inside of b' '): ")
            decrypt_password = decrypt(password, key)
            print()
            print("Password: {0}".format(decrypt_password))
        case 5:
            entrada_valida = True
            password = input("Por favor, digite a senha (Please, digit the password): ")
            key = input("Por favor, digite a chave de criptografia dentro de b' ' (Please, digit the encrypt key inside of b' '): ")
            encrypt_password = encrypt(password, key)
            print("Encrypt password: {0}".format(encrypt_password))
        case _:
            print("Português: Entrada inválida. Por favor, digite 1, 2, 3 ou 4 para a entrada ser válida.")
            print("English: Invalid input. Please, digit 1, 2, 3 or 4 for a valid input.")
            user_input = int(input("Qual entrada você deseja(1/2/3/4) ? (What option you wish(1/2/3/4) ?) "))

#--------------------------------------------------------------------------#

