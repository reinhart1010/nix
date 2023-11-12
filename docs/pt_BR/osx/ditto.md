---
layout: page
title: osx/ditto (português (Brasil))
description: "Copia arquivos e diretórios."
content_hash: 7a5124738e94655d142214d1e1324ebb9da404d2
last_modified_at: 2023-11-12
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
Mais informações: <https://ss64.com/osx/ditto.html>.

- Sobrescreve o conteúdo do diretório de destino pelo conteúdo do diretório de origem:

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Imprime uma linha na janela do Terminal para cada arquivo que está sendo copiado:

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Copia um determinado arquivo ou diretório, mantendo as permissões do arquivo original:

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>
