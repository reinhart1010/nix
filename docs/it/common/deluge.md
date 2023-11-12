---
layout: page
title: common/deluge (italiano)
description: "Client BItTorrent da linea di comando."
content_hash: 553efaa388907cbea0a6388838a755fac608e0ec
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/deluge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/deluge.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/deluge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deluge

Client BItTorrent da linea di comando.
Maggiori informazioni: <https://deluge-torrent.org>.

- Scarica un torrent:

`deluge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/del/file</span>

- Scarica un torrent utilizzando uno specifico file di configurazione:

`deluge -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_configurazione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/del/file</span>

- Scarica un torrent ed avvia una specifica interfaccia utente:

`deluge -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gtk|web|console</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/del/file</span>

- Scarica un torrent e scrivi il log in un file:

`deluge -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/del/file</span>
