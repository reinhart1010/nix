---
layout: page
title: common/pamexec (English)
description: "Execute a shell command on each image in a Netpbm file."
content_hash: 87d354f7a22c84aaa5caaca36b8d08f453b82a72
last_modified_at: 2024-03-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamexec

Execute a shell command on each image in a Netpbm file.
See also: `pamfile`, `pampick`, `pamsplit`.
More information: <https://netpbm.sourceforge.net/doc/pamexec.html>.

- Execute a shell command on each image in a Netpbm file:

`pamexec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>

- Stop processing if a command terminates with a nonzero exit status:

`pamexec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` -check`
