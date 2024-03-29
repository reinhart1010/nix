---
layout: page
title: common/ppmtosixel (English)
description: "Convert a PPM image to DEC sixel format."
content_hash: 3661b0e9dd5947d50a1971c743e7674f348052bc
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmtosixel

Convert a PPM image to DEC sixel format.
More information: <https://netpbm.sourceforge.net/doc/ppmtosixel.html>.

- Convert a PPM image to DEC sixel format:

`ppmtosixel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sixel</span>

- Produce an uncompressed SIXEL file that is much slower to print:

`ppmtosixel -raw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sixel</span>

- Add a left margin of 1.5 inches:

`ppmtosixel -margin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sixel</span>

- Encode control codes in a more portable (although less space-efficient) way:

`ppmtosixel -7bit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sixel</span>
