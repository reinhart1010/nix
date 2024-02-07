---
layout: page
title: common/pnmalias (English)
description: "Apply antialiasing onto a PNM image."
content_hash: 110e2c55b4f5f39a46daab43342b584d3b615b02
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pnmalias

Apply antialiasing onto a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmalias.html>.

- Perform antialiasing on a PNM image, taking black pixels as background and white pixels as foreground:

`pnmalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Explicitly specify the background and foreground color:

`pnmalias -bcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">background_color</span>` -fcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foreground_color</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Apply altialiasing to foreground pixels only:

`pnmalias -fonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Apply antialiasing to all surrounding pixels of background pixels:

`pnmalias -balias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
