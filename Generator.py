import os
import secrets
import string

#--------------------------------------------------------------------------#
#Função feita para criar uma senha:
def creating_a_password(alphabet, numbers, simbols):
    password = ""
    for i in range(16):
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
def confering_strong_password(password, alphabet, numbers, simbols):
    ok = False
    if (any(alphabet for k in password)
            and any(numbers for k in password)
            and any(simbols for k in password)):
        ok = True
    
    if ok:
        return password

    password = creating_a_password(alphabet, numbers, simbols)
#--------------------------------------------------------------------------#
#FUNÇÃO PRINCIPAL:

#Criando uma instância (objeto) para a classe SystemRandom 
random_generator = secrets.SystemRandom()

alphabet = string.ascii_letters
numbers = string.digits
simbols = string.punctuation

#CARACTERÍSTICAS DE SENHAS FORTES:
# - Letras maiúsculas (ABCD).
# - Letras minúsculas (abcd).
# - Números (0-9).
# - Caracteres especiais (!@#$%^&*, etc.).
password = creating_a_password(alphabet, numbers, simbols)

#Conferindo se a senha criada é uma senha FORTE.
password_confered = confering_strong_password(password, alphabet, numbers, simbols)



print(password_confered)
