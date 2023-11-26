---
layout: page
title: common/pbmtolj (English)
description: "Convert a PBM file to an HP LaserJet file."
content_hash: 024c20bba3e062f2294f4f95bd9a623cb24f1dee
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pbmtolj

Convert a PBM file to an HP LaserJet file.
More information: <https://netpbm.sourceforge.net/doc/pbmtolj.html>.

- Convert a PBM file to an HP LaserJet file:

`pbmtolj `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.lj</span>

- Compress the output file using the specified method:

`pbmtolj -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">packbits|delta|compress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.lj</span>

- Specify the required resolution:

`pbmtolj -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75|100|150|300|600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.lj</span>
