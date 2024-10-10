---
layout: page
title: common/bind (English)
description: "Bash builtin to manage bash hotkeys and variables."
content_hash: 1c69cad8a19b5a2f8fa231cb97c6424d4cb264d3
last_modified_at: 2024-10-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bind.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bind

Bash builtin to manage bash hotkeys and variables.
More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- List all bound commands and their hotkeys:

`bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|-P</span>

- Query a command for its hotkey:

`bind -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Bind a key:

`bind -x '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_sequence</span>`":`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`'`

- List user defined bindings:

`bind -X`

- Display help:

`help bind`
