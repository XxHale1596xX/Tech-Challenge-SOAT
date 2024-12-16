# Tech-Challenge-SOAT



Claro! Aqui está um exemplo formatado para um arquivo `README.md` que você pode usar no seu repositório GitHub. Ele inclui a descrição do projeto, instruções para uso local no Kubernetes com Kind, e exemplos de como testar a API.

```markdown
# Projeto API de Revenda de Veículos

Este projeto é uma **API RESTful** para uma plataforma de revenda de veículos automotores. Ele permite realizar operações relacionadas à compra e venda de veículos, incluindo cadastro, atualização, vendas e listagens.

## Funcionalidades

- **Cadastrar um veículo**: Cria um registro de um veículo com detalhes como marca, modelo, ano, cor e preço.
- **Editar dados do veículo**: Atualiza as informações de um veículo cadastrado.
- **Efetuar a venda de um veículo**: Registra a venda de um veículo com CPF do comprador e data da venda.
- **Listar veículos à venda**: Mostra veículos disponíveis, ordenados por preço.
- **Listar veículos vendidos**: Exibe os veículos já vendidos, também ordenados por preço.
- **Webhook de notificações de pagamento**: Endpoint para receber notificações de pagamento.

## Estrutura do Projeto

```
my_vehicle_api/
├── app/
│   ├── main.py          # Ponto de entrada da aplicação

│   ├── models.py        # Definições dos modelos de dados

│   ├── database.py      # Configurações de conexão com o banco de dados

│   ├── schemas.py       # Estruturas de dados (Pydantic)

│   └── crud.py          # Funções de acesso ao banco de dados

├── deployment.yaml      # Configuração do deployment no Kubernetes

├── service.yaml         # Configuração do serviço no Kubernetes

├── Dockerfile            # Configuração para construção da imagem Docker

└── README.md            # Documentação do projeto
```

## Como Usar Localmente no Kubernetes com Kind

### Pré-requisitos

- **Docker**: Certifique-se de que o Docker está instalado.
- **Kind**: Instale o Kind seguindo as instruções em [Kind Documentation](https://kind.sigs.k8s.io/docs/user/quick-start/).
- **kubectl**: Instale o `kubectl` para se comunicar com o cluster Kubernetes.

### Passo a Passo

1. **Criar um cluster Kind**:
   ```bash
   kind create cluster
   ```

2. **Construir a imagem Docker**:
   Navegue até o diretório do projeto e construa sua imagem Docker:
   ```bash
   docker build -t seu_usuario/seu_imagem:latest .
   ```

3. **Carregar a imagem no Kind**:
   Carregue a imagem Docker no cluster Kind:
   ```bash
   kind load docker-image seu_usuario/seu_imagem:latest
   ```

4. **Aplicar as configurações do Kubernetes**:
   Aplique os arquivos de configuração para o deployment e o serviço:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

5. **Verificar o status dos pods e serviços**:
   Confira se os pods estão rodando e obtenha informações do serviço:
   ```bash
   kubectl get pods
   kubectl get services
   ```

### Acessando a Aplicação

1. **Descobrir o NodePort**:
   Localize a porta atribuída ao seu serviço (type: NodePort) na saída do comando `kubectl get services`.

2. **Acessar a API**:
   Use o IP do cluster para acessar sua aplicação. Geralmente, você pode acessar em `http://127.0.0.1:<NodePort>`.

## Testando a API

Você pode testar a API utilizando comandos `curl` ou ferramentas como **Postman**. Aqui estão alguns exemplos:

1. **Cadastrar um veículo**:
   ```bash
   curl --location 'http://127.0.0.1:8000/vehicles/' \
--header 'Content-Type: application/json' \
--data '{"brand": "Toyota", "model": "Corolla", "year": 2020, "color": "Blue", "price": 30000}'
   ```

2. **Editar um veículo**:
   ```bash
   curl --location --request PUT 'http://127.0.0.1:8000/vehicles/1' \
--header 'Content-Type: application/json' \
--data '{"brand": "Honda", "model": "Civic", "year": 2022, "color": "Red", "price": 35000}'
   ```

3. **Efetuar a venda de um veículo**:
   ```bash
   curl --location 'http://127.0.0.1:8000/vehicles/7/sell' \
--header 'Content-Type: application/json' \
--data '{"customer_cpf": "12345678901", "sale_date": "2024-08-12"}'
  ```

4. **listar veiculos a venda**:
   ```bash
curl --location 'http://127.0.0.1:8000/vehicles/for-sale/''
   ```

5. **listar veiculos vendidos**:
   ```bash
curl --location 'http://127.0.0.1:8000/vehicles/sold/'
   ```

6. **Webhook**:
   ```bash
curl --location 'http://127.0.0.1:8000/payment-webhook/' \
--header 'Content-Type: application/json' \
--data '{"payment_code": "123456", "status": "completed"}'
   ```

