---
layout: page
title: common/cwebp (English)
description: "Compress an image file to a WebP file."
content_hash: 53366721ff200c6f6e72d59041ff335de4bc541d
last_modified_at: 2023-11-12
related_topics:
  - title: русский version
    url: /ru/common/cwebp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cwebp

Compress an image file to a WebP file.
More information: <https://developers.google.com/speed/webp/docs/cwebp>.

- Compress a WebP file with default settings (q = 75) to the [o]utput file:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.webp</span>

- Compress a WebP file with the best [q]uality and largest file size:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.webp</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Compress a WebP file with the worst [q]uality and smallest file size:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.webp</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- Compress a WebP file and apply resize to image:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.webp</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>

- Compress a WebP file and drop alpha channel information:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.webp</span>` -noalpha`
