---
layout: page
title: common/sudo (italiano)
description: "Esegue un singolo comando come superuser o come un altro utente."
content_hash: c6640144ebef7a27adf41a18239d41fdfd765746
related_topics:
  - title: English version
    url: /en/common/sudo.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/sudo.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sudo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sudo

Esegue un singolo comando come superuser o come un altro utente.
Maggiori informazioni: <https://www.sudo.ws/sudo.html>.

- Esegui un comando come superuser:

`sudo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">less /var/log/syslog</span>

- Modifica un file come superuser con il tuo editor di default:

`sudo -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/fstab</span>

- Esegui un comando come un altro utente e/o gruppo:

`sudo -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id -a</span>

- Ripeti l'ultimo comando prefissandolo con "sudo" (funziona solo in bash, zsh, ecc):

`sudo !!`

- Fai partire la shell di default con i privilegi da superuser:

`sudo -i`
