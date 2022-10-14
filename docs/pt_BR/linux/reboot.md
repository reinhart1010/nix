---
layout: page
title: linux/reboot (português (Brasil))
description: "Reinicia o sistema."
content_hash: 8fc95f90d9ac2b4a5eeadff63236dd83343d2dcf
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
  - title: français version
    url: /fr/linux/reboot.html
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

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># reboot

Reinicia o sistema.
Mais informações: <https://manned.org/reboot.8>.

- Reinicia o sistema:

`reboot`

- Desliga o sistema (igual a `poweroff`):

`reboot --poweroff`

- Suspende o sistema (igual a `halt`):

`reboot --halt`

- Reinicia imediatamente sem entrar em contato com o gerente do sistema:

`reboot --force`

- Escreve a entrada wtmp shutdown sem reinicializar o sistema:

`reboot --wtmp-only`
