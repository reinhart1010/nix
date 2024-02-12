---
layout: page
title: common/pbmtoppa (English)
description: "Convert a PBM image to HP Printer Performance Architecture format."
content_hash: 001e00b4a688045ea664ef8ab68eb4a04c2d3b6d
last_modified_at: 2024-02-12
tldri18n_status: 2
---
# pbmtoppa

Convert a PBM image to HP Printer Performance Architecture format.
More information: <https://netpbm.sourceforge.net/doc/pbmtoppa.html>.

- Convert a PBM image into a PPA file:

`pbmtoppa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppa</span>

- Specify the desired dots-per-inch and paper size:

`pbmtoppa -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppa</span>
