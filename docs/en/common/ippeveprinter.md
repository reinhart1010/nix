---
layout: page
title: common/ippeveprinter (English)
description: "A simple IPP Everywhere printer server."
content_hash: ea0e007c515df7cac6903fb2aee712fae32b7d85
last_modified_at: 2023-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ippeveprinter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ippeveprinter

A simple IPP Everywhere printer server.
See also: `ippeveps`, `ippevepcl`.
More information: <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>.

- Run the server with a specific service name:

`ippeveprinter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`"`

- Load printer attributes from a PPD file:

`ippeveprinter -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppd</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`"`

- Run the `file` command whenever a job is sent to the server:

`ippeveprinter -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/file</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`"`

- Specify the directory that will hold the print files (by default, a directory under the user's temporary directory):

`ippeveprinter -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spool_directory</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`"`

- Keep the print documents in the spool directory rather than deleting them:

`ippeveprinter -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`"`

- Specify the printer speed in pages/minute unit (10 by default):

`ippeveprinter -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">speed</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>`"`
