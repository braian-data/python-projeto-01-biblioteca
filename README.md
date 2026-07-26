# Sistema de Gestão de Biblioteca (Pure Python CLI)

> **Nota do Autor:** Este projeto foi construído do zero utilizando **apenas Python nativo** com o objetivo de dominar os fundamentos de Engenharia de Software, Clean Architecture e Orientação a Objetos antes de recorrer a frameworks web (como Django/FastAPI) ou ORMs.

---

## Por que Python Puro?

Em vez de apenas copiar sintaxe de bibliotecas prontas, decidi focar na base:
* **Entender a memória RAM:** Garantir que um objeto só exista se for 100% válido (Atomicidade).
* **Desacoplamento de verdade:** Separar quem valida, quem guarda regras de negócio e quem lida com o usuário.
* **Resiliência:** Tratar erros na borda do sistema (*Fail-Fast*) sem deixar a aplicação crashar.

---

## Arquitetura e Estrutura

├── models/             # Entidades (Livro, Usuário, Empréstimo)
├── services/           # Regras de negócio e acervo em memória (O(1))
├── utils/              # Validações sintáticas puras (Regex, Datetime, ISBN)
└── main.py             # Interface no terminal e captura de erros

### Padrões Aplicados
* **Validação Atômica:** Objetos só nascem se os dados passarem na auditoria.
* **Polimorfismo (ABC):** Uso de classe abstrata `Usuario` com regras específicas para `Aluno`, `Professor` e `Bibliotecario`.
* **Transação Defensiva:** A classe `Emprestimo` valida permissões e disponibilidade no ato da criação.

---

## Como Executar

```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
python main.py
