---
layout: page
title: common/fd (English)
description: "An alternative to `find`."
content_hash: 274e4252b443a30ee578f40b286966cd1b88fff3
last_modified_at: 2023-11-12
related_topics:
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

- Find files that begin with `foo`:

`fd "^foo"`

- Find files with a specific extension:

`fd --extension txt`

- Find files in a specific directory:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include ignored and hidden files in the search:

`fd --hidden --no-ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`"`

- Execute a command on each search result returned:

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string|regex</span>`" --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
