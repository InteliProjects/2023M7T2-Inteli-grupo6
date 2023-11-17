# Sistema de Manutenção Preditiva para Azul Linhas Aéreas

Bem-vindo à pasta de notebooks do projeto de Manutenção Preditiva para a Azul Linhas Aéreas. Nesta coleção de notebooks, você encontrará o processo de Extração, Transformação e Carregamento (ETL) dos dados necessários para a construção e treinamento dos modelos de machine learning voltados à manutenção preditiva. Este projeto tem como objetivo otimizar os processos de manutenção de aeronaves, reduzindo custos e aumentando a eficiência operacional.

## Sobre o Projeto

O objetivo principal deste projeto é desenvolver modelos de machine learning capazes de prever falhas e necessidades de manutenção em aeronaves da Azul Linhas Aéreas. Ao aplicar análises avançadas aos dados coletados das aeronaves em operação, pretendemos identificar padrões que indiquem possíveis problemas futuros. Isso permitirá que a Azul possa agendar a manutenção de forma mais eficaz, evitando atrasos e interrupções desnecessárias.

## Notebooks

Aqui está a lista dos notebooks disponíveis nesta pasta, cada um desempenhando um papel crucial na fase de ETL do projeto:

1. **01-coleta-dados.ipynb** : Este notebook abrange o processo de coleta de dados brutos das aeronaves. Utilizaremos sensores e sistemas embarcados para capturar informações em tempo real, como temperatura, pressão, vibração, entre outros.
2. **02-limpeza-preprocessamento.ipynb** : Neste notebook, você encontrará os passos para limpeza e pré-processamento dos dados brutos coletados. Isso envolve a remoção de outliers, preenchimento de valores ausentes e a normalização dos dados.
3. **03-engenharia-recursos.ipynb** : Aqui, realizamos a engenharia de recursos, onde transformamos os dados pré-processados em características relevantes para o treinamento dos modelos. Isso pode incluir a criação de estatísticas agregadas, seleção de atributos relevantes e criação de variáveis dummy.
4. **04-integracao-dados.ipynb** : Neste notebook, consolidamos os dados de diferentes fontes em um único conjunto de dados pronto para ser utilizado no treinamento dos modelos. Isso envolve a combinação de dados de diferentes sensores e sistemas da aeronave.
5. **05-validacao-dados.ipynb** : Antes de treinar os modelos, é crucial validar a qualidade dos dados. Neste notebook, realizamos verificações de integridade e qualidade nos dados consolidados.

## Instruções de Uso

Para garantir o sucesso do projeto, siga estas etapas ao utilizar os notebooks:

1. Execute os notebooks em ordem, do 01 ao 05, para garantir que o processo de ETL seja completo e coerente.
2. Leia atentamente os comentários e documentações internas de cada notebook para entender as transformações aplicadas aos dados.
3. Mantenha a estrutura de pastas intacta, pois os notebooks podem depender de arquivos gerados anteriormente.
4. Ao final do ETL, os dados preparados serão salvos em um formato adequado para o treinamento dos modelos de machine learning.
5. Certifique-se de documentar quaisquer alterações significativas ou insights obtidos durante o processo de ETL.
