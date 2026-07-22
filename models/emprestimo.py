from models.usuario import Usuario
from models.livro import Livro

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro, data_emprestimo: str) -> None:
        """Inicializa a transação com validação estrita de regras de negócio."""
        if not usuario.permissao_emprestimo():
            raise PermissionError(f"Usuário '{usuario._nome}' atingiu o limite ou não possui permissão para empréstimos.")
        
        if not livro.emprestar():
            raise ValueError(f"O livro '{livro._titulo}' encontra-se indisponível no acervo no momento.")

        self._usuario = usuario
        self._livro = livro
        self._data_emprestimo = data_emprestimo
        self._ativo: bool = True

    def __str__(self) -> str:
        status = "Ativo" if self._ativo else "Devolvido"
        return f"Empréstimo: [{self._livro._titulo}] para [{self._usuario._nome}] | Data: {self._data_emprestimo} | Status: {status}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(usuario={self._usuario.__repr__()}, livro={self._livro.__repr__()})"

    def registrar_devolucao(self) -> None:
        """Inverte o estado lógico da transação e do livro vinculado."""
        if not self._ativo:
            raise ValueError("Este empréstimo já foi encerrado anteriormente.")
        
        self._livro.devolver()
        self._ativo = False