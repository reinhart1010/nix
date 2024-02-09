---
layout: page
title: common/ppmtomitsu (English)
description: "Convert a PPM image to a Mitsubishi S340-10 file."
content_hash: a1083994b020734b595be89cc4323670a805ea5d
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# ppmtomitsu

Convert a PPM image to a Mitsubishi S340-10 file.
More information: <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>.

- Convert a PPM image to a MITSU file:

`ppmtomitsu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mitsu</span>

- Enlarge the image by the specified factor, use the specified sharpness and produce `n` copies:

`ppmtomitsu -enlarge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` -sharpness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|4</span>` -copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mitsu</span>

- Use the given medium for the printing process:

`ppmtomitsu -media `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|A4|AS|A4S</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mitsu</span>
