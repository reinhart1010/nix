---
layout: page
title: linux/nm-online (español)
description: "Pregunte a NetworkManager si la red está conectada."
content_hash: 9ef782fa2d3c3173e5865caa9b80df31d71525d5
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/nm-online.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nm-online.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nm-online.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nm-online

Pregunte a NetworkManager si la red está conectada.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nm-online.html>.

- Averigua si la red está conectada e imprime el resultado en `stdout`:

`nm-online`

- Espera durante `n` segundos por una conexión (30" por defecto):

`nm-online --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
