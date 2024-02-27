---
layout: page
title: linux/repo-remove (English)
description: "Package database maintenance utility which removes packages from a local repository."
content_hash: 013fe6b15b5fe45a8dbd2be5e27d00f9d25641e3
last_modified_at: 2024-02-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/repo-remove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># repo-remove

Package database maintenance utility which removes packages from a local repository.
More information: <https://man.archlinux.org/man/repo-add>.

- Remove a package from a local repository:

`repo-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
