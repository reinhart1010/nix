---
layout: page
title: common/msgunfmt (English)
description: "Decompile message catalog from the binary format."
content_hash: 0a9fe8c53b6f768c946904a617cccdb0e50a1380
last_modified_at: 2024-09-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/msgunfmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msgunfmt

Decompile message catalog from the binary format.
More information: <https://www.gnu.org/software/gettext/manual/html_node/msgunfmt-Invocation.html>.

- Output conversion:

`msgunfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mo</span>

- Convert a `.mo` file to a `.po` file:

`msgunfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mo</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.po</span>
