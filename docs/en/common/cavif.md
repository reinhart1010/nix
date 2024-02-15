---
layout: page
title: common/cavif (English)
description: "Convert PNG/JPEG images to AVIF. Written in Rust."
content_hash: 2155bc047cf235cd692fe5fa8ff497d1804da626
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# cavif

Convert PNG/JPEG images to AVIF. Written in Rust.
See also: `convert`.
More information: <https://github.com/kornelski/cavif-rs>.

- Convert a JPEG file to AVIF, saving it to `file.avif`:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>

- Adjust the image quality and convert a PNG file to AVIF:

`cavif --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Specify the output location:

`cavif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.avif</span>

- Overwrite the destination file if it already exists:

`cavif --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpg</span>
