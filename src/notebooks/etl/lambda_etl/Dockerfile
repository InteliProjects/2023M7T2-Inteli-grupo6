# Use uma imagem que contenha Python
FROM python:3.8-slim-buster

# Defina um diretório de trabalho
WORKDIR /app

# Instale as bibliotecas necessárias
RUN pip install pandas numpy scipy

# Copie o código para o contêiner
COPY . .

# Define a função lambda_handler como ponto de entrada
CMD ["lambda_function.lambda_handler"]