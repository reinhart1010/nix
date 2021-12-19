---
layout: page
title: common/deluge (italiano)
description: "Client BItTorrent da linea di comando."
content_hash: c4bf9a4ad7559827c341fcde614319135a05ced2
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
---
# deluge

Client BItTorrent da linea di comando.
Maggiori informazioni: <https://deluge-torrent.org>.

- Scarica un torrent:

`deluge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/a/file</span>

- Scarica un torrent utilizzando uno specifico file di configurazione:

`deluge -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_configurazione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/a/file</span>

- Scarica un torrent ed avvia una specifica interfaccia utente:

`deluge -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gtk|web|console</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/a/file</span>

- Scarica un torrent e scrivi il log in un file:

`deluge -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|percorso/a/file</span>
