---
layout: page
title: common/optipng (English)
description: "PNG file optimization utility."
content_hash: aefb69f10ad358e9726b29858218afb9dd021d5c
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# optipng

PNG file optimization utility.
More information: <https://optipng.sourceforge.net>.

- Compress a PNG with default settings:

`optipng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a PNG with the best compression:

`optipng -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a PNG with the fastest compression:

`optipng -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a PNG and add interlacing:

`optipng -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a PNG and preserve all metadata (including file timestamps):

`optipng -preserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a PNG and remove all metadata:

`optipng -strip all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>
