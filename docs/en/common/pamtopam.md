---
layout: page
title: common/pamtopam (English)
description: "Copy a PAM image."
content_hash: 722905a47df17532c2a0dede9c76d358790be96f
last_modified_at: 2023-11-18
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtopam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtopam

Copy a PAM image.
More information: <https://netpbm.sourceforge.net/doc/pamtopam.html>.

- Copy a PAM image (i.e. a PBM, PGM, PPM or PAM image) from `stdin` to `stdout`:

`pamtopam < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Display version:

`pamtopam -version`
