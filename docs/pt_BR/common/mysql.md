---
layout: page
title: common/mysql (português (Brasil))
description: "A ferramenta de linha de comando do MySQL."
content_hash: 2e68ffa1cfcd2042081b47d14dde593475fe3556
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysql.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/mysql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/mysql.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mysql.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mysql

A ferramenta de linha de comando do MySQL.
Mais informações: <https://www.mysql.com/>.

- Conectar a um banco de dados:

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>

- Conectar a um banco de dados (será solicitada a senha de acesso do usuário):

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>

- Conectar a um banco de dados disponível em um endereço específico:

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco_do_banco_de_dados</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>

- Conectar a um banco de dados utilizando um socket Unix:

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/socket.sock</span>

- Executar todos os comandos de um arquivo SQL em um banco de dados:

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_banco_de_dados</span>
