# Desafio
## Descrição
No desafio proposto era preciso realizar a indexação de palavras e a relação que elas possam ter entre si. Foi indicado realizar a busca e a indexação das palavras de um dicionário online. Após isso era necessário criar algum modelo que representasse as palavras e suas relações. Também foi pedido para apresentar este modelo de forma "agradável" ao usuário e publicamente.

## Solução proposta
Utilizando de algumas dicas apresentadas no desafio, decidi utilizar o site [dicionariocriativo.com.br](https://dicionariocriativo.com.br/) como base de informação. Deste site, fiz um script que realizava busca das palavras e registrava seus sinônimos e antônimos.

Para armazenamento foi utilizado o banco de dados de grafo [neo4j](https://neo4j.com/). Este banco foi escolhido por acreditar que o modelo de dados do problema é um modelo de relacionamento facilmente representado através de grafos. 

Como ferramenta de exibição dos dados foi utilizada a biblioteca [cytoscape](https://js.cytoscape.org/) para visualização e manipulação de dados através de uma interface web. Esta biblioteca é construida em javascript e é utilizada para criação de gráficos e grafos dinâmicos.

Para construir a aplicação foi escolhida a linguagem [Python](https://www.python.org/) na sua versão 3.8 e o framework web [Flask](https://flask.palletsprojects.com/en/1.1.x/). A linguagem foi escolhida pela sua facilidade de desenvolvimento e pela grande gama de bibliotecas disponíveis para scraping, manipulação de grafos e páginas webs.

Por fim, para disponibilizar o uso da aplicação através de containers, foi utilizado o [docker hub](https://hub.docker.com/) e tendo as imagens disponibilizadas no repositório [hub.docker.com/u/victoramsantos](https://hub.docker.com/u/victoramsantos). Já para disponibilizar publicamente, foi construido um script em [terraform](https://www.terraform.io/) para realizar o deploy dos containers da aplicação na infraestrutura da [aws](https://aws.amazon.com/).