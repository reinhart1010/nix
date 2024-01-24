---
layout: page
title: common/inkmake (English)
description: "GNU Makefile-style SVG exporting using Inkscape's backend."
content_hash: 6f25a83f7a2a5597617cb50cfac589b478cf0e6e
last_modified_at: 2024-01-24
tldri18n_status: 2
---
# inkmake

GNU Makefile-style SVG exporting using Inkscape's backend.
More information: <https://github.com/wader/inkmake>.

- Export an SVG file executing the specified Inkfile:

`inkmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Inkfile</span>

- Execute an Inkfile and show detailed information:

`inkmake --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Inkfile</span>

- Execute an Inkfile, specifying SVG input file(s) and an output file:

`inkmake --svg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.svg</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Inkfile</span>

- Use a custom Inkscape binary as the backend:

`inkmake --inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Applications/Inkscape.app/Contents/Resources/bin/inkscape</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Inkfile</span>

- Display help:

`inkmake --help`
