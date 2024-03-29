---
layout: page
title: common/cowsay (English)
description: "Print ASCII art (by default a cow) saying or thinking something."
content_hash: 7e4b7550d0b9e44c97bae4ffe183288dda0af8ff
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/cowsay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cowsay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cowsay

Print ASCII art (by default a cow) saying or thinking something.
More information: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Print an ASCII cow saying "hello, world":

`cowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`"`

- Print an ASCII cow saying text from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`" | cowsay`

- List all available art types:

`cowsay -l`

- Print the specified ASCII art saying "hello, world":

`cowsay -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">art</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`"`

- Print a dead thinking ASCII cow:

`cowthink -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">I'm just a cow, not a great thinker...</span>`"`

- Print an ASCII cow with custom eyes saying "hello, world":

`cowsay -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello, world</span>`"`
