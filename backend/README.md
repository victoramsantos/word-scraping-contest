# Backend

Decidi separar separar do frontend as funções de scraping das palavras. Acredito que está função seria melhor feita em um processo batch o qual alimentaria o banco de dados.
Desta forma criei um script que [faz o scrap do site](./src/scraper/scraper.py) o qual é usado por uma [função com as regras de negócio para popular](./src/process/process.py) o [banco de dados de grafo](./src/database/database.py).
Para exceução do scrip é indicado a execução do [docker-compose](./docker-compose.yml). Neste compose já estão configuradas as variáveis de ambiente para configuração do banco de dados, a primeira palavra (usada como base para pesquisar as demais) e a váriavel _DEPTH_INTERACTIONS_ que representa quantidade de interações que serão feitas no site (quantidade de vezes que serão feitas buscas no site).

## Débitos técnicos
- Este script foi construido de forma sincrona. Uma melhor abordagem melhor seria o uso de [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) ou [threading](https://docs.python.org/3/library/threading.html).
- Poderia ter sido  utilizado outras relações entre as palavras, talvez utilizando outra fonte de dados.