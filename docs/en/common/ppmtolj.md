---
layout: page
title: common/ppmtolj (English)
description: "Convert a PPM file to an HP LaserJet PCL 5 Color file."
content_hash: 5a3207573c65142694410f2585b84dea3840d25f
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# ppmtolj

Convert a PPM file to an HP LaserJet PCL 5 Color file.
More information: <https://netpbm.sourceforge.net/doc/ppmtolj.html>.

- Convert a PPM file to an HP LaserJet PCL 5 Color file:

`ppmtolj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.lj</span>

- Apply a gamma correction using the specified gamma value:

`ppmtolj -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gamma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.lj</span>

- Specify the required resolution:

`ppmtolj -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75|100|150|300|600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.lj</span>
