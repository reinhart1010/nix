---
layout: page
title: common/qr (English)
description: "Generate QR codes in the terminal with ANSI VT-100 escape codes."
content_hash: a3a3c85a7468b93cafab060061b2d635870e9241
---
# qr

Generate QR codes in the terminal with ANSI VT-100 escape codes.
More information: <https://github.com/lincolnloop/python-qrcode/>.

- Generate a QR code:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data</span>`" | qr`

- Specify the error correction level (defaults to M):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data</span>`" | qr --error-correction=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">L|M|Q|H</span>
