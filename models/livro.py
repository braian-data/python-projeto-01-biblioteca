class Livro:
    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        ano_publicacao: int,
        editora: str,
        categoria: str,
    ) -> None:
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._ano_publicacao = ano_publicacao
        self._editora = editora
        self._categoria = categoria
        self._disponivel: bool = True

    def __eq__(self, other: object) -> bool:
        """Define a igualdade baseada na unicidade do ISBN."""
        if not isinstance(other, Livro):
            return NotImplemented
        return self._isbn == other._isbn

    def __str__(self) -> str:
        """Representação amigável para exibição."""
        status = "Disponível" if self._disponivel else "Emprestado"
        return f"'{self._titulo}' - {self._autor} (ISBN: {self._isbn}) | Status: {status}"

    def __repr__(self) -> str:
        """Representação formal para logs e debug."""
        return f"{self.__class__.__name__}(titulo='{self._titulo}', isbn='{self._isbn}')"

    def emprestar(self) -> bool:
        """Altera o estado para indisponível se o livro estiver livre."""
        if not self._disponivel:
            return False
        self._disponivel = False
        return True

    def devolver(self) -> None:
        """Restaura a disponibilidade do livro."""
        self._disponivel = True