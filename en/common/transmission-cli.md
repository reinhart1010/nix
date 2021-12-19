---
layout: page
title: common/transmission-cli (English)
description: "A lightweight, command-line BitTorrent client."
content_hash: 3b0d89e7c7a705e1181b7d3074592a8a99f15812
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

- Set the download speed limit to 50 KB/s:

`transmission-cli --downlimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Set the upload speed limit to 50 KB/s:

`transmission-cli --uplimit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Use a specific port for connections:

`transmission-cli --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Force encryption for peer connections:

`transmission-cli --encryption-required `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>

- Use a Bluetack-formatted peer blocklist:

`transmission-cli --blocklist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blocklist_url|path/to/blocklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|magnet|path/to/file</span>
