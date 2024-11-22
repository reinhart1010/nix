---
layout: page
title: linux/let (English)
description: "Evaluate arithmetic expressions in shell."
content_hash: 5dc32904f52a4fcc155d36fc1e28e2fa46ccc03a
last_modified_at: 2024-11-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/let.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># let

Evaluate arithmetic expressions in shell.
Supports variables, operators, and conditional expressions.
More information: <https://manned.org/let>.

- Evaluate a simple arithmetic expression:

`let "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">result = a + b</span>`"`

- Use post-increment and assignment in an expression:

`let "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x++</span>`"`

- Use conditional operator in an expression:

`let "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">result = (x > 10) ? x : 0</span>`"`

- Display help:

`let --help`
