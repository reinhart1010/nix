---
layout: page
title: common/strings (português (Brasil))
description: "Procura strings imprimíveis em um arquivo objeto ou binário."
content_hash: bad4bc3eb2cf7383558ec7e978b23afaedd9ef9f
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/strings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/strings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/strings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># strings

Procura strings imprimíveis em um arquivo objeto ou binário.
Mais informações: <https://manned.org/strings>.

- Imprime todas as strings em um binário:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Limita resultados a strings com pelo menos n caracteres:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Prefixa cada resultado com seu deslocamento dentro do arquivo:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Prefixa cada resultado com seu deslocamento dentro do arquivo em hexadecimal:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
