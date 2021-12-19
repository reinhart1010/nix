---
layout: page
title: common/deluge (English)
description: "A command-line BitTorrent client."
content_hash: 781db6ca10a8ac506c046b1df4ce9670ef6f87a4
related_topics:
  - title: français version
    url: /fr/common/deluge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/deluge.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/deluge.html
    icon: bi bi-globe
---
# deluge

A command-line BitTorrent client.
More information: <https://deluge-torrent.org>.

- Download a torrent:

`deluge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Download a torrent using a specific configuration file:

`deluge -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Download a torrent and launch the specified user interface:

`deluge -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gtk|web|console</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Download a torrent and output the log to a file:

`deluge -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>
