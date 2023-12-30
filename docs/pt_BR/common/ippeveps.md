---
layout: page
title: common/ippeveps (português (Brasil))
description: "Imprime em impressoras Adobe PostScript."
content_hash: 3f087c6261069213b503b87ea887287e45e43c19
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/ippeveps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ippeveps

Imprime em impressoras Adobe PostScript.
Suporta arquivos PDF, PostScript, JPEG, PWG Raster or Apple Raster.
Veja também: `ippevepcl`, `ippeveprinter`.
Mais informações: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Imprime um arquivo para `stdout` (mensagens de estado e progresso são enviadas para `stderr`):

`ippeveps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime um arquivo de `stdin` para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wget -O - https://examplewebsite.com/file</span>` | ippeveps`
