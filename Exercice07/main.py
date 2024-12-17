# Écrivez votre code ici !
def square(number):
    if isinstance(number, int) or isinstance(number, float):
        return number * number
    else:
        print("Le paramètre doit être un nombre !")
        return None


print(square("a"))
print(square(2))
