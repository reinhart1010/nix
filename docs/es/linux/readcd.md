---
layout: page
title: linux/readcd (español)
description: "Lee o escribe datos sobre un soporte Compact Disc."
content_hash: 1a9e1d4b111288298a2411248624a5ce3aed8f6d
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/readcd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/readcd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># readcd

Lee o escribe datos sobre un soporte Compact Disc.
Más información: <https://manned.org/readcd>.

- Leer un cd y lo copia a un archivo:

`readcd dev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/srX</span>` f=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.iso</span>
