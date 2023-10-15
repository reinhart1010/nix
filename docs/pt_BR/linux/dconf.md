---
layout: page
title: linux/dconf (português (Brasil))
description: "Gerencia banco de dados dconf."
content_hash: 95174d9ab24deee19f8d7d0dbf280316598cead4
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/linux/dconf.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dconf

Gerencia banco de dados dconf.
Veja também: `dconf-read`, `dconf-reset`, `dconf-write`, `gsettings`.
Mais informações: <https://manned.org/dconf>.

- Imprime um valor de chave específico:

`dconf read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>

- Imprime sub-diretórios e sub-chaves de um caminho específico:

`dconf list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/diretório/</span>

- Grava um valor de chave específico:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Redefine um valor de chave específico:

`dconf reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave</span>

- Observa alterações em uma chave/diretório específico:

`dconf watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/chave|/caminho/para/diretório/</span>

- Despeja um diretório específico no formato de arquivo INI:

`dconf dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/diretório/</span>
