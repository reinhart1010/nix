---
layout: page
title: linux/libuser-lid (español)
description: "Muestra los grupos de un usuario o los usuarios de un grupo."
content_hash: 00e7e15c99574cb0208bf0afcafcd422a786d5a3
last_modified_at: 2024-01-15
related_topics:
  - title: English version
    url: /en/linux/libuser-lid.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/libuser-lid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libuser-lid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libuser-lid

Muestra los grupos de un usuario o los usuarios de un grupo.
En Fedora y Arch Linux, este programa se instala como `lid`.
Más información: <https://manned.org/lid.8>.

- Lista los grupos primarios y secundarios de un usuario específico:

`sudo lid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Lista los usuarios de un grupo específico:

`sudo lid --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
