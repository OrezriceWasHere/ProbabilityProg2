# Jonathan Shaki, Or Shachar 204920367, 209493709

class ArgumentsDictionary(dict):

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, *args, **kw):
        if kw or args or ArgumentsDictionary.instance is None:
            super(ArgumentsDictionary, self).__init__(*args, **kw)
            ArgumentsDictionary.instance = self
