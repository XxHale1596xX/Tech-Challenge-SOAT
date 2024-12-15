# Tech-Challenge-SOAT



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

## Como Usar Localmente no Kubernetes com Kind

### Pré-requisitos

- **Docker**: Certifique-se de que o Docker está instalado.
- **Kind**: Instale o Kind seguindo as instruções em [Kind Documentation](https://kind.sigs.k8s.io/docs/user/quick-start/).
- **kubectl**: Instale o `kubectl` para se comunicar com o cluster Kubernetes.

### Passo a Passo

1. **Criar um cluster Kind**:
   ```bash
   kind create cluster
