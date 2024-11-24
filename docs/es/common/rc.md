---
layout: page
title: common/rc (español)
description: "Una escucha de puerto moderna simplificada y con interfaz de comando reversa."
content_hash: c296ebdf4d6f73eb35515dc56c1ba74158e5ebae
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/rc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/rc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rc

Una escucha de puerto moderna simplificada y con interfaz de comando reversa.
Similar a `nc`.
Más información: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Comienza a escuchar en un puerto específico:

`rc -lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Comienza una interfaz de comando inversa:

`rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>
