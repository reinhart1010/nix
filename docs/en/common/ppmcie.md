---
layout: page
title: common/ppmcie (English)
description: "Draw a CIE color chart as a PPM image."
content_hash: acc2c3c02fcca8be30e3aef67109cc06d6489f3f
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmcie

Draw a CIE color chart as a PPM image.
More information: <https://netpbm.sourceforge.net/doc/ppmcie.html>.

- Draw a CIE color chart using the REC709 color system as a PPM image:

`ppmcie > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Specify the color system to be used:

`ppmcie -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cie|ebu|hdtv|ntsc|smpte</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Specify the location of the individual illuminants:

`ppmcie -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red|green|blue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpos ypos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Do not dim the area outside the Maxwell triangle:

`ppmcie -full > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
