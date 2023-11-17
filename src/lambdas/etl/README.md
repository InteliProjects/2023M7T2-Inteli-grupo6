# Projeto ETL com FastAPI e PostgreSQL

## Sobre o Projeto
O projeto é uma aplicação desenvolvida em FastAPI para processar dados de voo. Ele implementa um pipeline ETL (Extract, Transform, Load) para extrair dados de arquivos, transformar esses dados em um formato JSON e carregá-los em um banco de dados PostgreSQL.

## Motivação
Dados de voo são cruciais para a análise de desempenho, segurança e eficiência em operações aéreas. Tendo uma solução ETL automatizada, as organizações podem garantir que os dados sejam processados de forma eficiente e armazenados de maneira organizada para análises posteriores. Posteriormente, vamos utilizar esses dados para prever problemas no sistema de bleed dos aviões por meio de um modelo de Machine Learning treinado com dados que passaram pela mesma etapa de ETL.

## Configuração

### Dependências

- FastAPI
- Uvicorn
- Prisma
- python-dotenv

### Variáveis de Ambiente

Antes de executar o projeto, certifique-se de configurar a variável de ambiente `DATABASE_URL` no arquivo `.env`. Essa URL deve apontar para sua instância PostgreSQL.

Exemplo:
```
DATABASE_URL=postgresql://username:password@localhost:5432/mydatabase
```

## Estrutura do Código

### app.py

Este é o ponto de entrada da aplicação. Define a configuração básica do FastAPI, incluindo:

- Middleware para CORS
- Registro do router para upload de arquivos
- Inicialização do servidor Uvicorn

### services/etl.py

Define a classe `ETLService` que orquestra o processo ETL:

- `extract`: Extrai dados de um arquivo.
- `transform`: Transforma os dados extraídos em um formato JSON.
- `load`: Carrega o JSON transformado no banco de dados PostgreSQL.

## Como rodar:

- Faça o build da aplicação:

```shell
$ docker build -t lambda .
```

- Rode a aplicação na porta 8001:

```shell
$ docker run -p 8001:8001 lambda
```