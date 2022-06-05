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

