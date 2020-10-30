from abc import abstractmethod, ABC


class ManipulaArquivo(ABC):
    # Uma classe abstrata que implementa métodos concretos.
    def ler_arquivo(self):
        self.abrir_arquivo()
        conteudo = self.ler_conteudo()
        self.fechar_arquivo()

        return conteudo

    @abstractmethod
    def abrir_arquivo(self):
        ...

    @abstractmethod
    def fechar_arquivo(self):
        ...

    @abstractmethod
    def ler_conteudo(self):
        ...




    # Dando a diretriz do que precisa ser feito, mas não como você realmente fará isso. Cada objeto tem uma forma
    # diferente de implementar tal comportamento.

    # Uma configuração pronta, padrão do que você vai usar, mas como fazer isso, não está sendo dito.
