import re

def validar_email(email: str) -> None:

    padrao_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(padrao_regex, email):
        raise ValueError(f"Falha de integridade: A string '{email}' não é um endereço de e-mail válido.")

def estruturar_data(data_string: str) -> str:

    try:
        # Tenta realizar o particionamento da string e conversão de tipagem para inteiros
        partes = data_string.replace("-", "/").split("/")
        
        if len(partes) != 3:
            raise ValueError
        
        dia, mes, ano = int(partes[0]), int(partes[1]), int(partes[2])
        
        # Validação lógica de calendário básico
        if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 1900):
            raise ValueError
            
        return f"{dia:02d}/{mes:02d}/{ano:04d}"

    except (ValueError, TypeError, AttributeError):
        # Captura qualquer falha de conversão, formatação ou método de string
        raise TypeError(
            f"Erro de conversão: A entrada '{data_string}' não pôde ser interpretada como data. "
            "Utilize obrigatoriamente o formato estruturado DD/MM/AAAA."
        )

def auditar_isbn(isbn: str) -> str:

    try:
        isbn_limpo = isbn.replace("-", "").replace(" ", "")
        
        if not isbn_limpo.isdigit():
            raise ValueError
            
        if len(isbn_limpo) not in (10, 13):
            raise ValueError
            
        return isbn_limpo
        
    except (ValueError, AttributeError):
        raise ValueError(
            f"Erro de integridade de metadado: O ISBN '{isbn}' fornecido é sintaticamente inválido. "
            "Deve conter exatamente 10 ou 13 dígitos numéricos."
        )