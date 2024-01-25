---
layout: page
title: linux/rpmconf (English)
description: "Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades."
content_hash: 3973ec668a28ac027c55cdcf2dfdf7afa5dde803
last_modified_at: 2024-01-25
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpmconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpmconf

Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades.
See also: `rpm`.
More information: <https://github.com/xsuchy/rpmconf>.

- List leftover files and interactively choose what to do with each of them:

`sudo rpmconf --all`

- Delete orphaned RPMNEW and RPMSAVE files:

`sudo rpmconf --all --clean`
