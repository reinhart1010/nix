---
layout: page
title: linux/cdrdao (español)
description: "Lee y graba CDs en modo disc-at-once."
content_hash: 30be603d165b6d3561d30d358fedeac1134e9e6c
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/cdrdao.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cdrdao.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cdrdao

Lee y graba CDs en modo disc-at-once.
Más información: <https://manned.org/man/cdrdao>.

- Lee un CD y escribe su contenido en un archivo:

`cdrdao read-cd --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` --read-raw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen.toc</span>
