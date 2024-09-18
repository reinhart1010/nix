---
layout: page
title: linux/dpkg-deb (italiano)
description: "Impacchetta, spacchetta e fornisce informazioni su archivi Debian."
content_hash: d8447e1248abc04b0f79db7369ce8880ddf3648b
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/dpkg-deb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-deb

Impacchetta, spacchetta e fornisce informazioni su archivi Debian.
Maggiori informazioni: <https://manned.org/dpkg-deb>.

- Mostra le informazioni riguardo ad un pacchetto:

`dpkg-deb --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.deb</span>

- Mostra il nome e la versione del pacchetto in una singola riga:

`dpkg-deb --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.deb</span>

- Elenca i contenuti del pacchetto:

`dpkg-deb --contents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.deb</span>

- Estrae i contenuti del pacchetto in una directory:

`dpkg-deb --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Crea una pacchetto a partire da una directory specificata:

`dpkg-deb --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>
