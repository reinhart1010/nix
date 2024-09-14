---
layout: page
title: linux/reboot (Nederlands)
description: "Herstart het systeem."
content_hash: c45528c240cd0220364fa7642b45c4821a34b43e
last_modified_at: 2024-09-14
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
  - title: português (Brasil) version
    url: /pt_BR/linux/reboot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/reboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reboot

Herstart het systeem.
Meer informatie: <https://manned.org/reboot.8>.

- Herstart het systeem:

`reboot`

- Schakel het systeem uit (zelfde als `poweroff`):

`reboot --poweroff`

- Houd het systeem (beëindigt alle processen en zet de CPU uit) (zelfde als `halt`):

`reboot --halt`

- Herstart onmiddellijk zonder contact op te nemen met de systeembeheerder:

`reboot --force`

- Schrijf de wtmp shutdown entry zonder het systeem opnieuw te starten:

`reboot --wtmp-only`
