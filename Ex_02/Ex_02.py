"""
Ваше курсовое приложение сейчас работает в консольном режиме и взаимодействует с
пользователем посредством команд в консоли. Приложение надо развивать и наиболее часто изменяемой частью приложения
обычно является пользовательский интерфейс (консоль пока что). Модифицируйте код вашего приложения, чтобы представление
информации пользователю (вывод карточек с контактами пользователя, заметками, страничка с информацией
о доступных командах) было легко изменить. Для этого надо описать абстрактный базовый класс для пользовательских
представлений и конкретные реализации, которые наследуют базовый класс и реализуют консольный интерфейс.
В дальнейшем мы будем расширять приложение, добавляя туда Web-интерфейс.
"""

from abc import ABC, abstractmethod


class IOConsole(ABC):

    @abstractmethod
    def show_msg(self):
        ...


class IOWeb(ABC):

    @abstractmethod
    def show_msg(self):
        ...


class Console(IOConsole):

    def __init__(self, message):
        self.message = message

    def show_msg(self):
        return f'your console msg is "{self.message}"'


class Web(IOWeb):

    def __init__(self, message):
        self.message = message

    def show_msg(self):
        return f'your web msg is "{self.message}"'


def main():
    c = Console('this is a console')
    print(c.show_msg())

    w = Web('this is web')
    print(w.show_msg())


if __name__ == '__main__':
    main()
