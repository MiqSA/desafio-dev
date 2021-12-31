# Store Manager

Esse projeto consiste em parsear [este arquivo de texto(CNAB)](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados.

# Sobre

Esse projeto é composto por uma interface web que aceita upload do [arquivo CNAB](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt) (que contêm informações sobre movimentações financeiras de várias lojas), normaliza os dados e armazena em um banco de dados relacional MySQL. As informações das movimentações são exibidas na interface web.


# Tecnologias Utilizadas

## Back-end

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [MySQL](https://www.mysql.com/)

## Front-end

- HTML
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

## Testes

- Testes de unidade = [Unittest](https://docs.python.org/3/library/unittest.html)
- Testes de velocidade e estrutura = [Postman](https://learning.postman.com/docs/writing-scripts/test-scripts/)

# Como Utilizar?

```bash
# Clonar esse repositório
$ https://github.com/MiqSA/desafio-dev.git

# Entrar no pasta do projeto
$ cd desafio-dev

# Subir aplicação pelo docker
$ docker-compose up

# Mude para branch de desenvolvimento 
$ git checkout develop

# Sincronize com o repositório
$ git pull

# Garantir que o docker desktop está ativo 

$ docker-compose up --build

# A aplicação estará funcionando em http://0.0.0.0:5057/
# Ao clicar no botão "Add Data" é possível fazer o upload do arquivo CNAB.txt

```
# Endpoints disponíveis

Todos os endpoints são organizados em sua url a versão da API, isso permite que haja parelismo em desenvolvimento de melhorias dos endpoints atuais, bem como criação de outros, focando-se em escalabilidade. A versão atual é v1.0. Mais detalhes da versão poderia ser acrescida em um header customizado para mostrar detalhes da sub-versão.

Todos os endpoints retornam um dicionário (arquivo json com chaves e valores) na seguinte estrutura:
```
{
  "message": "Success",
  "results": [],
  "status": 200
}
```
Em que "message" corresponde a mensagem textual ligada aos códigos de status da resposta HTTP do endpoint, mais sobre esses códigos de status [aqui](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status). O "status" corresponde ao código de status da resposta HTTP. Já o "results" corresponde uma lista de informações que variam de acordo com a finalidade do endpoint.


- #### Nome das Lojas
    - Endereço: 
        - /stores
        - ```http://localhost:5057/v1.0/stores```
    - Retorna no "results": 
        - Lista dos nomes das lojas disponíveis no banco de dados.
          ```
          [
            "BAR DO JOÃO       ",
            "LOJA DO Ó - MATRIZ",
            "MERCADO DA AVENIDA",
            "MERCEARIA 3 IRMÃOS",
            "LOJA DO Ó - FILIAL"
          ] 
          ```
- #### Detalhes das Movimentações Financeiras das Lojas
    - Endereço: 
        - /stores/transactions
        - ```http://localhost:5057/v1.0/stores/transactions```
    - Retorna no "results": 
        - Lista a descrição da movimentação, o nome da loja e o valor da movimentação.
          ```
          [
            {
                "description": "Boleto",
                "store_name": "BAR DO JOÃO       ",
                "transaction_value": 152.0
            }, 
            ...
          ]
          ```

- #### Total das Movimentações Financeiras das Lojas
    - Endereço: 
        - /stores/transactions/total
        - ```http://localhost:5057/v1.0/stores/transactions/total```
    - Retorna no "results": 
        - Lista o valor total da movimentação por loja.
          ```
          [
            {
                "store_name": "BAR DO JOÃO       ",
                "transaction_value": 406.0
            },
            {
                "store_name": "LOJA DO Ó - FILIAL",
                "transaction_value": 152.32
            }, 
            ...
          ]
          ```

- #### Upload de arquivo para salvar no banco de dados
    - Endereço: 
        - /files/upload
        - ```http://localhost:5057/v1.0/files/upload```
    - Retorna: 
        - Redireciona para home da aplicação depois de salvar os dados em banco de dados MySQL.

# Melhorias
- Autenticação e Autorização com OAuth pode ser implementado.
- Front-end com uso de CSS e JavaScript para melhorar experiência do usuário.
- Testes de carga devem ser efetuados.



