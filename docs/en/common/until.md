---
layout: page
title: common/until (English)
description: "Simple shell loop that repeats until it receives zero as return value."
content_hash: 0a5a34e61a1d4e9e035d47b4b62d051c0f1c52e4
last_modified_at: 2024-12-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/until.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># until

Simple shell loop that repeats until it receives zero as return value.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-until>.

- Execute a command until it succeeds:

`until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; do :; done`

- Wait for a systemd service to be active:

`until systemctl is-active --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Waiting..."</span>`; sleep 1; done; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Launched!"</span>
