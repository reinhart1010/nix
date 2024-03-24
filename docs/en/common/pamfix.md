---
layout: page
title: common/pamfix (English)
description: "Fix errors in PAM, PBM, PGM and PPM files."
content_hash: 4ff6efa5c0d47fcab7765adfd80627844a177ca2
last_modified_at: 2024-03-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamfix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamfix

Fix errors in PAM, PBM, PGM and PPM files.
See also: `pamfile`, `pamvalidate`.
More information: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Fix a Netpbm file that is missing its last part:

`pamfix -truncate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corrupted.ext} > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ext</span>

- Fix a Netpbm file where pixel values exceed the image's `maxval` by lowering the offending pixels' values:

`pamfix -clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corrupted.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ext</span>

- Fix a Netpbm file where pixel values exceed the image's maxval by increasing it:

`pamfix -changemaxval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corrupted.pam|pbm|pgm|ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam|pbm|pgm|ppm</span>
