---
layout: page
title: common/ipptool (English)
description: "Issue IPP requests and receive printer's/server's responses."
content_hash: 365ae99a790bb4f50c3f3a51b6a96c186e39624c
last_modified_at: 2024-01-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ipptool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ipptool

Issue IPP requests and receive printer's/server's responses.
See also: `ippfind`, `ippeveprinter`.
More information: <https://openprinting.github.io/cups/doc/man-ipptool.html>.

- Get all attributes and their values supported by a printer:

`ipptool ipp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_uri</span>` get-completed-jobs.test`

- Get the list of completed jobs of a printer:

`ipptool ipp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_uri</span>` get-completed-jobs.test`

- Send an email notification when a printer changes:

`ipptool -d recipient=mailto:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` ipp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_uri</span>` create-printer-subscription.test`
