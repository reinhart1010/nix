---
layout: page
title: common/ppmntsc (English)
description: "Make the RGB colors in a PPM image compatible with NTSC or PAL color systems."
content_hash: 5c21098728b9f9a8a3c8d3a3c418528f04fe197a
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmntsc

Make the RGB colors in a PPM image compatible with NTSC or PAL color systems.
More information: <https://netpbm.sourceforge.net/doc/ppmntsc.html>.

- Make the RGB colors in a PPM image compatible with NTSC color systems:

`ppmntsc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- Make the RGB colors in a PPM image compatible with PAL color systems:

`ppmntsc --pal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- Print the number of illegal pixels in the input image to `stderr`:

`ppmntsc --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>

- Output only legal/illegal/corrected pixels, set other pixels to black:

`ppmntsc --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legalonly|illegalonly|correctedonly</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
