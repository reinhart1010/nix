---
layout: page
title: common/lpinfo (English)
description: "List connected printers and installed drivers for the CUPS print server."
content_hash: c7588f29a0f2001bbb79aa123a69a7af2425aaec
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/lpinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpinfo

List connected printers and installed drivers for the CUPS print server.
More information: <https://openprinting.github.io/cups/doc/man-lpinfo.html>.

- List all the currently connected printers:

`lpinfo -v`

- List all the currently installed printer drivers:

`lpinfo -m`

- Search installed printer drivers by make and model:

`lpinfo --make-and-model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_model</span>`" -m`
