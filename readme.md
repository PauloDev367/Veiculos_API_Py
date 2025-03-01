# API de Veículos

Este é um projeto de API para gerenciamento de veículos, desenvolvido com Django Rest Framework e MySQL.

## Tecnologias Utilizadas
- **Python**: 3.8.0
- **Framework**: Django com Django Rest Framework
- **Banco de Dados**: MySQL

## Pré-requisitos
Antes de rodar o projeto, você precisa garantir que as dependências estão instaladas corretamente e que o ambiente de desenvolvimento esteja configurado.

### 1. Instalação das Dependências

Primeiro, instale as dependências do projeto. Certifique-se de ter o **Python 3.8.0** ou versão superior e o **pip** instalados.

Execute o seguinte comando no diretório raiz do projeto:

```bash
pip install -r requirements.txt
```

Isso irá instalar todas as bibliotecas necessárias, conforme listado no arquivo `requirements.txt`.

### 2. Acessando o Diretório do Projeto

Acesse o diretório `veiculos`, onde o projeto Django está localizado:

```bash
cd veiculos/
```

### 3. Configuração do Banco de Dados

Certifique-se de que você tenha o **MySQL** configurado e acessível. Para isso, crie um banco de dados e configure o acesso no arquivo `settings.py` em:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Rodando o Servidor

Após configurar o banco de dados, você pode rodar as migrações e subir o servidor.

1. **Rodar as migrações do banco de dados**:

```bash
python manage.py migrate
```

2. **Subir o servidor**:

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

## Dicas de Desenvolvimento

Para uma melhor experiência, recomendamos o uso do **pyenv** para gerenciar versões do Python e do **virtualenv** para criar ambientes virtuais isolados para o projeto. 

### Instalando o `pyenv` (se necessário)

- Para instalar o `pyenv`, siga as instruções [aqui](https://github.com/pyenv/pyenv).
- Após a instalação, use o `pyenv` para instalar a versão correta do Python:

```bash
pyenv install 3.8.0
pyenv local 3.8.0
```

Isso garantirá que você está usando a versão correta do Python no ambiente do projeto.