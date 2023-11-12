---
layout: page
title: common/deluge-console (English)
description: "An interactive interface for the Deluge BitTorrent client."
content_hash: 9e78ff93fd25e6aab2e7689d9508cd6f1c91a965
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/deluge-console.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/deluge-console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deluge-console

An interactive interface for the Deluge BitTorrent client.
More information: <https://deluge-torrent.org>.

- Start the interactive console interface:

`deluge-console`

- Connect to a Deluge daemon instance:

`connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Add a torrent to the daemon:

`add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Display information about all torrents:

`info`

- Display information about a specific torrent:

`info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>

- Pause a torrent:

`pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>

- Resume a torrent:

`resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>

- Remove a torrent from the daemon:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>
