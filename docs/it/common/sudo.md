---
layout: page
title: common/sudo (italiano)
description: "Esegue un singolo comando come superuser o come un altro utente."
content_hash: 3ae2cec505c04dd607d7d0d465d2b0fae870e3a2
last_modified_at: 2024-03-10
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/sudo.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sudo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sudo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sudo

Esegue un singolo comando come superuser o come un altro utente.
Maggiori informazioni: <https://www.sudo.ws/sudo.html>.

- Esegui un comando come superuser:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Modifica un file come superuser con il tuo editor di default:

`sudo -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Esegui un comando come un altro utente e/o gruppo:

`sudo -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- Ripeti l'ultimo comando prefissandolo con "sudo" (funziona solo in Bash, Zsh, ecc):

`sudo !!`

- Fai partire la shell di default con i privilegi da superuser:

`sudo -i`
