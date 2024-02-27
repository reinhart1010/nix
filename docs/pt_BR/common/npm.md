---
layout: page
title: common/npm (português (Brasil))
description: "Gerenciador de pacotes JavaScript e Node.js."
content_hash: b9111b7975e9941d4d0003d1c3883c6625d25b68
last_modified_at: 2024-02-27
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

Gerenciador de pacotes JavaScript e Node.js.
Gerencia projetos Node.js e suas dependências de módulos.
Mais informações: <https://www.npmjs.com>.

- Interativamente cria um arquivo `package.json`:

`npm init`

- Baixa todos os pacotes listados como dependências em `package.json`:

`npm install`

- Baixa uma versão específica de um pacote e o adiciona à lista de dependências em `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Baixa a última versão de um pacote e o adiciona à lista de dependências de desenvolvimento em `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --save-dev`

- Baixa a última versão de um pacote e o instala globalmente:

`npm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Desinstala um pacote e o remove da lista de dependências em `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Lista as dependências instaladas localmente:

`npm list`

- Lista os pacotes de nível superior instalados globalmente:

`npm list --global --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
