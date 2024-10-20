---
layout: page
title: common/oxipng (English)
description: "Losslessly improve compression of PNG files."
content_hash: 2e688eebb9975d481fd88d06e90dfa038c4b12af
last_modified_at: 2024-10-20
tldri18n_status: 2
---
# oxipng

Losslessly improve compression of PNG files.
More information: <https://github.com/shssoichiro/oxipng>.

- Compress a PNG file (overwrites the file by default):

`oxipng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress a PNG file and save the output to a new file:

`oxipng --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Compress all PNG files in the current directory using multiple threads:

`oxipng "*.png"`

- Compress a file with a set optimization level (default is 2):

`oxipng --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3|4|5|6|max</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Set the PNG interlacing type (`0` removes interlacing, `1` applies Adam7 interlacing, `keep` preserves existing interlacing; default is `0`):

`oxipng --interlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|keep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Perform additional optimization on images with an alpha channel:

`oxipng --alpha `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Use the much slower but stronger Zopfli compressor with max optimization:

`oxipng --zopfli --opt max `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Strip all non-critical metadata chunks:

`oxipng --strip all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>
