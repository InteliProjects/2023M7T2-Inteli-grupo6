# Documentação do Modelo de IA

## Sumário

- Introdução
- Estrutura dos Arquivos
- Dependências e Bibliotecas
- Instruções para a API
- Processo de Treinamento do Modelo
- Detalhes Técnicos
- Glossário

## Introdução

Este projeto visa treinar um modelo de aprendizado de máquina para realizar previsões e, em seguida, servir esse modelo via uma API RESTful criada com FastAPI. A API foi projetada para ser fácil de usar, garantindo que os usuários possam obter previsões de forma eficiente.

## Estrutura dos Arquivos

- `./model_api.py`: O código principal da API. É responsável por inicializar a aplicação FastAPI, carregar o modelo treinado e fornecer a rota para previsão.
- `/src/notebooks/models/automl_model_v2.ipynb`: Jupyter Notebook que contém todo o fluxo de trabalho para o treinamento do modelo, desde a importação de dados até a avaliação do modelo.

## Dependências e Bibliotecas

### API (`model_api.py`)

- `pandas`: Para manipulação de dados.
- `pycaret.regression`: Usado para carregar o modelo treinado e fazer previsões.
- `fastapi`: Framework para criar a API.
- `uvicorn`: Servidor ASGI para hospedar a aplicação FastAPI.
- `pydantic`: Para criar modelos de dados.

### Treinamento (`automl_model_v2.ipynb`)

- `pandas` e `numpy`: Para manipulação de dados.
- `google.colab`: Para montar o Google Drive.
- `sklearn`: Biblioteca de aprendizado de máquina para treinamento e avaliação.
- `pycaret`: Biblioteca de automação de aprendizado de máquina.

## Instruções para a API

1. **Inicialização**: Execute o arquivo `main.py` para inicializar a API. Isto hospedará a API localmente em `http://127.0.0.1:8000/`.
2. **Endpoint de Previsão**:
   - Método: POST
   - Endpoint: `/predict`
   - Payload: Um JSON contendo os valores dos atributos conforme definido no `input_model`.
   - Resposta: JSON com o valor da previsão.
3. **Formato de Entrada**: Os valores dos atributos devem ser passados no formato JSON conforme o `input_model`.

## Processo de Treinamento do Modelo

O treinamento do modelo é detalhadamente documentado no notebook `automl_model_v2.ipynb`. O fluxo do processo é o seguinte:

1. **Importação de Bibliotecas**: Todas as bibliotecas necessárias são importadas.
2. **Carregamento de Dados**: Os dados são lidos de um arquivo CSV hospedado no Google Drive.
3. **Preprocessamento**: As colunas altamente correlacionadas são descartadas para evitar multicolinearidade.
4. **Análise de Correlação**: É feita uma análise visual da matriz de correlação.
5. **Separação dos Dados**: Divididos em conjuntos de treinamento e teste.
6. **Treinamento**: Um modelo de Árvore de Decisão é treinado.
7. **Avaliação do Modelo**: Diversas métricas são utilizadas para avaliar o desempenho do modelo.
8. **Uso do PyCaret**: PyCaret é utilizado para selecionar o melhor modelo.
9. **Salvamento do Modelo**: O modelo final é salvo para posterior uso na API.

## Detalhes Técnicos

- **Modelo de Entrada**: O `input_model` é um modelo Pydantic que descreve a estrutura do payload que a API espera. Ele é criado dinamicamente usando `create_model` e contém os nomes dos atributos e seus tipos.
- **Modelo de Saída**: O `output_model` descreve a estrutura da resposta da API, que consiste na previsão gerada pelo modelo.
- **Modelo de Aprendizado de Máquina**: A Árvore de Decisão foi a técnica escolhida neste projeto. Foi utilizado o `DecisionTreeClassifier` do Scikit-learn.

## Implantação na AWS e Modelo Pré-Treinado

### Modelo Pré-Treinado

Para otimizar a eficiência e a experiência do usuário ao interagir com nossa API, optamos por utilizar um modelo já pré-treinado. Isso significa que o modelo de aprendizado de máquina já passou pelo processo completo de treinamento com nosso conjunto de dados e foi ajustado para oferecer as melhores previsões possíveis antes de ser integrado à nossa API. A vantagem deste método é uma resposta mais rápida da API, evitando os tempos de treinamento ao vivo e garantindo que os usuários recebam previsões consistentes baseadas em um modelo estável e testado.

### Implantação na AWS (Amazon Web Services)

Para garantir a disponibilidade, escalabilidade e robustez de nossa solução, decidimos hospedar nossa API no serviço EC2 (Elastic Compute Cloud) da AWS. O EC2 é um serviço web que fornece capacidade computacional escalável na nuvem da Amazon. Ele é projetado para tornar a computação em nuvem na web mais fácil para os desenvolvedores.

**Etapas de implantação**:

1. **Instância EC2**: Foi criada uma instância EC2 na AWS, configurada de acordo com as necessidades de recursos do nosso projeto.
2. **Configuração de Segurança**: Grupos de segurança foram configurados para permitir o tráfego HTTP/HTTPS, garantindo que a API possa ser acessada via web, mas também mantendo padrões rigorosos de segurança.
3. **Transferência do Modelo e Código**: Os arquivos do projeto, incluindo o modelo pré-treinado, foram transferidos para a instância EC2 usando SCP (Secure Copy Protocol).
4. **Inicialização da API**: Uma vez na instância EC2, a API foi inicializada, tornando-a acessível via endereço IP público associado à instância.
5. **Monitoramento e Manutenção**: Usamos os serviços integrados da AWS para monitorar o desempenho e o status da instância EC2 e da API. Isso nos permite reagir rapidamente a quaisquer problemas ou demandas aumentadas, ajustando os recursos conforme necessário.

Com a combinação de um modelo pré-treinado e a robusta infraestrutura da AWS, garantimos que os usuários tenham uma experiência de alta qualidade ao interagir com nossa API, independentemente do volume de solicitações.

## Glossário

- **Acurácia**: Mede a proporção total de previsões corretas.
- **Precisão**: Proporção de previsões positivas que foram corretamente classificadas.
- **Revocação**: Proporção de observações positivas reais que foram corretamente classificadas.
- **F1-Score**: Média harmônica da precisão e revocação, fornecendo um balanço entre as duas métricas.
- **Matriz de Confusão**: Tabela que mostra a distribuição das previsões do modelo em relação aos valores reais.
