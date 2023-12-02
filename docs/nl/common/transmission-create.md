---
layout: page
title: common/transmission-create (Nederlands)
description: "Maak BitTorrent `.torrent` bestanden."
content_hash: a26751852d2103ef001f095d8f3bbd9ef5977451
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/common/transmission-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-create

Maak BitTorrent `.torrent` bestanden.
Bekijk ook: `transmission`.
Meer informatie: <https://manned.org/transmission-create>.

- Maak een torrent met een stukgrootte van 2048 KB:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/voorbeeld.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aankondigings-url_van_tracker</span>` --piecesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Maak een privé torrent met een stukgrootte van 2048 KB:

`transmission-create -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/voorbeeld.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aankondigings-url_van_tracker</span>` --piecesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Maak een torrent met een opmerking:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/voorbeeld.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracker_url1</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opmerking</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Maak een torrent met meerdere trackers:

`transmission-create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/voorbeeld.torrent</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracker_url1</span>` --tracker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracker_url2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Toon de help-pagina:

`transmission-create --help`
