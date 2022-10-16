---
layout: page
title: sunos/dmesg (français)
description: "Ecrire les messages du kernel sur la sortie standard."
content_hash: 6759f89436021274cec4163b616af6ae1d099442
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dmesg

Ecrire les messages du kernel sur la sortie standard.
Plus d'informations : <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Afficher les messages du kernel:

`dmesg`

- Afficher combien de mémoire physique est disponible sur ce système:

`dmesg | grep -i memory`

- Afficher les messages du kernel une page a la fois:

`dmesg | less`
