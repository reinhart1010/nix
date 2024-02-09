---
layout: page
title: common/transmission-cli (English)
description: "A lightweight, command-line BitTorrent client."
content_hash: a436f2a98102d77fef250ed3dfa12a2d139c1548
last_modified_at: 2024-02-09
related_topics:
  - title: Nederlands version
    url: /nl/common/transmission-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-cli

A lightweight, command-line BitTorrent client.
This tool has been deprecated, please see `transmission-remote`.
More information: <https://transmissionbt.com>.

- Download a specific torrent:

`transmission-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Download a torrent to a specific directory:

`transmission-cli --download-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/download_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Create a torrent file from a specific file or directory:

`transmission-cli --new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file_or_directory</span>

- Specify the download speed limit (in KB/s):

`transmission-cli --downlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Specify the upload speed limit (in KB/s):

`transmission-cli --uplimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Use a specific port for connections:

`transmission-cli --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Force encryption for peer connections:

`transmission-cli --encryption-required `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Use a Bluetack-formatted peer blocklist:

`transmission-cli --blocklist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blocklist_url|path/to/blocklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>
