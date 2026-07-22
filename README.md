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

## Nomenclatura e Tipagem da Branch

O prefixo muda:
    chore/ (tarefas de manutenção/setup)
    feat/ (novas funcionalidades de negócio).

## Contexto do Desenvolvimento

Este repositório é operado sob um modelo de simulação de fluxo de trabalho assíncrono e colaborativo. O ciclo de vida de desenvolvimento de software — abrangendo o provisionamento de tarefas, revisão de código (Code Review) e integração de Pull Requests — é executado simulando ambientes e permissões distintas. O objetivo é garantir o rigor e a aplicação estrita de políticas de controle de versão, segregação de funções e rastreabilidade de requisitos.