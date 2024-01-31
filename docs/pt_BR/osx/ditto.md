---
layout: page
title: osx/ditto (português (Brasil))
description: "Copia arquivos e diretórios."
content_hash: 482106e02b7d3e5162437ff7d9a80236df98327d
last_modified_at: 2024-01-31
related_topics:
  - title: বাংলা version
    url: /bn/osx/ditto.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/ditto.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ditto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ditto

Copia arquivos e diretórios.
Mais informações: <https://keith.github.io/xcode-man-pages/ditto.1.html>.

- Sobrescreve o conteúdo do diretório de destino pelo conteúdo do diretório de origem:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Imprime uma linha na janela do Terminal para cada arquivo que está sendo copiado:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Copia um determinado arquivo ou diretório, mantendo as permissões do arquivo original:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>
