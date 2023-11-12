---
layout: page
title: linux/lsusb (italiano)
description: "Visualizza le informazioni su i bus USB e i dispositivi a loro connessi."
content_hash: cc1db0fa427bc379344456a487f8e8ac0bc93246
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# lsusb

Visualizza le informazioni su i bus USB e i dispositivi a loro connessi.
Maggiori informazioni: <https://manned.org/lsusb>.

- Elenca tutti i dispositivi USB disponibili:

`lsusb`

- Visualizza la gerarchia USB come un albero:

`lsusb -t`

- Elenca informazioni prolisse riguardo ai dispositivi USB:

`lsusb --verbose`

- Elenca informazioni dettagliate riguardo ad un dispositivo USB:

`lsusb -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo</span>

- Elenca solamente i dispositivi con un certo id fornitore e id prodotto:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fornitore</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prodotto</span>
