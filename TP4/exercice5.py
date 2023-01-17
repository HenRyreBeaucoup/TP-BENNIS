from datetime import datetime

def date_valide(date_string):
    try:
        date = datetime.strptime(date_string, "%d%m%Y")
        if date > datetime.now():
            raise ValueError("Date invalide : La date est dans le futur")
        return True
    except ValueError as e:
        print(str(e))
        return False
    except:
        print("La date est invalide. Veuillez entrez la date au format 'jjmmaaaa'.")
        return False
date_input = input("Entrer la date dans le format 'jjmmaaaa': ")
if date_valide(date_input):
        print("La date {} est valide.".format(date_input))
else:
    print("La date {} est invalide.".format(date_input))