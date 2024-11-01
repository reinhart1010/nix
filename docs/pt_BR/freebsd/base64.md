---
layout: page
title: freebsd/base64 (português (Brasil))
description: "Codifica ou decodifica arquivo ou `stdin` de/para base64, para `stdout` ou outro arquivo."
content_hash: 684578fb7b242790241465d53dfff840d00d6e9e
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/freebsd/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

Codifica ou decodifica arquivo ou `stdin` de/para base64, para `stdout` ou outro arquivo.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Codifica um arquivo para `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Codifica um arquivo para o arquivo de saída especificado:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_entrada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_saída</span>

- Quebra (insere uma quebra de linha) a saída codificada em uma largura específica (‘0’ desabilita encapsulamento):

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--break</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|76|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Decodifica um arquivo para `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Codifica de `stdin` para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | base64`

- Decodifica de `stdin` para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>
