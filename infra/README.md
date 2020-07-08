# terraform
Projeto para construção de stack terraform.

#### Descrição
Este projeto possui dois providers, sendo:
- **master_vpc:** constroi uma VPC com 4 Subnets (2 públicas e 2 privadas). Também é criado um Nat Gateway em uma subnet pública com rotas das subnets privadas para pública. Por fim, é criado um Internet Gateway na VPC e as rotas das subnets públicas para ele.
- **deploy_env:** constroi uma stack com Application Loadbalancer redirecionando para um Target Group. Também é criado uma instância EC2 que será registrada no Target Group e com user-data que instala o docker. _É importante notar que esse provider é específico para o exemplo._

##### Pré requisitos
- [terraform](https://learn.hashicorp.com/terraform/getting-started/install.html) 
- Ter configurado o acesso a AWS ([aws cli](https://docs.aws.amazon.com/cli/latest/reference/configure/))

##### Construindo a stack de rede
Acesse o diretório [master_vpc](providers/aws/stacks/master_vpc) e execute o comando:
```shell script
terraform init
```
Após isso execute o comando 
```shell script
terraform apply
```
Isso irá construir os componentes na AWS na região us-east-1.

##### Deploy da aplicação
Acesse o diretório [deploy_env](providers/aws/stacks/deploy_env) e execute o comando:
```shell script
terraform init
```
Após isso será necessário aplicar o provider. Ao ser aplicado será solicitado que informe o valor para as variáveis:
- **frontend_img** - imagem docker do frontend (utilize: victoramsantos/stilingue-frontend:1.0.0)
- **backend_img** - imagem docker do backend (utilize: victoramsantos/stilingue-backend:1.0.0)
- **vpc_id** - Nome da vpc que será feito o deploy da aplicação (ex.:vpc-77f0f00d)
- **public_subnets** - Nome das subnets que será feito o deploy dos loadbalancers  (ex.:["subnet-16d92b37","subnet-3f192201"])
- **ec2_key_pair:** - Nome da chave que será utilizada para acessar a EC2.

Para facilitar este processo, crie um arquivo chamado _env.tfvars_. Para exemplicar, seu arquivo deverá ser:
```
frontend_img="victoramsantos/stilingue-frontend:1.0.0"
backend_img="victoramsantos/stilingue-backend:1.0.0"
vpc_id="vpc-77f0f00d"
public_subnets=["subnet-16d92b37","subnet-3f192201"]
ec2_key_pair="nova-pem"
```

Após isso execute o comando 
```shell script
terraform apply -var-file=env.tfvars
```
Isso irá construir a stack na AWS na região us-east-1 e será  mostrado o DNS de um loadbalancer.