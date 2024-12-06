---
layout: page
title: common/fd (English)
description: "An alternative to `find`."
content_hash: 19e319a3d6f5e70a1e70aba4d4e24460a8a1adc6
last_modified_at: 2024-12-06
related_topics:
  - title: 한국어 version
    url: /ko/common/fd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fd

An alternative to `find`.
Aims to be faster and easier to use than `find`.
More information: <https://github.com/sharkdp/fd>.

- Recursively find files matching a specific pattern in the current directory:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`"`

- Find files that begin with a specific string:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^string</span>`"`

- Find files with a specific extension:

`fd --extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- Find files in a specific directory:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include ignored and hidden files in the search:

`fd --hidden --no-ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`"`

- Execute a command on each search result returned:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`" --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
