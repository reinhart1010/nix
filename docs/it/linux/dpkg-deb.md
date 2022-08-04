---
layout: page
title: linux/dpkg-deb (italiano)
description: "Impacchetta, spacchetta e fornisce informazioni su archivi Debian."
content_hash: 1f576f265a5c9e24d645e1d12bd1783f858f92d4
related_topics:
  - title: English version
    url: /en/linux/dpkg-deb.html
    icon: bi bi-globe
---
# dpkg-deb

Impacchetta, spacchetta e fornisce informazioni su archivi Debian.
Maggiori informazioni: <https://manpages.debian.org/latest/dpkg/dpkg-deb.html>.

- Mostra le informazioni riguardo ad un pacchetto:

`dpkg-deb --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.deb</span>

- Mostra il nome e la versione del pacchetto in una singola riga:

`dpkg-deb --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.deb</span>

- Elenca i contenuti del pacchetto:

`dpkg-deb --contents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.deb</span>

- Estrae i contenuti del pacchetto in una cartella:

`dpkg-deb --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella</span>

- Crea una pacchetto a partire da una cartella specificata:

`dpkg-deb --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella</span>
