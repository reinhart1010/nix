---
layout: page
title: linux/zypper (italiano)
description: "Sistema di Gestione dei Pacchetti di SUSE e openSUSE."
content_hash: a40f7e4887ffbcef1d556a3ab9ede287a1180a35
related_topics:
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zypper.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zypper

Sistema di Gestione dei Pacchetti di SUSE e openSUSE.
Maggiori informazioni: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincronizza il database dei pacchetti e delle versioni disponibili:

`zypper refresh`

- Installa un nuovo pacchetto:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Rimuovi un pacchetto:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Aggiorna i pacchetti installati alle ultime versioni disponibili:

`zypper update`

- Cerca usando nome o parola chiave:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|parole_chiave</span>
