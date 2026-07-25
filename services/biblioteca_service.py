from models.emprestimo import Emprestimo
from models.livro import Livro
from models.usuario import Usuario


class BibliotecaService:

    def __init__(self) -> None:
        self._acervo: dict[str, Livro] = {}
        # Dicionário mapeando email -> Usuario (Otimiza busca para O(1))
        self._usuarios: dict[str, Usuario] = {}
        self._emprestimos: list[Emprestimo] = []

    def adicionar_livro(self, livro: Livro) -> None:
        if livro.isbn in self._acervo:
            raise ValueError(
                f"Violação de integridade: ISBN {livro.isbn} já cadastrado."
            )
        self._acervo[livro.isbn] = livro

    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario.email in self._usuarios:
            raise ValueError(
                f"Violação de integridade: E-mail {usuario.email} já"
                " cadastrado."
            )
        self._usuarios[usuario.email] = usuario

    def buscar_usuario_por_email(self, email: str) -> Usuario:
        """Busca em tempo constante O(1) no repositório de usuários."""
        usuario = self._usuarios.get(email)
        if not usuario:
            raise KeyError(f"Usuário com e-mail '{email}' não encontrado.")
        return usuario

    def processar_emprestimo(
        self, usuario: Usuario, isbn: str, data: str
    ) -> Emprestimo:
        """Encapsula a transação e valida a existência do recurso no acervo."""
        try:
            livro_alvo = self._acervo[isbn]
            novo_emprestimo = Emprestimo(usuario, livro_alvo, data)
            self._emprestimos.append(novo_emprestimo)
            return novo_emprestimo
        except KeyError:
            raise ValueError(
                f"Falha na transação: ISBN {isbn} não consta no banco de dados."
            )

    def buscar_livros_por_autor(self, autor: str) -> list[Livro]:
        """Aplica filter + lambda para varredura condicional no acervo."""
        return list(
            filter(
                lambda livro: livro.autor.lower() == autor.lower(),
                self._acervo.values(),
            )
        )

    def listar_todos_os_titulos(self) -> list[str]:
        """Aplica map + lambda para mutação extraindo apenas os títulos."""
        return list(map(lambda livro: livro.titulo, self._acervo.values()))

    def listar_acervo_ordenado_por_ano(self) -> list[Livro]:
        """Aplica sorted + lambda ordenando por ano de publicação."""
        return sorted(
            self._acervo.values(), key=lambda livro: livro.ano_publicacao
        )

    def listar_livros_indisponiveis(self) -> list[Livro]:
        """Aplica list comprehension para filtro booleano de disponibilidade."""
        return [
            livro for livro in self._acervo.values() if not livro.disponivel
        ]