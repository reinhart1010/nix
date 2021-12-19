---
layout: page
title: common/qrencode (English)
description: "QR Code generator. Supports PNG and EPS."
content_hash: a7d64fbd6d81b043c5ea85a88b5d68258bee3cc8
---
# qrencode

QR Code generator. Supports PNG and EPS.
More information: <https://fukuchi.org/works/qrencode>.

- Convert a string to a QR code and save to an output file:

`qrencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Convert an input file to a QR code and save to an output file:

`qrencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.png</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Convert a string to a QR code and print it in terminal:

`qrencode -t ansiutf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Convert input from pipe to a QR code and print it in terminal:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` | qrencode -t ansiutf8`
