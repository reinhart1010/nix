---
layout: page
title: common/cavif (English)
description: "PNG/JPEG to AVIF converter. Written in Rust."
content_hash: 83046c51f651e79a10b2b9243bbb65f6313459c1
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# cavif

PNG/JPEG to AVIF converter. Written in Rust.
See also: `convert`.
More information: <https://github.com/kornelski/cavif-rs>.

- Convert a JPEG file to AVIF, saving it to `file.avif`:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>

- Adjust the image quality (1-100) and convert a PNG file to AVIF:

`cavif --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Specify the output location:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.avif</span>

- Overwrite the destination file if it already exists:

`cavif --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jpg</span>
