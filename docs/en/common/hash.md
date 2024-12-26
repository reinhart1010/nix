---
layout: page
title: common/hash (English)
description: "View cached executable locations."
content_hash: b9a54c1e0859caa18159ade441c5ee88df8d947c
last_modified_at: 2024-12-26
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hash

View cached executable locations.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-hash>.

- View cached command locations for the current shell:

`hash`

- Clear the hash table:

`hash -r`

- Delete a specific command from the hash table:

`hash -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Print the full path of `command`:

`hash -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
