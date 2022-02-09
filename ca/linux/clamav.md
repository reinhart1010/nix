---
layout: page
title: linux/clamav (català)
description: "Antivirus de codi obert."
content_hash: 6bd8cf55e4dda91509c8b8ef59a8f96718bc9f06
related_topics:
  - title: English version
    url: /en/linux/clamav.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/clamav.html
    icon: bi bi-globe
---
# clamav

Antivirus de codi obert.
Dissenyat especialment per escanejar correus electrònics, però pot ser emprat en altres contextos.
Més informació: <https://www.clamav.net>.

- Actualitza definicions de virus:

`freshclam`

- Escaneja un arxiu en busca de virus:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/arxiu</span>

- Escaneja directoris recursivament i mostra els arxius infectats:

`clamscan --recursive --infected `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directori</span>

- Escaneja directoris recursivament y posa els arxius infectats en quarantena:

`clamscan --recursive --move=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directori</span>
