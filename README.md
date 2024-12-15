# Tech-Challenge-SOAT



Descrição do Projeto
O projeto é uma API RESTful para uma plataforma de revenda de veículos automotores. O objetivo principal é permitir que os usuários realizem operações relacionadas à compra e venda de veículos, incluindo cadastro de novos veículos, atualização de informações, registro de vendas, e listagens de veículos disponíveis e já vendidos.

Funcionalidades da API
Cadastrar um veículo: Permite que um usuário crie um registro de um veículo com detalhes como marca, modelo, ano, cor e preço.
Editar dados do veículo: Permite que informações de um veículo cadastrado sejam atualizadas.
Efetuar a venda de um veículo: Registra a venda de um veículo, armazenando o CPF do comprador e a data da venda.
Listar veículos à venda: Oferece uma lista de veículos disponíveis para venda, ordenada pelo preço, do mais barato para o mais caro.
Listar veículos vendidos: Permite visualizar os veículos que já foram vendidos, também ordenados por preço.
Webhook para notificações de pagamento: Um endpoint que pode receber notificações de uma entidade de pagamento, informando se um pagamento foi efetuado ou cancelado.
Implementação
A API foi desenvolvida usando o framework FastAPI em Python, que oferece alta performance e é simples de usar para a construção de APIs. O código foi estruturado seguindo os princípios de Clean Architecture e orientado por SOLID, de forma a permitir a manutenibilidade e escalabilidade.

As interações com a base de dados são feitas usando SQLAlchemy, e a persistência de dados está configurada para uma base de dados SQLite (ideal para desenvolvimento e testes locais).


Como Usar Localmente no Kubernetes com Kind
Pré-requisitos:

Instale o Docker e o Kind (Kubernetes IN Docker) em sua máquina.
Certifique-se de que tem o kubectl instalado.

Criar um cluster Kind:

Execute o seguinte comando para criar um novo cluster Kubernetes:
-- kind create cluster

Construir a imagem Docker:
Primeiro, crie uma imagem Docker da aplicação utilizando o Dockerfile. Execute:
-- docker build -t seu_usuario/seu_imagem:latest .

Carregar a imagem no Kind:
Se você estiver usando Kind, precisará carregar a imagem local no cluster. Use o seguinte comando:
-- kind load docker-image seu_usuario/seu_imagem:latest

Aplicar as configurações do Kubernetes:
Aplique as definições de deployment e service para sua aplicação:
-- kubectl apply -f deployment.yaml
-- kubectl apply -f service.yaml

Verificar o status dos pods e serviços:
Certifique-se de que os pods estão rodando:
-- kubectl get pods -A

Acessando a Aplicação
Descobrir o NodePort:
Localize a porta que foi atribuída ao seu serviço (type: NodePort). Você pode ver isso na saída do comando kubectl get services.

Acessar a API:
Use o IP do cluster para acessar sua aplicação. Se você estiver rodando o Kind localmente, normalmente você pode acessar em http://127.0.0.1:<NodePort>.

Como Testar
Você pode testar a API utilizando o curl ou ferramentas como Postman. Segue alguns exemplos de
