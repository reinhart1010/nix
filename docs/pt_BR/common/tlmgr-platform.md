---
layout: page
title: common/tlmgr-platform (português (Brasil))
description: "Gerencia plataformas de TeX Live."
content_hash: 2cbf04f649a647a26358486c6499801788f59195
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/tlmgr-platform.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tlmgr-platform.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-platform.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr platform

Gerencia plataformas de TeX Live.
Mais informações: <https://www.tug.org/texlive/tlmgr.html>.

- Lista todas as plataformas disponíveis no repositório de pacotes:

`tlmgr platform list`

- Adiciona os executáveis de uma plataforma específica:

`sudo tlmgr platform add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>

- Remove os executáveis de uma plataforma específica:

`sudo tlmgr platform remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>

- Detecta automaticamente e troca para a plataforma atual:

`sudo tlmgr platform set auto`

- Troca para uma plataforma específica:

`sudo tlmgr platform set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>
