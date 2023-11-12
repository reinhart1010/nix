---
layout: page
title: linux/zypper (italiano)
description: "Sistema di Gestione dei Pacchetti di SUSE e openSUSE."
content_hash: a40f7e4887ffbcef1d556a3ab9ede287a1180a35
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

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
