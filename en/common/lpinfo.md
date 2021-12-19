---
layout: page
title: common/lpinfo (English)
description: "List connected printers and installed drivers for the CUPS print server."
content_hash: eee7f9f7004f149f345709c0272046997aa33737
---
# lpinfo

List connected printers and installed drivers for the CUPS print server.
More information: <https://www.cups.org/doc/man-lpinfo.html>.

- List all the currently connected printers:

`lpinfo -v`

- List all the currently installed printer drivers:

`lpinfo -m`

- Search installed printer drivers by make and model:

`lpinfo --make-and-model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_model</span>`" -m`
