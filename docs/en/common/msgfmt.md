---
layout: page
title: common/msgfmt (English)
description: "Compile message catalog to binary format."
content_hash: ba09136e5694a0319dcc3c408add6d2928a73f84
last_modified_at: 2024-09-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/msgfmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msgfmt

Compile message catalog to binary format.
More information: <https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html>.

- Convert a `.po` file to a `.mo` file:

`msgfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.po</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mo</span>
