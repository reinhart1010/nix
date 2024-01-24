---
layout: page
title: common/zrun (English)
description: "Transparently uncompress argument files to a command."
content_hash: 00d175afc9d613387124512246ba3c2ce1ae06a0
last_modified_at: 2024-01-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zrun.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zrun

Transparently uncompress argument files to a command.
More information: <https://joeyh.name/code/moreutils/>.

- Run the specified command with uncompressed versions of the compressed argument files:

`zrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat path/to/file1.gz path/to/file2.bz2 ...</span>
