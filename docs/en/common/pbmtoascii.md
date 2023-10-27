---
layout: page
title: common/pbmtoascii (English)
description: "Convert a PBM image to ASCII graphics."
content_hash: 4e02c8f3c881a818a602d02745caa648cd4eca06
last_modified_at: 2023-10-27
---
# pbmtoascii

Convert a PBM image to ASCII graphics.
More information: <https://netpbm.sourceforge.net/doc/pbmtoascii.html>.

- Read a PBM file as input and produce an ASCII output:

`pbmtoascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>

- Read a PBM file as input and save an ASCII output into a file:

`pbmtoascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Read a PBM file as input while setting the pixel mapping (defaults to 1x2):

`pbmtoascii -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1x2|2x4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>

- Display version:

`pbmtoascii -version`
