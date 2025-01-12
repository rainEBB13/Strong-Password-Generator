import os
import secrets
import string

#--------------------------------------------------------------------------#
#Função feita para criar uma senha:
def creating_a_password():
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
def confering_strong_password(password):
    #CARACTERÍSTICAS DE SENHAS FORTES:
    # - 12 a 16 caracteres.
    # - Letras maiúsculas (ABCD).
    # - Letras minúsculas (abcd).
    # - Números (0-9).
    # - Caracteres especiais (!@#$%^&*, etc.).
    ok = False
    if (any(alphabet for k in password)
            and any(numbers for k in password)
            and any(simbols for k in password)):
        ok = True
    
    if ok:
        return password

    password = creating_a_password(alphabet, numbers, simbols)
#--------------------------------------------------------------------------#
#Função feita para conferir a força de uma senha:
def confering_the_strength(password):
    # Senhas divididas em 4 níveis: Fraca, Moderada, Semi-Forte e Forte.
        # Nível 1) Fraca: Menos de 8 caracteres, apenas letras minúsculas e números.
        # Nível 2) Moderada: 8 a 10 caracteres, combina pelo menos 2 tipos de caracteres.
        # Nível 3) Semi-Forte: 10 a 12 caracteres, inclui letras maiúsculas, minúsculas, números e simbolos.
        # Nível 4) Forte: 12 a 16 caracteres, distribuição aleatória e equilibrada de todos os tipos de caracteres.
    #Equilíbrio do Nível 4: Distribuição de 10% a 40% de cada um dos 4 tipos de caracteres(maiúsculas, minúsculas, números e simbolos)
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
    max_distribution = 0.1 * size_of_password


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
#FUNÇÃO PRINCIPAL:

#Criando uma instância (objeto) para a classe SystemRandom 
random_generator = secrets.SystemRandom()

alphabet = string.ascii_letters
numbers = string.digits
simbols = string.punctuation


password = creating_a_password()

if confering_the_strength(password) == 1:
    print("Nível 1: Fraca\n")
elif confering_the_strength(password) == 2:
    print("Nível 2: Moderada\n")
elif confering_the_strength(password) == 3:
    print("Nível 3: Semi-Forte\n")
elif confering_strong_password(password) == 4:
    print("Nível 4: Forte")

print(password)


#Conferindo se a senha criada é uma senha FORTE.
password_confered = confering_strong_password(password)

print(password_confered)
