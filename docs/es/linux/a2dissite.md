---
layout: page
title: linux/a2dissite (español)
description: "Deshabilita un servidor virtual Apache en sistemas operativos basados en Debian."
content_hash: c167f1abe5bf31346450e31a31c03b73557be143
last_modified_at: 2023-03-21
related_topics:
  - title: català version
    url: /ca/linux/a2dissite.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2dissite.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2dissite.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2dissite.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2dissite.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2dissite.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2dissite.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2dissite.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2dissite.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># a2dissite

Deshabilita un servidor virtual Apache en sistemas operativos basados en Debian.
Más información: <https://manpages.debian.org/latest/apache2/a2dissite.8.en.html>.

- Deshabilita un host virtual:

`sudo a2dissite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_virtual</span>

- No muestra mensajes informativos:

`sudo a2dissite --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_virtual</span>
