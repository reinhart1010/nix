---
layout: page
title: common/fossil-add (português (Brasil))
description: "Coloca arquivos ou diretórios sob o controle de versão do Fossil."
content_hash: ccfc09593a2693edd8d0fdf18da0a14c16cfa13c
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/fossil-add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fossil-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fossil add

Coloca arquivos ou diretórios sob o controle de versão do Fossil.
Mais informações: <https://fossil-scm.org/home/help/add>.

- Coloca um arquivo ou diretório sob o controle de versão, de forma que ele estará no checkout atual:

`fossil add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Remove todos os arquivos adicionados do checkout atual:

`fossil add --reset`
