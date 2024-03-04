---
layout: page
title: common/pamtouil (English)
description: "Convert a PNM or PAM file into a Motif UIL icon file."
content_hash: 08d3ffb32d22c25d232f1a858e028d89c5d59e85
last_modified_at: 2024-03-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtouil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtouil

Convert a PNM or PAM file into a Motif UIL icon file.
More information: <https://netpbm.sourceforge.net/doc/pamtouil.html>.

- Convert a PNM or PAM file into a Motif UIL icon file:

`pamtouil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm|pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.uil</span>

- Specify a prefix string to be printed in the output UIL file:

`pamtouil -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uilname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm|pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.uil</span>
