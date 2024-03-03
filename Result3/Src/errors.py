
class error_proxy:
    __error_text = ""

    def __init__(self, exception: Exception = None):
        if exception is not None:
            self.set_error(exception)

    @property
    def error(self):
        return self.__error_text

    @error.setter
    def error(self, value: str):
        if value == "":
            raise Exception("Некорректно переданы параметры!")

        self.__error_text = value

    @classmethod
    def set_error(self, exception: Exception):
        if exception is None:
            self.__error_text = ""
            return

        self.__error_text = "Ошибка! " + str(exception)

    @property
    def is_empty(self) -> bool:

        if len(self.__error_text) != 0:
            return False
        else:
            return True


# Набор классов для генерации собственных исключений

#
# Абстрактный класс для наследования
#
class exception_proxy(Exception):
    __error: error_proxy = error_proxy()

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.__error.set_error(self)

    @property
    def error(self):
        return self.__error

    @staticmethod
    def is_valide(value, type_, len_=None):

        # Проверка типа
        if not isinstance(value, type_):
            raise argument_exception("Некорректный тип")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) >= len_:
            raise argument_exception("Некорректная длина аргумента")

        return True
class argument_exception(exception_proxy):
    pass

class operation_exception(argument_exception):
    pass