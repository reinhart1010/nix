---
layout: page
title: linux/eu-readelf (English)
description: "Displays information about ELF files."
content_hash: bb8a493ac8c6053cbee35e423351e01cd5d34ee5
last_modified_at: 2024-04-11
tldri18n_status: 2
---
# eu-readelf

Displays information about ELF files.
More information: <https://manned.org/eu-readelf>.

- Display all extractable information contained in the ELF file:

`eu-readelf --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the contents of all NOTE segments/sections, or of a particular segment/section:

`eu-readelf --notes[=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.note.ABI-tag</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
