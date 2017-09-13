import json

config = None


def init():
    """
    todo
    :return:
    """

    global config

    with open('config.json') as file:
        class Config():
            """
            todo
            """

            def __init__(self, dict):
                """
                todo
                """
                self.__dict__ = dict

        config = Config(json.load(file))
