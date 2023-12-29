---
layout: page
title: common/ippeveps (português (Brasil))
description: "Imprime em impressoras Adobe PostScript."
content_hash: 3f087c6261069213b503b87ea887287e45e43c19
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/ippeveps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ippeveps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ippeveps

Imprime em impressoras Adobe PostScript.
Suporta arquivos PDF, PostScript, JPEG, PWG Raster or Apple Raster.
Veja também: `ippevepcl`, `ippeveprinter`.
Mais informações: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Imprime um arquivo para `stdout` (mensagens de estado e progresso são enviadas para `stderr`):

`ippeveps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime um arquivo de `stdin` para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wget -O - https://examplewebsite.com/file</span>` | ippeveps`
