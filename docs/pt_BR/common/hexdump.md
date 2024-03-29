---
layout: page
title: common/hexdump (português (Brasil))
description: "Imprime dados no formato ASCII, decimal, hexadecimal ou octal."
content_hash: 9557b5dfc6471de8d422b3cbc1a7a9d9c80ba554
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/hexdump.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hexdump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexdump

Imprime dados no formato ASCII, decimal, hexadecimal ou octal.
Mais informações: <https://manned.org/hexdump>.

- Imprime a representação hexadecimal de um arquivo, substituindo linhas duplicadas por '*':

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime a representação hexadecimal e ASCII de um arquivo, em duas colunas:

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime a representação hexadecimal de um arquivo, porém apresentando apenas seus n primeiros bytes:

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime a representação hexadecimal completa de um arquivo (sem omitir linhas duplicadas):

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
