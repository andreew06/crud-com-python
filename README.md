# 🚀 API CRUD com FastAPI e SQLAlchemy

Um projeto prático de backend construído do zero para consolidar conceitos fundamentais de desenvolvimento em Python, focado na criação de uma API RESTful completa.

## 📌 Sobre o Projeto
Este projeto implementa as quatro operações básicas de um sistema (Create, Read, Update, Delete) gerenciando um cadastro de usuários. O foco principal foi garantir uma arquitetura limpa, separação de responsabilidades (Rotas, Modelos, Schemas de Validação e Conexão com Banco) e documentação automatizada.

## 🛠️ Tecnologias Utilizadas
* **Python 3.11**
* **FastAPI:** Framework web moderno e de alta performance.
* **SQLAlchemy:** ORM (Object-Relational Mapping) para comunicação com o banco.
* **Pydantic:** Validação rigorosa de dados de entrada e saída.
* **SQLite:** Banco de dados relacional leve para desenvolvimento local.
* **Uvicorn:** Servidor ASGI para rodar a aplicação.

## ⚙️ Como Executar Localmente

1. Clone este repositório:
`git clone https://github.com/andreew06/crud-com-python.git`

2. Acesse a pasta do projeto:
`cd crud-com-python`

3. Crie e ative um ambiente virtual (exemplo com Anaconda):
`conda create --name crud-env python=3.11`
`conda activate crud-env`

4. Instale as dependências:
`pip install -r requirements.txt`

5. Inicie o servidor:
`uvicorn main:app --reload`

6. Acesse a documentação interativa (Swagger) no navegador:
`http://127.0.0.1:8000/docs`

## 🔗 Endpoints (Rotas)
* `POST /usuarios/` - Cria um novo usuário.
* `GET /usuarios/` - Lista todos os usuários cadastrados.
* `PUT /usuarios/{id}` - Atualiza os dados de um usuário específico.
* `DELETE /usuarios/{id}` - Exclui um usuário do banco de dados.

---
**Desenvolvido por:**
[andreew06](https://github.com/andreew06)
*Data Analyst | Dashboards com Power BI & Automação com N8N | Transformando dados em decisões inteligentes*