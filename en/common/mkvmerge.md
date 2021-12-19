---
layout: page
title: common/mkvmerge (English)
description: "Merge and extract multimedia streams."
content_hash: f69105ce2e65bcbb5355208f4a1dcb7d63137a69
---
# mkvmerge

Merge and extract multimedia streams.
More information: <https://mkvtoolnix.download/doc/mkvmerge.html>.

- Display information about a Matroska file:

`mkvmerge --identify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mkv</span>

- Extract the audio from track 1 of a specific file:

`mkvextract tracks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mkv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.webm</span>

- Extract the subtitle from track 3 of a specific file:

`mkvextract tracks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mkv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/subs.srt</span>
