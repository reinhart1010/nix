---
layout: page
title: common/pamditherbw (English)
description: "Apply dithering to a greyscale image, i.e. turn it into a pattern of black and white pixels that look the same as the original greyscale."
content_hash: 49094778f774f2cf5f8d9c656650b6b2e3e62262
last_modified_at: 2024-02-12
tldri18n_status: 2
---
# pamditherbw

Apply dithering to a greyscale image, i.e. turn it into a pattern of black and white pixels that look the same as the original greyscale.
See also: `pbmreduce`.
More information: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Read a PGM image, apply dithering and save it to a file:

`ppmditherbw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pgm</span>

- Use the specified quantization method:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">floyd|fs|atkinson|threshold|hilbert|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pgm</span>

- Use the atkinson quantization method and the specified seed for a pseudo-random number generator:

`ppmditherbw -atkinson -randomseed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1337</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pgm</span>

- Specify the thresholding value for quantization methods that perform some sort of thresholding:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fs|atkinson|thresholding</span>` -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pgm</span>
