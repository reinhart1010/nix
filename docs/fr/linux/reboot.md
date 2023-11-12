---
layout: page
title: linux/reboot (français)
description: "Redémarre le système."
content_hash: 36ecb43815b95bc00f143a610162fe441bb3e872
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/reboot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/reboot.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/reboot.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/reboot.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/reboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reboot

Redémarre le système.
Plus d'informations : <https://manned.org/reboot.8>.

- Redémarre le système :

`reboot`

- Éteint le système (identique à `poweroff`) :

`reboot --poweroff`

- Arrête (met fin à tous les processus et arrête le processeur) le système (identique à `halt`) :

`reboot --halt`

- Redémarre immédiatement sans contacter le gestionnaire du système :

`reboot --force`

- Écrit l'entrée wtmp shutdown sans redémarrer le système :

`reboot --wtmp-only`
