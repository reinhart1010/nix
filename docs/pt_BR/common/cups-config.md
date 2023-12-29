---
layout: page
title: common/cups-config (português (Brasil))
description: "Mostra informação técnica sobre a instalação do seu servidor de impressão CUPS."
content_hash: c7ee864a37bb9344402dbbbcca11edbd92db0e92
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/cups-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cups-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cups-config

Mostra informação técnica sobre a instalação do seu servidor de impressão CUPS.
More information: <https://openprinting.github.io/cups/doc/man-cups-config.html>.

- Mostra a versão do CUPS instalada atualmente:

`cups-config --version`

- Mostra onde o CUPS está instalado atualmente:

`cups-config --serverbin`

- Mostra a localização do diretório de configuração do CUPS:

`cups-config --serverroot`

- Mostra a localização do diretório de dados do CUPS:

`cups-config --datadir`

- Mostra todos as opções disponíveis:

`cups-config --help`
