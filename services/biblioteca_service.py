from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo

class BibliotecaService:
    def __init__(self) -> None:
        self._acervo: dict[str, Livro] = {} 
        self._usuarios_emails: set[str] = set()
        self._usuarios: list[Usuario] = []
        self._emprestimos: list[Emprestimo] = []

    def adicionar_livro(self, livro: Livro) -> None:
        if livro._isbn in self._acervo:
            raise ValueError(f"Violação de integridade: ISBN {livro._isbn} já cadastrado.")
        self._acervo[livro._isbn] = livro

    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario._email in self._usuarios_emails:
            raise ValueError(f"Violação de integridade: E-mail {usuario._email} já cadastrado.")
        self._usuarios_emails.add(usuario._email)
        self._usuarios.append(usuario)

    def processar_emprestimo(self, usuario: Usuario, isbn: str, data: str) -> Emprestimo:
        """Encapsula a transação em bloco try/except para capturar falha de chave em tempo de execução."""
        try:
            livro_alvo = self._acervo[isbn]
            novo_emprestimo = Emprestimo(usuario, livro_alvo, data)
            self._emprestimos.append(novo_emprestimo)
            return novo_emprestimo
        except KeyError:
            raise ValueError(f"Falha na transação: ISBN {isbn} não consta no banco de dados.")

    def buscar_livros_por_autor(self, autor: str) -> list[Livro]:
        """Aplica filter + lambda para varredura condicional no acervo."""
        return list(filter(lambda livro: livro._autor.lower() == autor.lower(), self._acervo.values()))

    def listar_todos_os_titulos(self) -> list[str]:
        """Aplica map + lambda para mutação extraindo apenas atributos específicos."""
        return list(map(lambda livro: livro._titulo, self._acervo.values()))

    def listar_acervo_ordenado_por_ano(self) -> list[Livro]:
        """Aplica sorted + lambda para roteamento de critério de ordenação (ano de publicação)."""
        return sorted(self._acervo.values(), key=lambda livro: livro._ano_publicacao)

    def listar_livros_indisponiveis(self) -> list[Livro]:
        """Aplica list comprehension para filtro booleano de disponibilidade."""
        return [livro for livro in self._acervo.values() if not livro._disponivel]
    
    def buscar_usuario_por_email(self, email: str) -> Usuario:
        """Busca linear (O(N)) na lista de usuários cadastrados."""
        for usuario in self._usuarios:
            if usuario._email == email:
                return usuario
        raise KeyError(f"Usuário com e-mail '{email}' não encontrado.")