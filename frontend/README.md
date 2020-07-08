# Frontend
Para o frontend decidi utilizar uma solução monolítica tendo o Python servindo como servidor e construtor das páginas html.
Foi escolhido [Flask](https://flask.palletsprojects.com/en/1.1.x/) para construção do servidor. Optei por utilizar uma solução baseada em [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) com o uso de [Blueprints do Flask](https://flask.palletsprojects.com/en/1.1.x/blueprints/) usado na construção de aplicações modulares.
Na parte cliente, usamos a biblioteca [cytoscape](https://js.cytoscape.org/) além de [jquery](https://jquery.com/) e html básico.

A solução conta com um controlador que responde no path /. Este path pode receber via [query string](https://en.wikipedia.org/wiki/Query_string) o parâmetro _word_, que é utilizado para pesquisar na base de dados o seus relacionamentos.

Na interface web mostrada, é possível com dois cliques realizar uma nova busca, recarregando a página alterando o parâmetro _word_.

## Débitos Técnicos
- Seria muito interessante separar o cliente do servidor, uma aplicação node seria uma boa abordagem.