---
layout: page
title: common/pamarith (English)
description: "Apply a binary function on two Netpbm images."
content_hash: 00949906950b9a0c0c8485bb15891524c0d15a86
last_modified_at: 2024-03-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamarith.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamarith

Apply a binary function on two Netpbm images.
See also: `pamfunc`.
More information: <https://netpbm.sourceforge.net/doc/pamarith.html>.

- Apply the specified binary function pixel-wise on the two specified images (which must be of the same size):

`pamarith -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|subtract|multiply|divide|difference|minimum|maximum|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pam|pbm|pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.pam|pbm|pgm|ppm</span>
