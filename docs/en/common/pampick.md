---
layout: page
title: common/pampick (English)
description: "Pick images out of a multi-image Netpbm stream."
content_hash: cf1acacb2a359c465b038816309e7cd0f41fa063
last_modified_at: 2024-03-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pampick.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pampick

Pick images out of a multi-image Netpbm stream.
See also: `pamfile`, `pamsplit`.
More information: <https://netpbm.sourceforge.net/doc/pampick.html>.

- Execute a shell command on each image in a Netpbm file:

`pampick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_number1 image_number2 ...</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
