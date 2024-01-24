---
layout: page
title: common/chronic (English)
description: "Display `stdout` and `stderr` of a command if and only if it fails."
content_hash: 098ce883a5bf8f21c85d12cd53ba945a70f41528
last_modified_at: 2024-01-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chronic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chronic

Display `stdout` and `stderr` of a command if and only if it fails.
More information: <https://joeyh.name/code/moreutils/>.

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-zero exit code or crashes:

`chronic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-empty `stderr`:

`chronic -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>

- Enable [v]erbose mode:

`chronic -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command options ...</span>
