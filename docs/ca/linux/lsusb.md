---
layout: page
title: linux/lsusb (català)
description: "Mostra informació sobre ports i dispositius USB."
content_hash: 3aa45d4bd03c39bd6a4ed4853a8d1b5295067dd9
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/linux/lsusb.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsusb.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsusb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/lsusb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsusb

Mostra informació sobre ports i dispositius USB.
Més informació: <https://manned.org/lsusb>.

- Llista tots els dispositius USB disponibles:

`lsusb`

- Llista la jerarquia de dispositius USB en forma d'arbre:

`lsusb -t`

- Llista tots els disposititus USB de forma verbosa:

`lsusb --verbose`

- Llista només dispositius amb un ID d'assemblador i producte determinat:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assemblador</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">producte</span>
