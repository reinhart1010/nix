---
layout: page
title: common/fiascotopnm (English)
description: "Convert a compressed FIASCO file to a PNM image."
content_hash: 12491e82d4c5067ac3c4d6d7c6538eab1d4c8b2b
last_modified_at: 2023-12-18
tldri18n_status: 2
---
# fiascotopnm

Convert a compressed FIASCO file to a PNM image.
More information: <https://netpbm.sourceforge.net/doc/fiascotopnm.html>.

- Convert a compressed FIASCO file to a PNM file or in the case of video streams multiple PNM files:

`fiascotopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_basename</span>

- Use fast decompression, resulting in a slightly decreased quality of the output file(s):

`fiascotopnm --fast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_basename</span>

- Load the options to be used from the specified configuration file:

`fiascotopnm --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fiascorc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_basename</span>

- Magnify the decompressed image(s) by a factor of 2^n:

`fiascotopnm --magnify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_basename</span>

- Smooth the decompressed image by the specified amount:

`fiascotopnm --smooth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file_basename</span>
