---
layout: page
title: common/transmission-show (English)
description: "Get information about a torrent file."
content_hash: 8e7f39fefd0e1326b017b9517ddac844eb1d28a3
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># transmission-show

Get information about a torrent file.
See also: `transmission`.
More information: <https://manned.org/transmission-show>.

- Display metadata for a specific torrent:

`transmission-show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.torrent</span>

- Generate a magnet link for a specific torrent:

`transmission-show --magnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.torrent</span>

- Query a torrent's trackers and print the current number of peers:

`transmission-show --scrape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.torrent</span>
