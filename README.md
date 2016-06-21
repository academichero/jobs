# Academic Job Board
O Job Board é uma plataforma online que permite o encontro perfeito entre a busca por vagas no mercado de trabalho e a busca por profissionais qualificados.

## Como contribuir com o desenvolvimento
1. Faça um fork do repositório
2. Faça suas alterações no seu repositório
3. Envie um pull request

## Como instalar?
Se você estiver utilizando uma distribuição Ubuntu ou Debian, precisará instalar alguns pacotes:

1. sudo apt-get install libncurses-dev g++ git-core

Precisamos fazer o download do nosso código fonte, digite:
```shell
git clone https://github.com/academichero/jobs.git
```
A plataforma utiliza a linguagem Python e o Web Framework Django portanto é necessário possuir os seguintes requerimentos:

1. Python >= 3.5
2. Django >= 1.9

Para começarmos a instalar nossas dependências, precisamos criar um ambiente virtual onde as bibliotecas do Python serão instaladas:
```shell
cd jobs && python3 -m venv ambiente
```
A seguir nós vamos habilitar nosso ambiente virtual de desenvolvimento e instalar nossas dependências:
```shell
source ambiente/bin/activate
pip install -r deploy/requirements-dev.txt
```

Com todas as dependências instaladas, precisamos então utilizar um arquivo de configurações locais,
para isso, vamos copiar um arquivo de exemplo já existente em nosso projeto. Na pasta app você encontrará o arquivo **settings.sample.py**, faça uma cópia alterando o nome para **settings.py**

Após copiar o arquivo de configurações precisamos criar nosso banco de dados, digite o seguinte comando no terminal:
```shell
python manage.py migrate
```

Então agora podemos rodar nossa aplicação:
```shell
python manage.py runserver
```

Você deverá ver essa mensagem:
```shell
Performing system checks...

System check identified no issues (0 silenced).
Django version 1.9.7, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Para visualizar em funcionamento, acesse o endereço: http://127.0.0.1:8000/
