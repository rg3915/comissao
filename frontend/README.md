# Frontend

## Este projeto foi feito com:

* [Node 16.17.0 LTS](https://nodejs.org/en/)
* [VueJS 2.6.11](https://vuejs.org/)

Pode instalar o node com [nvm](https://github.com/nvm-sh/nvm).

```
# Linux
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

## Como rodar o frontend

```
npm install
npm run serve
```

Se der erro ao rodar o projeto, então verifique em `package.json` a versão do `babel-eslint`.

```
"babel-eslint": "^8.2.2",
```

Remova a pasta `node_modules`, e instale novamente.

ref: https://qdmana.com/2022/02/202202260505530778.html