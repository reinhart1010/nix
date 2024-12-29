---
layout: page
title: common/ppmdraw (English)
description: "Draw lines, text and more on a PPM image by executing a script."
content_hash: c18224b54cca771f17faa692f95515ecde8c8e36
last_modified_at: 2024-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmdraw.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmdraw

Draw lines, text and more on a PPM image by executing a script.
Documentation on the utilized scripting language can be found by following the link below.
More information: <https://netpbm.sourceforge.net/doc/ppmdraw.html>.

- Draw on the specified PPM image by executing the supplied script:

`ppmdraw -script '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setpos 50 50; text_here "hello!"; </span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Draw on the specified PPM image by executing the script in the specified file:

`ppmdraw -scriptfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
