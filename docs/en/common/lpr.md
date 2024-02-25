---
layout: page
title: common/lpr (English)
description: "Print files."
content_hash: de10a83c9f8a3e35f1bd1908c95d929b4c995a77
last_modified_at: 2024-02-25
related_topics:
  - title: Deutsch version
    url: /de/common/lpr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpr

Print files.
See also: `lpstat` and `lpadmin`.
More information: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- Print a file to the default printer:

`lpr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print 2 copies:

`lpr -# `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print to a named printer:

`lpr -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print either a single page (e.g. 2) or a range of pages (e.g. 2–16):

`lpr -o page-ranges=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|2-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print double-sided either in portrait (long) or in landscape (short):

`lpr -o sides=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">two-sided-long-edge|two-sided-short-edge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Set page size (more options may be available depending on setup):

`lpr -o media=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4|letter|legal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print multiple pages per sheet:

`lpr -o number-up=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|4|6|9|16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
