
class Usuario:
    def __init__(
        self,
        nome: str,
        data_nascimento: str,
        data_cadastro: str,
        email: str,
        telefone: str,
    ) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._data_cadastro = data_cadastro
        self._email = email
        self._telefone = telefone
        self._lista: list = []

    def __eq__(self, other: object) -> bool:
        """Define a igualdade baseada na unicidade do e-mail."""
        if not isinstance(other, Usuario):
            return NotImplemented
        return self._email == other._email

    def __str__(self) -> str:
        """Representação amigável para o usuário final."""
        return (
            f"Usuário: {self._nome} | E-mail: {self._email} | "
            f"Cadastro: {self._data_cadastro} | Tel: {self._telefone}"
        )

    def __repr__(self) -> str:
        """Representação formal para log e debug."""
        return f"{self.__class__.__name__}(nome='{self._nome}', email='{self._email}')"

    def permissao_emprestimo(self) -> bool:
        """
        Simulação de abstração.
        Força as subclasses a implementarem sua própria regra de negócio.
        """
        raise NotImplementedError(
            f"A subclasse {self.__class__.__name__} deve implementar o método permissao_emprestimo()."
        )


class Aluno(Usuario):
    def __init__(
        self,
        nome: str,
        data_nascimento: str,
        data_cadastro: str,
        email: str,
        telefone: str,
        matricula: str,
        limite_emprestimos: int = 3,
    ) -> None:
        super().__init__(nome, data_nascimento, data_cadastro, email, telefone)
        self._matricula = matricula
        self._limite_emprestimos = limite_emprestimos

    def permissao_emprestimo(self) -> bool:
        """Aluno só pode pegar livro se não tiver atingido o limite."""
        return self._limite_emprestimos > 0

    def __str__(self) -> str:
        return f"{super().__str__()} | Matrícula: {self._matricula} | Limite de Empréstimos: {self._limite_emprestimos}"


class Professor(Usuario):
    def __init__(
        self,
        nome: str,
        data_nascimento: str,
        data_cadastro: str,
        email: str,
        telefone: str,
        cod_docente: str,
    ) -> None:
        super().__init__(nome, data_nascimento, data_cadastro, email, telefone)
        self._cod_docente = cod_docente 

    def permissao_emprestimo(self) -> bool:
        """Professor possui permissão irrestrita na lógica atual."""
        return True

    def __str__(self) -> str:
        return f"{super().__str__()} | Código Docente: {self._cod_docente}"


class Bibliotecario(Usuario):
    def __init__(
        self,
        nome: str,
        data_nascimento: str,
        data_cadastro: str,
        email: str,
        telefone: str,
        crb: str, #sigla para Conselho Regional de Biblioteconomia
    ) -> None:
        super().__init__(nome, data_nascimento, data_cadastro, email, telefone)
        self._crb = crb

    def permissao_emprestimo(self) -> bool:
        """Bibliotecários gerenciam o sistema, não contraem empréstimos nesta regra de negócio."""
        return False

    def __str__(self) -> str:
        return f"{super().__str__()} | CRB: {self._crb}"
