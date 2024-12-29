---
layout: page
title: common/spottopgm (English)
description: "Convert a SPOT satellite image to PGM format."
content_hash: c021e9b9c0c8b785f919e38336617732ea53e49f
last_modified_at: 2024-12-29
tldri18n_status: 2
---
# spottopgm

Convert a SPOT satellite image to PGM format.
More information: <https://netpbm.sourceforge.net/doc/spottopgm.html>.

- Convert the specified SPOT image to PGM format:

`spottopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.spot</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Extract the specified color channel:

`spottopgm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.spot</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Extract the specified rectangle from the input image:

`spottopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_col first_row last_col last_row</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.spot</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>
