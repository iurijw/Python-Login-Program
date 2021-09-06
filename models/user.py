

class User(object):
    idf: int = 1

    def __init__(self, user_name: str, user_pass: str, comment: str) -> None:
        self.__id: int = User.idf
        self.__user_name: str = user_name
        self.__user_pass: str = user_pass
        self.__comment: str = comment
        User.idf += 1

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def user_name(self: object) -> str:
        return self.__user_name

    @property
    def user_pass(self: object) -> str:
        return self.__user_pass

    @property
    def comment(self: object) -> str:
        return self.__comment

