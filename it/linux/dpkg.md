---
layout: page
title: linux/dpkg (italiano)
description: "Gestore di pacchetti Debian."
content_hash: 2971cfba16c6599d96e95207416971abd8e08537
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
---
# dpkg

Gestore di pacchetti Debian.
Alcuni comandi aggiuntivi, come `dpkg deb`, hanno la propria documentazione.
Maggiori informazioni: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

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
