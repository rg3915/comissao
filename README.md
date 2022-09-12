# comissao

Sistema de Comissão de vendas e serviços feito em Django.

<a href="">
    <img src="img/youtube.png">
</a>

## Este projeto foi feito com:

* [Python 3.10.4](https://www.python.org/)
* [Django 4.0.5](https://www.djangoproject.com/)
* [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/)
* [VueJS](https://vuejs.org/)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/comissao.git
cd comissao
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## Frontend

### Este projeto foi feito com:

* [Node 16.17.0 LTS](https://nodejs.org/en/)
* [VueJS 2.6.11](https://vuejs.org/)

Pode instalar o node com [nvm](https://github.com/nvm-sh/nvm).

```
# Linux
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

## Como rodar o frontend

Entrar na pasta `frontend` e instalar as dependências do VueJS.

```
cd frontend
npm install

npm run serve
```

Template: https://www.creative-tim.com/product/vuetify-material-dashboard

Se der erro ao rodar o projeto, então verifique em `package.json` a versão do `babel-eslint`.

```
"babel-eslint": "^8.2.2",
```

Remova a pasta `node_modules`, e instale novamente.

ref: https://qdmana.com/2022/02/202202260505530778.html