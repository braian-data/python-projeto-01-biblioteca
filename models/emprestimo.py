from models.livro import Livro
from models.usuario import Usuario


class Emprestimo:

    def __init__(
        self, usuario: Usuario, livro: Livro, data_emprestimo: str
    ) -> None:
        """Inicializa a transação com validação estrita de regras de negócio."""
        if not usuario.permissao_emprestimo():
            raise PermissionError(
                f"Usuário '{usuario.nome}' atingiu o limite ou não possui"
                " permissão para empréstimos."
            )

        if not livro.emprestar():
            raise ValueError(
                f"O livro '{livro.titulo}' encontra-se indisponível no acervo"
                " no momento."
            )

        self._usuario = usuario
        self._livro = livro
        self._data_emprestimo = data_emprestimo
        self._ativo: bool = True

    # --- GETTERS VIA PROPERTY ---

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @property
    def livro(self) -> Livro:
        return self._livro

    @property
    def ativo(self) -> bool:
        return self._ativo

    # --- MÉTODOS MÁGICOS ---

    def __str__(self) -> str:
        status = "Ativo" if self._ativo else "Devolvido"
        return (
            f"Empréstimo: [{self._livro.titulo}] para [{self._usuario.nome}] |"
            f" Data: {self._data_emprestimo} | Status: {status}"
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(usuario={repr(self._usuario)}, livro={repr(self._livro)})"

    # --- REGRAS DE NEGÓCIO DA TRANSAÇÃO ---

    def registrar_devolucao(self) -> None:
        """Inverte o estado lógico da transação e do livro vinculado."""
        if not self._ativo:
            raise ValueError("Este empréstimo já foi encerrado anteriormente.")

        self._livro.devolver()
        self._ativo = False