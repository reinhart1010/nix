---
layout: page
title: linux/apt-cache (italiano)
description: "Strumenti di Debian e Ubuntu per richiedere informazioni sui pacchetti."
content_hash: aa72e6e28cc9fd314505c66adb160dc87d7afc22
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/apt-cache.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-cache.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-cache.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-cache.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-cache.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-cache.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-cache.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-cache.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-cache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-cache

Strumenti di Debian e Ubuntu per richiedere informazioni sui pacchetti.
Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Cerca un pacchetto nelle sorgenti attuali:

`apt-cache search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Mostra informazioni su un pacchetto:

`apt-cache show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Mostra se un pacchetto è installato ed aggiornato:

`apt-cache policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Mostra le dipendenze di un pacchetto:

`apt-cache depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Mostra i pacchetti che dipendono da un particolare pacchetto:

`apt-cache rdepends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>
