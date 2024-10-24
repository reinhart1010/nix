---
layout: page
title: common/npm (português (Brasil))
description: "Gerenciador de pacotes JavaScript e Node.js."
content_hash: e1058bcb9820c07143f27744d25ca4172a97fda2
last_modified_at: 2024-10-24
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
  - title: Nederlands version
    url: /nl/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

Gerenciador de pacotes JavaScript e Node.js.
Gerencia projetos Node.js e suas dependências de módulos.
Mais informações: <https://www.npmjs.com>.

- Cria um arquio `package.json` com os valores padrões (omita `--yes` para torná-lo interativo):

`npm init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-y|--yes</span>

- Baixa todos os pacotes listados como dependências em `package.json`:

`npm install`

- Baixa uma versão específica de um pacote e o adiciona à lista de dependências em `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Baixa a última versão de um pacote e o adiciona à lista de dependências de desenvolvimento em `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- Baixa a última versão de um pacote e o instala globalmente:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Desinstala um pacote e o remove da lista de dependências em `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Lista todas as dependências instaladas localmente:

`npm list`

- Lista todos os pacotes de nível superior instalados globalmente:

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
