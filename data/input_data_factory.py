class InputDataDictionary(dict):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


input_data_instance = InputDataDictionary()


def get_instance():
    return input_data_instance
