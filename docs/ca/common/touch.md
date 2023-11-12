---
layout: page
title: common/touch (català)
description: "Canvia els temps d'accés i modificació d'un fitxer (atime, ntime)."
content_hash: 8f4c68cdd4cd7b9cb520b518219b55e849467e5e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># touch

Canvia els temps d'accés i modificació d'un fitxer (atime, ntime).
Més informació: <https://manned.org/man/freebsd-13.1/touch>.

- Crea un o múltiples fitxers o canvia els temps al temps actual:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camí/al/fitxer</span>

- Estableix el temps d'un fitxer a una data i hora específica:

`touch -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camí/al/fitxer</span>

- Estableix el temps en un fitxer a fa una hora:

`touch -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1 hour</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camí/al/fitxer</span>

- Fa servir el temps d'un fitxer per establir el temps d'un segons fitxer:

`touch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camí/al/fitxer1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camí/al/fitxer2</span>

- Crea múltiples fitxers:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camí/al/fitxer{1,2,3}.txt</span>
