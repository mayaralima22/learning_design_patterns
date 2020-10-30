from template_method.template_method_dp import ManipulaArquivo


class TextFile(ManipulaArquivo):
    def __init__(self, filename):
        self.filename = filename
        self._file = None

    def abrir_arquivo(self):
        self._file = open(self.filename)

    def fechar_arquivo(self):
        self._file.close()

    def ler_conteudo(self):
        return self._file.read()