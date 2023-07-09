---
layout: page
title: common/cavif (English)
description: "PNG/JPEG to AVIF converter."
content_hash: d5b06888ee38845e06f8f7f6660434c6b0651df7
last_modified_at: 2023-07-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cavif

PNG/JPEG to AVIF converter.
More information: <https://github.com/kornelski/cavif-rs>.

- Convert a JPEG file to AVIF:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>

- Adjust the image quality (1-100) and convert a PNG file to AVIF:

`cavif --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Set the output location explicitly:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.avif</span>

- Overwrite the destination file if it already exists:

`cavif --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>
