---
layout: page
title: common/unzip (português (Brasil))
description: "Ferramenta de descompactação de arquivos zip."
content_hash: 10681d0b5c9fbe9e9816238901d78ad335d59d8f
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unzip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unzip

Ferramenta de descompactação de arquivos zip.

- Extraindo arquivos zip:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.zip</span>

- Extraindo arquivos zip para caminhos específicos:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.zip</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para</span>

- Listando conteúdos de arquivos zip:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.zip</span>

- Extraindo arquivos zip sobrescrevendo outros arquivos:

`unzip -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.zip</span>

- Extraindo arquivos zip não sobrescrevendo outros arquivos:

`unzip -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.zip</span>

- Extraindo arquivos zip sem a estrutura dos diretórios:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.zip</span>
