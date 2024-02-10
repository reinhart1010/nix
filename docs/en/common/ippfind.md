---
layout: page
title: common/ippfind (English)
description: "Find services registered with a DNS server or available through local devices."
content_hash: 8fc7d0bac5e36680c1b44d33a98cf84a567ab147
last_modified_at: 2024-02-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ippfind.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ippfind

Find services registered with a DNS server or available through local devices.
See also: `ipptool`, `ippeveprinter`.
More information: <https://openprinting.github.io/cups/doc/man-ippfind.html>.

- List IPP printers registered on the network with their status:

`ippfind --ls`

- Send a specific PostScript document to every PostScript printer on the network:

`ippfind --txt-pdl application/postscript --exec ipptool -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/document.ps</span>` '{}' print-job.test \;`

- Send a PostScript test document to every PostScript printer on the network:

`ippfind --txt-pdl application/postscript --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`

- Send a PostScript test document to every PostScript printer on the network, whose name matches a regular expression:

`ippfind --txt-pdl application/postscript --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>` --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`
