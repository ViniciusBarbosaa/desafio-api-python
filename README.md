# desafio-api-python

Título do Projeto
  API monetaria em python

Descrição do Problema
    O problema abordado por esta aplicação é a necessidade de realizar conversões monetárias entre diferentes moedas de forma fácil e eficiente. Em um cenário globalizado, onde transações financeiras ocorrem internacionalmente, ter uma ferramenta que forneça taxas de câmbio atualizadas e permita a conversão de valores em tempo real é essencial.
  
  Muitas vezes, obter taxas de câmbio precisas pode ser um desafio, e as soluções existentes podem ser complexas ou exigir acesso a serviços especializados. Esta aplicação resolve esse problema fornecendo uma API simples e acessível que permite aos usuários converter valores monetários entre uma variedade de moedas, incluindo Dólar Americano (USD), Real Brasileiro (BRL), Euro (EUR), Bitcoin (BTC), Ethereum (ETH) e outras.
  
  Além disso, a aplicação oferece a capacidade de adicionar novas moedas dinamicamente, mantendo-se flexível para atender a requisitos específicos do usuário.

Pré-requisitos
  Lista de pré-requisitos que os usuários precisam ter instalados em seus sistemas antes de começarem.
  
  Docker 
  Git
  Flask
  requests

Configuração do Ambiente
  Instruções sobre como configurar o ambiente de desenvolvimento. Isso pode incluir a clonagem do repositório, instalação de     dependências, etc.
  
  git clone https://github.com/seu-usuario/seu-fork.git
  cd seu-fork

Instalação de Dependências
  pip install -r requirements.txt

Configuração do Docker

  docker build -t imagem .
  docker run -p 5000:5000 imagem

Uso

  curl "http://localhost:5000/convert?from=USD&to=BRL&amount=100.00"
  curl "http://localhost:5000/currencies"
