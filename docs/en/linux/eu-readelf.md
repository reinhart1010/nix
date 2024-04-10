---
layout: page
title: linux/eu-readelf (English)
description: "Displays information about ELF files."
content_hash: bb8a493ac8c6053cbee35e423351e01cd5d34ee5
last_modified_at: 2024-04-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eu-readelf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eu-readelf

Displays information about ELF files.
More information: <https://manned.org/eu-readelf>.

- Display all extractable information contained in the ELF file:

`eu-readelf --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the contents of all NOTE segments/sections, or of a particular segment/section:

`eu-readelf --notes[=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.note.ABI-tag</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
