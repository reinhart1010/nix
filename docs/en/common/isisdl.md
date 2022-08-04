---
layout: page
title: common/isisdl (English)
description: "A downloading utility for ISIS of TU-Berlin. Download all your files and videos from ISIS."
content_hash: e45dc17812ec6b1817e5b36af204b7ff3204f972
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># isisdl

A downloading utility for ISIS of TU-Berlin. Download all your files and videos from ISIS.
More information: <https://github.com/Emily3403/isisdl>.

- Start the synchronization process:

`isisdl`

- Limit the download rate to 20 MiB/s and download with 5 threads:

`isisdl --download-rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` --max-num-threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Run the initialization configuration wizard:

`isisdl --init`

- Run the additional configuration wizard:

`isisdl --config`

- Initiate a full synchronization of the database and compute the checksum of every file:

`isisdl --sync`

- Start ffmpeg to compress downloaded videos:

`isisdl --compress`
