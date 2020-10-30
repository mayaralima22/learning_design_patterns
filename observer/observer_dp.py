from abc import ABC

class Observer(ABC):

    def __init__(self, nome):
        self.nome = nome

    def update(self, msg):
        print(f'{self.nome} recebeu: {msg}')


class Email:
    def __init__(self):
        self.observers = []

    def adding_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, msg):
        for observador in self.observers:
            observador.update(msg)

eduardo = Observer("Eduardo")
mayara = Observer("Mayara")
bruno = Observer("Bruno")


email = Email()

email.adding_observer(eduardo)
email.adding_observer(mayara)
email.adding_observer(bruno)

email.notify_observers('Chegou um novo e-mail na sua caixa de entrada')