from abc import ABC


class Pizza(ABC):
    pedacos = 8

    def mudar_tamanho(self, pedacos):
        self.pedacos = pedacos

    @staticmethod
    def ingredientes():
        return 'Ingredientes'


class Mussarela(Pizza):

    @staticmethod
    def ingredientes():
        return ['queijo murrarela', 'molho de tomate', 'oregano']
