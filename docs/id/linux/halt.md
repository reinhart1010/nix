---
layout: page
title: linux/halt (Indonesia)
description: "Hentikan seluruh proses dan jalannya CPU dalam sistem komputer."
content_hash: 15f4755ba2431d9b798995eee85d6d955a5b70c6
last_modified_at: 2023-12-15
related_topics:
  - title: català version
    url: /ca/linux/halt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/halt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/halt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/halt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# halt

Hentikan seluruh proses dan jalannya CPU dalam sistem komputer.
Informasi lebih lanjut: <https://manned.org/halt.8>.

- Hentikan sistem komputer:

`halt`

- Matikan sistem (sama seperti `poweroff`):

`halt --poweroff`

- Nyalakan ulang sistem (sama seperti `reboot`):

`halt --reboot`

- Hentikan sistem secara segera tanpa menghubungi manajer sistem:

`halt --force`

- Tulis entri wtmp shutdown tanpa menghentikan sistem:

`halt --wtmp-only`
