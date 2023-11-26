---
layout: page
title: common/ppmtoilbm (English)
description: "Convert a PPM image to an ILBM file."
content_hash: 3f635b313a1f813b2e0cf7b9a370bcaa719dd5e5
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmtoilbm

Convert a PPM image to an ILBM file.
More information: <https://netpbm.sourceforge.net/doc/ppmtoilbm.html>.

- Convert a PPM image to an ILBM file:

`ppmtoilbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ilbm</span>

- Write a maximum of n planes to the ILBM file and produce a HAM/24bit/direct color file if this number is exceeded:

`ppmtoilbm -maxplanes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hamif|24if|dcif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ilbm</span>

- Produce a ILBM file with exactly n planes:

`ppmtoilbm -fixplanes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ilbm</span>

- Select the compression method to be used:

`ppmtoilbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compress|nocompress|savemem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ilbm</span>
