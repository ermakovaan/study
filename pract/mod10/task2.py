import re

def date_verification(date):
    """
    >>> date_verification('20 января 1806')
    True
    >>> date_verification('1924, July 25')
    True
    >>> date_verification('26/09/1635')
    True
    >>> date_verification('3.1.1506')
    True
    >>> date_verification('25.08-1002')
    False
    >>> date_verification('декабря 19, 1838')
    False
    >>> date_verification('8.20.1973')
    False
    >>> date_verification('Jun 7, -1563')
    False
    >>> date_verification('31 февраля 2023')
    False
    >>> date_verification('31 июня 2015')
    False
    """
    limitation = re.compile("^(?:(?:0?\d|[12]\d|3[01])([\.\/-])(?:(?<!3[01][\.\/-])0?2|?<!31"
                       "[\.\/-])0?[469]|0?[^2469]|12)\1\d{4}|\d{4}([\.\/-])(?:0?2(?![\.\/-]"
                       "3[01])|0?[469](?!31[\.\/-])|0?[^2469]|12)\2(?:0?\d|[12]\d|3[01])|"
                       "(?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )"
                       "(?:апреля|июня|сентября|ноября)|мая|июля|августа|октября|декабря) "
                       "\d{4}|(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)"
                       "?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|"
                       "Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, (?:Jan(?:uary)?|"
                       "Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|"
                       "Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) "
                       "(?:[0-2]\d|3[01]))$")

    return bool(limitation.match(date))


if __name__ == "main":
    import doctest

    doctest.testmod(verbose=True)
