---
layout: page
title: common/caller (español)
description: "Imprime el contexto de la función."
content_hash: bee7e016b9328f9f10ff1bb3f5ed5e2cf4a4d5d3
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/common/caller.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/caller.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># caller

Imprime el contexto de la función.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-caller>.

- Imprime la línea y el nombre de archivo desde donde se invocó a la función actual:

`caller`

- Imprime la línea, la función y el nombre de archivo desde donde se invocó a la función actual:

`caller 0`

- Imprime la línea, el nombre de la función y el nombre del archivo de una llamada a una función `n`:

`caller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
