---
layout: page
title: common/transmission-remote (Nederlands)
description: "Externe besturingshulpprogramma voor `transmission-daemon` en `transmission`."
content_hash: b722e4a585351c16a9ede92cc02767e92129dda4
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/common/transmission-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-remote

Externe besturingshulpprogramma voor `transmission-daemon` en `transmission`.
Meer informatie: <https://transmissionbt.com>.

- Voeg een torrentbestand of magnet-link toe aan Transmission en download naar een opgegeven map:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent|url</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/download_map</span>

- Verander de standaard downloadmap:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/download_map</span>

- Toon alle torrents:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --list`

- Start torrent 1 en 2, stop torrent 3:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2</span>`" --start -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --stop`

- Verwijder torrent 1 en 2 en verwijder ook alle lokale gegevens voor torrent 2:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --remove -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --remove-and-delete`

- Stop alle torrents:

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` --stop`

- Verplaats torrents 1-10 en 15-20 naar een nieuwe map (die wordt aangemaakt als deze nog niet bestaat):

`transmission-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10,15-20</span>`" --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/nieuwe_map</span>
