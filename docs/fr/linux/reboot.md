---
layout: page
title: linux/reboot (français)
description: "Réinitialisez le système."
content_hash: cc391060250e69e9999604e5a356e669018682e2
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
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/reboot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reboot

Réinitialisez le système.
Plus d'informations : <https://manned.org/reboot.8>.

- Réinitialisez le système normalement :

`reboot`

- Mettrez le système hors tension :

`reboot --poweroff`

- Arrêtez toutes les fonctions du CPU :

`reboot --halt`

- Réinitialisez le système maintenant mais propre :

`reboot --force`
