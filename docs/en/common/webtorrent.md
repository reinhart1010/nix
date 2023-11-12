---
layout: page
title: common/webtorrent (English)
description: "The command-line interface for WebTorrent."
content_hash: 48aff62ab8ae8d70480576735fe5a9fdf1fcdd7f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# webtorrent

The command-line interface for WebTorrent.
Supports magnets, URLs, info hashes and `.torrent` files.
More information: <https://github.com/webtorrent/webtorrent-cli>.

- Download a torrent:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>`"`

- Stream a torrent to VLC media player:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>`" --vlc`

- Stream a torrent to a Digital Living Network Alliance (DLNA) device:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>`" --dlna`

- Display a list of files for a specific torrent:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>`" --select`

- Specify a file index from the torrent to download:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_id</span>`" --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index</span>

- Seed a specific file or directory:

`webtorrent seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Create a new torrent file for the specified file path:

`webtorrent create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display information for a magnet URI or `.torrent` file:

`webtorrent info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_magnet</span>
