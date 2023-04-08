# scrapp-data-api

Repositório com os scripts de webscrapping dos dados de supermercados e da API que intermedia a interacao com a aplicacao mobile.


### Tabela de Conteúdo
- [Consideracoes](#resumo)
- [Estrutura de Diretórios](#tree)
- [Uso Local](#uso)


## Consideracoes
Para fazer o post na API com os dados dos supermercados é preciso preparar o ambiente local, ou seja, clonar o repositório, criar um ambiente virtual e rodar os comandos no Makefile dentro do ambiente virtual criado. Os dados são coletados via webscrapping utilizando as bibliotecas bs4 e resquests e a API foi desenvolvida com FastAPI, persistindo os dados no banco de dados relacional SQLite3. Ambos em Python3.


## Estrutura de Diretórios

```
.
├───.gitignore
├───delete.py
├───get.py
├───Makefile
├───post.py
├───README.md
├───requirements.txt
├───response.txt
├───tree.txt
│   
├───api
│   ├───main.py
│   │   
│   ├───database
│   │   ├───database.py
│   │   ├───db.sqlite3
│   │   ├───models.py
│   │   ├───repositories.py
│   │   ├───schemas.py
│           
└───data
    ├───poc_mercadolivre.py
    ├───poc_paodeacucar.py
    ├───poc_prezunic.py
    │       
    ├───modules
    │   ├───mercadolivre.py
    │   ├───paodeacucar.py
    │   ├───prezunic.py
    │   ├───scrapper.py
```

## Uso Local

1.  Clonar repositório
2.  Preparar ambiente local - Se Windows, baixar e instalar [GNUWin32/Make](https://gnuwin32.sourceforge.net/packages/make.htm)
3.  Rodar comandos do Makefile


#### Clonar repositório

git clone https://github.com/beer-code-pizza/data.git

#### Criar ambiente virtual
No MacOS - [virtualenvwrapper - via brew](https://formulae.brew.sh/formula/virtualenvwrapper)


No Windows - [venv - Windows PowerShell](https://docs.python.org/pt-br/dev/library/venv.html)

#### Entrar no ambiente virtual 

[Usando Python no VS Code com ambiente virtual (venv)](https://oandersonbm.medium.com/usando-python-no-vs-code-com-ambiente-virtual-venv-ecef7959b652)

#### Rodar comandos do Makefile
Para instalar os pre-requisitos
```
make install-requirements
```

Para fazer webscrapp dos dados
```
make scrapp-data
```

Para subir a API
```
make up-api
```

Para fazer requisicao GET na API
```
make get-api
```

Para fazer requisicao POST na API
```
make post-api
```

Para fazer requisicao DELETE na API
```
make delete-api
```