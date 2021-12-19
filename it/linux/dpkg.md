---
layout: page
title: linux/dpkg (italiano)
description: "Gestore di pacchetti Debian."
content_hash: 0fd4f9cf9297dfc6022752228e4e467793488cc4
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
---
# dpkg

Gestore di pacchetti Debian.
Alcuni comandi aggiuntivi, come `dpkg deb`, hanno la propria documentazione.
Maggiori informazioni: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>.

- Installa un pacchetto:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.deb</span>

- Rimuove un pacchetto:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>

- Elenca i pacchetti installati:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_per_la_ricerca</span>

- Elenca i contenuti di un pacchetto:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>

- Elenca i contenuti di un file pacchetto locale:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.deb</span>

- Trova a quale pacchetto appartiene un file:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
