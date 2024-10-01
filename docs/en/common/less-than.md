---
layout: page
title: common/less-than (English)
description: "Redirect a file to `stdin`."
content_hash: e986d64436b086b035b97ea8c64b6684c4b34d04
last_modified_at: 2024-10-01
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/less-than.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Less than

Redirect a file to `stdin`.
Achieves the same effect as `cat file.txt |`.
More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- Redirect a file to `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
