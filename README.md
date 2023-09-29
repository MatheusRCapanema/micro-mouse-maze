# Micro Mouse Maze API

Uma API simples para explorar um labirinto virtual com a lógica de um rato micro.

## 🚀 **Começando**

Essas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

### 📋 **Pré-requisitos**

- Python 3.10+
- Pip (Gerenciador de pacotes do Python)

### 🔧 **Instalação**

1. Clone o repositório para sua máquina local:

git clone https://github.com/MatheusRCapanema/micro-mouse-maze.git


2. Navegue até o diretório do projeto:

cd micro-mouse-maze


3. Instale as dependências:

pip install -r requirements.txt


4. Execute a aplicação:

python app.py


A API agora deve estar rodando na porta 5000. 

## 📦 **Endpoints**

- **POST /maze/generate**: Gere um novo labirinto. 
- **GET /maze/start**: Inicie a exploração do labirinto.
- **GET /maze/move/<int:direction>**: Mova-se na direção especificada.
- **GET /maze/remaining_time**: Obtenha o tempo restante para a exploração.

A documentação completa dos endpoints, incluindo os parâmetros esperados e as respostas, pode ser encontrada no Swagger UI acessando:

http://127.0.0.1:5000/

## 📌 **Tecnologias Utilizadas**

- [Flask](https://flask.palletsprojects.com/)
- [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/)
- [Python](https://www.python.org/)

## 🖇️ **Contribuindo**

Sinta-se à vontade para contribuir para este projeto. Qualquer ajuda é bem-vinda!

## ✒️ **Autores**

- *Matheus Rocha Capanema* - [GitHub](https://github.com/MatheusRCapanema)

