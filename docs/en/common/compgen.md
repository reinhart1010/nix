---
layout: page
title: common/compgen (English)
description: "A built-in command for auto-completion in Bash, which is called on pressing TAB key twice."
content_hash: 8c989f1c8f8a3812314224496e69a4a0524b62d7
last_modified_at: 2024-12-26
related_topics:
  - title: español version
    url: /es/common/compgen.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/compgen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/compgen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/compgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compgen

A built-in command for auto-completion in Bash, which is called on pressing TAB key twice.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- List all commands that you could run:

`compgen -c`

- List all commands that you could run that start with a specified string:

`compgen -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">str</span>

- List all aliases:

`compgen -a`

- List all functions that you could run:

`compgen -A function`

- Show shell reserved keywords:

`compgen -k`

- See all available commands/aliases starting with 'ls':

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
