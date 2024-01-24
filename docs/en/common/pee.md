---
layout: page
title: common/pee (English)
description: "Tee `stdin` to pipes."
content_hash: af3842329c1a1a3280ecdb1457b27248958214fd
last_modified_at: 2024-01-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pee.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pee

Tee `stdin` to pipes.
See also: `tee`.
More information: <https://joeyh.name/code/moreutils/>.

- Run each command, providing each one with a distinct copy of `stdin`:

`pee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 command2 ...</span>

- Write a copy of `stdin` to `stdout` (like `tee`):

`pee cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 command2 ...</span>

- Immediately terminate upon SIGPIPEs and write errors:

`pee --no-ignore-sigpipe --no-ignore-write-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1 command2 ...</span>
