---
layout: page
title: common/transmission-cli (Nederlands)
description: "Een lichtgewicht, command-line BitTorrent client."
content_hash: 50738fc03fd6c63b619492e5166c39b5e14473cd
last_modified_at: 2023-12-03
related_topics:
  - title: English version
    url: /en/common/transmission-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-cli

Een lichtgewicht, command-line BitTorrent client.
Deze tool is verouderd, bekijk `transmission-remote`.
Meer informatie: <https://transmissionbt.com>.

- Download een specifieke torrent:

`transmission-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>

- Download een torrent naar een specifieke map:

`transmission-cli --download-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/download_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>

- Maak een torrent bestand van een specifiek bestand of map:

`transmission-cli --new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron_bestand_of_map</span>

- Zet de download snelheid limiet naar 50 KB/s:

`transmission-cli --downlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>

- Zet de upload snelheid limiet naar 50 KB/s:

`transmission-cli --uplimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>

- Gebruik een specifieke poort voor verbindingen:

`transmission-cli --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort_nummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>

- Forceer versleuteling voor alle peer-verbindingen:

`transmission-cli --encryption-required `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>

- Gebruik een Bluetack-geformatteerde peer blocklist:

`transmission-cli --blocklist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blocklist_url|pad/naar/blocklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|pad/naar/bestand</span>
