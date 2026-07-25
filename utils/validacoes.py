from datetime import datetime
import re


def validar_email(email: str) -> None:
    """Valida o formato sintático de um endereço de e-mail via Regex."""
    padrao_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not isinstance(email, str) or not re.match(padrao_regex, email):
        raise ValueError(
            f"Falha de integridade: A string '{email}' não é um endereço de e-mail válido."
        )


from datetime import datetime

def estruturar_data(data_string: str) -> str:
    """Valida e normaliza uma string de data para o formato DD/MM/AAAA."""
    if not isinstance(data_string, str):
        raise TypeError("A entrada da data deve ser obrigatoriamente uma string.")

    data_sanitizada = data_string.replace("-", "/")

    # 1. Tenta exclusivamente o parse da biblioteca nativa
    try:
        dt = datetime.strptime(data_sanitizada, "%d/%m/%Y")
    except ValueError:
        raise ValueError(
            f"Erro de conversão: A entrada '{data_string}' não é uma data válida. "
            "Utilize obrigatoriamente o formato DD/MM/AAAA."
        )

    # 2. Regra de Negócio (fora do try/except para não sobrescrever a mensagem)
    if dt.year <= 1900:
        raise ValueError("O ano deve ser superior a 1900.")

    return data_sanitizada

def auditar_isbn(isbn: str) -> str:
    """Higieniza e audita a quantidade de dígitos de um ISBN (10 ou 13 dígitos)."""
    if not isinstance(isbn, str):
        raise TypeError("O ISBN deve ser uma string.")

    isbn_limpo = isbn.replace("-", "").replace(" ", "")

    # Suporta ISBN-10 com 'X' final ou ISBN-13 numérico
    if len(isbn_limpo) not in (10, 13) or not (
        isbn_limpo.isdigit() or (len(isbn_limpo) == 10 and isbn_limpo[:-1].isdigit() and isbn_limpo[-1].upper() == 'X')
    ):
        raise ValueError(
            f"Erro de integridade de metadado: O ISBN '{isbn}' fornecido é sintaticamente inválido. "
            "Deve conter exatamente 10 ou 13 dígitos numéricos."
        )

    return isbn_limpo.upper()