---
layout: page
title: linux/lsusb (italiano)
description: "Visualizza le informazioni su i bus USB e i dispositivi a loro connessi."
content_hash: ea206c75f7aed2afa07cfe71d3698c2640aa5125
last_modified_at: 2024-03-14
related_topics:
  - title: català version
    url: /ca/linux/lsusb.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/lsusb.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsusb.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsusb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsusb

Visualizza le informazioni su i bus USB e i dispositivi a loro connessi.
Maggiori informazioni: <https://manned.org/lsusb>.

- Elenca tutti i dispositivi USB disponibili:

`lsusb`

- Visualizza la gerarchia USB come un albero:

`lsusb -t`

- Elenca informazioni prolisse riguardo ai dispositivi USB:

`lsusb --verbose`

- Elenca solamente i dispositivi con un certo id fornitore e ID prodotto:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fornitore</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prodotto</span>
