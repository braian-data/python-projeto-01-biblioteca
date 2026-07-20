# python-projeto-01-biblioteca
Projeto de estudo para praticar Python, POO, organização de código e boas práticas.

## Criação do Ambiente Virtual
python -m venv .venv
(Convenção de mercado: usar .venv com ponto inicial para mantê-lo oculto em sistemas Unix).

## Ativação da Instância Isolada

Garantir que qualquer pip install que você execute instale os pacotes dentro do diretório local do projeto, e não no ambiente global do seu sistema operacional.

Windows (PowerShell):
    .\.venv\Scripts\Activate.ps1
Windows (CMD):
    .\.venv\Scripts\activate.bat
Linux/macOS (Bash/Zsh):
    source .venv/bin/activate

# Instalação e Troca de Dependências
Instalar pacotes mapeados:
    pip install -r requirements.txt
Registrar novas bibliotecas instaladas no projeto:
    pip freeze > requirements.txt

## Gestão do Projeto

O desenvolvimento deste repositório é gerenciado via **ClickUp**, utilizando metodologias ágeis (Scrum/Kanban) para acompanhamento das tasks e do fluxo de Pull Requests.