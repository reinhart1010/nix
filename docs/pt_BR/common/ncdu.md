---
layout: page
title: common/ncdu (português (Brasil))
description: "Analisador de uso de disco com uma interface ncurses."
content_hash: 9a691a0c0d251229bb9242650efea6f1a82cdba1
last_modified_at: 2024-02-27
related_topics:
  - title: dansk version
    url: /da/common/ncdu.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ncdu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ncdu

Analisador de uso de disco com uma interface ncurses.
Mais informações: <https://manned.org/ncdu>.

- Analisa o diretório de trabalho atual:

`ncdu`

- Colore a saída:

`ncdu --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|off</span>

- Analisa um dado diretório:

`ncdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Salva os resultados em um arquivo:

`ncdu -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Exclui arquivos que correspondem a um padrão, o argumento pode ser fornecido várias vezes para adicionar mais padrões:

`ncdu --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`'`
