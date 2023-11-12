---
layout: page
title: common/bioradtopgm (English)
description: "Convert a Biorad confocal file into a PGM file."
content_hash: cf4f4ae932f86a257cd9af53acdff78baa39821e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# bioradtopgm

Convert a Biorad confocal file into a PGM file.
More information: <https://netpbm.sourceforge.net/doc/bioradtopgm.html>.

- Read a Biorad confocal file and store the n'th image contained in it to as a PGM file:

`bioradtopgm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pic</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pgm</span>

- Read a Biorad confocal file and print the number of images it contains:

`bioradtopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pic</span>

- Display version:

`bioradtopgm -version`
