---
layout: page
title: common/ippevepcl (English)
description: "Print to B&W HP PCL laser printers."
content_hash: a052e27953a333eac0c12a385cc62ddbfd8d0186
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# ippevepcl

Print to B&W HP PCL laser printers.
Supports HP PCL, PWG Raster and Apple Raster files.
See also: `ippevepcl`, `ippeveprinter`.
More information: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Print a file to `stdout` (status and progress messages are sent to `stderr`):

`ippeveps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a file from `stdin` to `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wget -O - https://examplewebsite.com/file</span>` | ippeveps`
