---
layout: page
title: common/pamvalidate (English)
description: "Validate PAM, PGM, PBM and PPM files."
content_hash: 26472453a757fb15041590a2ab165cd4cb444ade
last_modified_at: 2024-03-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamvalidate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamvalidate

Validate PAM, PGM, PBM and PPM files.
See also: `pamfile`, `pamfix`.
More information: <https://netpbm.sourceforge.net/doc/pamvalidate.html>.

- Copy a Netpbm file from `stdin` to `stdout` if and only if it valid; fail otherwise:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | pamvalidate > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ext</span>
