# Desafio Bemol Digital Ciência de Dados

## Análise de Dados Brazilian E-Commerce Public Dataset by Olist
O presente artigo foi produzido com o intuito de apresentar uma análise de dados frente ao banco de dados Brazilian E-Commerce Public Dataset by Olist.zip, disponibilizado através das etapas do estágio para ciência de dados da Bemol Digital.

### Ferramentas Utilizadas
Linguagens:
- Python
Bibliotecas:
- Pandas 
- Altair 
- Matplotlib.pyplot
- Matplotlib.ticker

## 1. Análise de Performance de Vendas
    b.	Análise de Sazonalidade: Investigar padrões de sazonalidade nas vendas, identificando os períodos do ano com maior volume de vendas.    

#### O conjunto de dados apresentado no gráfico abaixo demonstra o volume de vendas por ano, tornando explícito que em 2016 não houve dados suficientes para gerar dados relevantes. Fato este constatado ao decorrer do tempo, nota-se que o volume de vendas cresce, disparando no último bimestre de 2017, atingindo seu ápice nos meses de março e abril de 2018.

![Volume de vendas por bimestre](./d_bemol/imagens/volume-vendas-bimestre-ano.png)



#### Insights valiosos podem ser extraídos, como o fato de que o pico do volume de vendas não ocorreu nas festas de final de ano, mas sim no segundo bimestre do ano de 2018, que possui os dados mais confiáveis.

## 2. Análise de logística
    a. Prazos de Entrega: Calcular o tempo médio de entrega e identificar os fatores que influenciam os atrasos nas entregas.

#### Durante a análise, descobrimos que os dados revelam-se mais esclarecedores quando examinamos frente ao tempo de entrega e os estados envolvidos. No entanto, eles carecem de informações sobre as possíveis causas de atraso. Embora tenhamos considerado o tamanho e peso dos produtos, encontramos maior valor nos dados relacionados às entregas em diferentes estados. Foi nesse contexto que percebemos uma correlação significativa com os maiores indíces de atrasos nas entregas.

![Atraso Por estado](./d_bemol/imagens/atraso-estado.png)

#### Podemos perceber um grande índice de atrasos nas entregas dos estados da região Norte do país. Em contraste, a região Nordeste apresenta os melhores índices, possivelmente relacionados à sua localização costeira favorável. Isso desempenha um papel importantíssimo para a logística no Brasil. Com mais dados, podemos relacionar as melhores práticas para alinhar estoque e entregas importadas visando a diminuição de custos.



## 3. Análise de Satisfação do Cliente
    a.	Avaliações de Produtos: Analisar a distribuição das avaliações dos produtos e identificar os produtos com as melhores e piores avaliações.

![Avaliações](./d_bemol/imagens/10-avaliações.png)

#### A avaliação de produtos por meio de notas tem se mostrado uma ferramenta valiosa para a tomada de decisões, pois frequentemente oferece insights precisos sobre aspectos positivos e negativos. Muitas vezes, uma avaliação representa uma comunicação direta com o cliente final, tornando-se, assim, crucial. Os dados disponibilizados revelam lacunas no negócio e ajudam na tomada de decisões. Como mostrado nos gráficos, os serviços e seguros são os itens menos agradáveis, o que é de se esperar. Por outro lado, a categoria de áudio carece de atenção, pois é uma parte importante das vendas no mercado brasileiro. Os dados destacam quais produtos são bem recebidos pelos clientes e quais não alcançam suas expectativas. É importante relacionar esses dados com a lucratividade e otimizar as vendas com base nos insights revelados.




## 4. Análise Financeira
    a.	Análise de Lucratividade por Categoria: Calcular a lucratividade de diferentes categorias de produtos, levando em conta o custo dos produtos e o preço de venda.



##### Os dados apresentados não retratavam os custos dos produtos diretamente, para tal foi considerado a margem de lucro de 20% no preço do produto sem o frete, para gerar o gráfico também foi diminuido as vendas do tipo voucher, com o intuito de aproximar os dados da lucratividade da precisão.

![Melhores Avaliações](./d_bemol/imagens/avaliação-categorias.png)

#### Os dados mostraram a grande dominação de lucratividade no setor de telefonia, seguidos por utilidade domestica, computadores e artes, Com a telefonia tendo quase o dobro da lucratividade das categorias mais proximas a ela.
