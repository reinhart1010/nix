---
layout: page
title: common/pamsplit (English)
description: "Split a multi-image Netpbm file into multiple single-image Netpbm files."
content_hash: 615b89d2130f9f26dc8fc5611f893dba7677f90a
last_modified_at: 2024-03-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamsplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamsplit

Split a multi-image Netpbm file into multiple single-image Netpbm files.
See also: `pamfile`, `pampick`, `pamexec`.
More information: <https://netpbm.sourceforge.net/doc/pamsplit.html>.

- Split a multi-image Netpbm file into multiple single-image Netpbm files:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>

- Specify a pattern for naming output files:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_%d.pam</span>
