---
layout: page
title: common/pnmtofiasco (English)
description: "Convert a PNM image to a compressed FIASCO file."
content_hash: d8e45c427bff762e747991f0fec9b893f7af3e79
last_modified_at: 2023-12-18
tldri18n_status: 2
---
# pnmtofiasco

Convert a PNM image to a compressed FIASCO file.
More information: <https://netpbm.sourceforge.net/doc/pnmtofiasco.html>.

- Convert a PNM image to a compressed FIASCO file:

`pnmtofiasco `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>

- Specify the [i]nput files through a pattern:

`pnmtofiasco --image-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">img[01-09+1].pnm</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>

- Specify the compression quality:

`pnmtofiasco --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quality_level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>

- Load the options to be used from the specified configuration file:

`pnmtofiasco --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fiascorc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fiasco</span>
