---
layout: page
title: common/pngquant (English)
description: "PNG converter and lossy image compressor."
content_hash: a9cd7c6a18f40d6c2e545179dceb95006f408dcf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pngquant

PNG converter and lossy image compressor.
More information: <https://pngquant.org/>.

- Compress a specific PNG as much as possible and write result to a new file:

`pngquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a specific PNG and override original:

`pngquant --ext .png --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Try to compress a specific PNG with custom quality (skip if below the min value):

`pngquant --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a specific PNG with the number of colors reduced to 64:

`pngquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a specific PNG and skip if the file is larger than the original:

`pngquant --skip-if-larger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a specific PNG and remove metadata:

`pngquant --strip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a specific PNG and save it to the given path:

`pngquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a specific PNG and show progress:

`pngquant --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>
