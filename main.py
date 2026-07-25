from datetime import date
import sys

from models.livro import Livro
from models.usuario import Aluno, Professor
from services.biblioteca_service import BibliotecaService
from utils.validacoes import auditar_isbn


def exibir_menu() -> str:
    """Renderiza a interface do terminal e devolve a opção escolhida."""
    print("\n" + "=" * 30)
    print("SISTEMA DE BIBLIOTECA (CLI)")
    print("=" * 30)
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário (Aluno)")
    print("3. Processar Empréstimo")
    print("4. Listar Títulos do Acervo (Map)")
    print("5. Listar Livros Indisponíveis (List Comprehension)")
    print("0. Encerrar Sistema")
    print("=" * 30)
    return input("Selecione a rotina: ").strip()


def main() -> None:
    # Inicialização do Service (Banco de Dados em Memória)
    biblioteca = BibliotecaService()

    # Loop de Eventos do Terminal
    while True:
        opcao = exibir_menu()

        if opcao == "0":
            print("Encerrando execução.")
            sys.exit(0)

        elif opcao == "1":
            print("\n--- CADASTRO DE LIVRO ---")
            try:
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                isbn_raw = input("ISBN (10 ou 13 dígitos): ").strip()
                ano = int(input("Ano de Publicação: ").strip())
                editora = input("Editora: ").strip()
                categoria = input("Categoria: ").strip()

                # Apenas a auditoria do ISBN ocorre antes de instanciar o Livro
                isbn_validado = auditar_isbn(isbn_raw)

                novo_livro = Livro(
                    titulo, autor, isbn_validado, ano, editora, categoria
                )
                biblioteca.adicionar_livro(novo_livro)
                print("[SUCCESS] Livro indexado com sucesso.")
            except ValueError as e:
                print(f"[ERRO DE VALIDAÇÃO] {e}")

        elif opcao == "2":
            print("\n--- CADASTRO DE ALUNO ---")
            try:
                nome = input("Nome Completo: ").strip()
                data_nasc = input("Data de Nascimento (DD/MM/AAAA): ").strip()
                email = input("E-mail corporativo/acadêmico: ").strip()
                telefone = input("Telefone: ").strip()
                matricula = input("Matrícula: ").strip()

                # Obtém a data atual em formato de string dinamicamente
                data_cadastro_atual = date.today().strftime("%d/%m/%Y")

                # Passamos as strings puras: o __init__ de Aluno/Usuario
                # executará a validação de e-mail e a estruturação de data!
                novo_aluno = Aluno(
                    nome=nome,
                    data_nascimento=data_nasc,
                    data_cadastro=data_cadastro_atual,
                    email=email,
                    telefone=telefone,
                    matricula=matricula,
                )
                biblioteca.registrar_usuario(novo_aluno)
                print("[SUCCESS] Usuário injetado no sistema.")
            except (ValueError, TypeError) as e:
                print(f"[ERRO DE VALIDAÇÃO] {e}")

        elif opcao == "3":
            print("\n--- PROCESSAMENTO DE EMPRÉSTIMO ---")
            email_usuario = input("E-mail do Usuário cadastrado: ").strip()
            isbn_alvo = input("ISBN do Livro: ").strip()

            try:
                # 1. Busca através da interface do Service (sem violar atributo privado)
                usuario = biblioteca.buscar_usuario_por_email(email_usuario)

                data_hoje = date.today().strftime("%d/%m/%Y")

                # 2. Executa a transação no Service
                emprestimo = biblioteca.processar_emprestimo(
                    usuario, auditar_isbn(isbn_alvo), data_hoje
                )
                print(f"[SUCCESS] {emprestimo}")
            except (KeyError, PermissionError, ValueError) as e:
                print(f"[FALHA NA TRANSAÇÃO] {e}")

        elif opcao == "4":
            print("\n--- ACERVO COMPLETO ---")
            titulos = biblioteca.listar_todos_os_titulos()
            if not titulos:
                print("O acervo está vazio.")
            else:
                for t in titulos:
                    print(f" -> {t}")

        elif opcao == "5":
            print("\n--- RECURSOS INDISPONÍVEIS ---")
            indisponiveis = biblioteca.listar_livros_indisponiveis()
            if not indisponiveis:
                print("Nenhum livro emprestado no momento.")
            else:
                for livro in indisponiveis:
                    print(f" -> {livro}")

        else:
            print(
                "[ERRO] Instrução não reconhecida. Utilize os índices do menu."
            )


if __name__ == "__main__":
    main()