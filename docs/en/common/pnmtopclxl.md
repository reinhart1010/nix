---
layout: page
title: common/pnmtopclxl (English)
description: "Convert a PNM file to an HP LaserJet PCL XL printer stream."
content_hash: 1ae8d7c61844f2ef5b9e2cd02bc1dca2619f2433
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pnmtopclxl

Convert a PNM file to an HP LaserJet PCL XL printer stream.
More information: <https://netpbm.sourceforge.net/doc/pnmtopclxl.html>.

- Convert PNM files to an HP LaserJet PCL XL printer stream:

`pnmtopclxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pclxl</span>

- Specify the resolution of the image as well as the location of the page from the upper left corner of each image:

`pnmtopclxl -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resolution</span>` -xoffs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_offset</span>` -yoffs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_offset</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pclxl</span>

- Generate a duplex printer stream for the specified paper format:

`pnmtopclxl -duplex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vertical|horizontal</span>` -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">letter|legal|a3|a4|a5|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pclxl</span>
