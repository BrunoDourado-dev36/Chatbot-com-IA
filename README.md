# 🤖 Chatbot com IA

Aplicação de chatbot desenvolvida em Python utilizando **Streamlit** para a interface e uma **API de IA generativa** para processamento das mensagens.

O projeto permite que o usuário envie mensagens e receba respostas da IA em uma interface de chat, mantendo o histórico da conversa durante a sessão.

## 🚀 Tecnologias utilizadas

* Python
* Streamlit
* API de IA generativa
* OpenAI Python SDK
* Listas e dicionários
* `st.session_state`

## 💻 Funcionalidades

* Interface de chat interativa
* Envio de mensagens pelo usuário
* Geração de respostas utilizando IA
* Histórico das mensagens durante a sessão
* Separação entre mensagens do usuário e da IA
* Integração com API através de Python

## 📂 Estrutura do projeto

```text
Chatbot-com-IA/
│
├── src/
│   ├── codigo.py
│   └── auxiliar.py
│
├── .gitattributes
├── LICENSE
└── README.md
```

### `src/codigo.py`

Arquivo principal da aplicação. Responsável por:

* Criar a interface do chatbot;
* Receber mensagens do usuário;
* Armazenar o histórico da conversa;
* Enviar as mensagens para a API;
* Receber e exibir as respostas da IA.

### `src/auxiliar.py`

Arquivo utilizado durante o desenvolvimento para praticar a criação e manipulação da estrutura de mensagens utilizando listas e dicionários.

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/BrunoDourado-dev36/Chatbot-com-IA.git
```

### 2. Entre na pasta do projeto

```bash
cd Chatbot-com-IA
```

### 3. Instale as dependências

```bash
pip install streamlit openai
```

### 4. Configure sua chave da API

A chave da API não deve ser colocada diretamente no código-fonte.

Utilize uma variável de ambiente ou arquivo `.env` e mantenha esse arquivo fora do GitHub.

### 5. Execute a aplicação

```bash
streamlit run src/codigo.py
```

Após executar o comando, o Streamlit abrirá a aplicação no navegador.

## 🧠 O que aprendi neste projeto

Este projeto foi desenvolvido como prática de integração entre Python e inteligência artificial.

Durante o desenvolvimento, foram trabalhados conceitos como:

* Consumo de APIs;
* Integração de aplicações Python com serviços externos;
* Listas e dicionários;
* Estruturas de repetição;
* Condicionais;
* Gerenciamento de estado com `st.session_state`;
* Desenvolvimento de interfaces com Streamlit;
* Manipulação e armazenamento do histórico de mensagens.

## 🔒 Segurança

Nunca compartilhe chaves de API diretamente no código ou em repositórios públicos.

Para executar o projeto, configure sua própria chave de API através de uma variável de ambiente ou outro método seguro de gerenciamento de credenciais.

## 👨‍💻 Autor

**Bruno Dourado**

GitHub: [BrunoDourado-dev36](https://github.com/BrunoDourado-dev36)
