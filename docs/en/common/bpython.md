---
layout: page
title: common/bpython (English)
description: "A fancy interface to the Python interpreter."
content_hash: e241c6c7976fb34d1310080bd6d80eca30074d74
last_modified_at: 2024-12-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bpython.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bpython

A fancy interface to the Python interpreter.
Provides syntax highlighting and many other nice-to-haves in REPL mode.
More information: <https://manned.org/bpython>.

- Start a REPL (interactive shell):

`bpython`

- Execute a specific Python file:

`bpython `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Execute a specific Python file and start a REPL:

`bpython --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Use the specified [c]onfig file instead of the default config:

`bpython --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.conf</span>
