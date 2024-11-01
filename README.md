# Projeto Flask: Tabela de Notas

Este projeto é uma aplicação web simples construída com Flask que exibe uma tabela de notas de alunos utilizando um DataFrame do Pandas. A aplicação possui duas rotas: a rota principal que apresenta uma página inicial e uma rota que renderiza a tabela de notas em HTML.

## Estrutura do Projeto
├── app.py
└── templates\
    ├── index.html
    └── table.html

- **app.py**: O arquivo principal da aplicação que define as rotas e a lógica da aplicação.
- **templates/**: Pasta que contém os arquivos HTML.
  - **index.html**: Página inicial da aplicação.
  - **table.html**: Página que exibe a tabela de notas.

## Tecnologias Utilizadas

- Python
- Flask
- Pandas

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python e o pip instalados. Além disso, você precisará instalar as dependências do Flask e do Pandas. Você pode fazer isso usando o seguinte comando:


pip install Flask pandas

## Como Executar
1. Clone o repositório para sua máquina local:


`git clone https://github.com/SrMedeirosJr/teste-stalse.git`

2. Execute a aplicação:

`python app.py`

3. Acesse a aplicação no seu navegador em: http://127.0.0.1:5000/

4. Para visualizar a tabela de notas, acesse: http://127.0.0.1:5000/table
