import re

def password_verification(password):
    """
    >>> password_verification("rtG&3FG#Tr^e")
    True
    >>> password_verification("a^A1@*@1Aa")
    True
    >>> password_verification("oF^a1D@y5%e6")
    True
    >>> password_verification("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True
    >>> password_verification("пароль")
    False
    >>> password_verification("password")
    False
    >>> password_verification("qwerty")
    False
    >>> password_verification("lOngPa$$W0Rd")
    False
    """
    limitation = (
        r'^(?=.*[a-z].*[a-z])'
        r'(?=.*\d)'
        r'(?=.*[\^$%@#&*].*[\^$%@#&*].*[\^$%@#&*])'
        r'(?!.*[,.!?])'
        r'[A-Za-z0-9^$%@#&*]{8,}$'
    )

    return bool(re.match(limitation, password))


if __name__ == "main":
    import doctest
    doctest.testmod(verbose=True)