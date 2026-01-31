import re
class InvalidPasswordError(Exception):
    pass
class InvalidEmailError(Exception):
    pass
def validate_email(email):
    if len(email)<8:
        raise InvalidEmailError("СЛИШКОМ КОРОТКАЯ ПОЧТА")
    if not re.search(r"@mail[.]",email):
        raise InvalidEmailError("GDE INDEX?")
    if re.search(r"[#$%!&*]",email):
        raise InvalidEmailError("SPECSIMVOLI NELZYA")
    else:
        print("КРАСАВЧИК ПОЧТА ВВЕДЕНА")
        with open ("mail.txt","w") as file:
            file.write(email)
email=input("ВВЕДИ ПОЧТУ")
try:
    validate_email(email)
except InvalidEmailError as g:
    print(g)


def validatpassword(password):
    if len (password)< 8:
        raise InvalidPasswordError("minimum 8 simvolov idiot")
    if not re.search(r"[A-Z]",password):
        raise InvalidPasswordError("ZAGLAVNYE BUKVY")
    if not re.search(r"[#$%!@]", password):
        raise InvalidPasswordError("SPECSIMVOLI ZABIL")
    if not re.search(r"\d",password):
        raise InvalidPasswordError("CIFRI")
    else:
        print("KRASAVCHIK PAROL VVEDEN")
        with open("parol.txt","w") as file:
            file.write(password)
password=input("VVEDI: ")
try:
    validatpassword(password)
except InvalidPasswordError as e:
    print(e)