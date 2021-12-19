---
layout: page
title: common/compgen (English)
description: "A built-in command for auto-completion in Bash, which is called on pressing TAB key twice."
content_hash: 4063bd2ff9c6d2cd4ab03ea9be7fd6ef62b31c72
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/compgen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/compgen.html
    icon: bi bi-globe
---
# compgen

A built-in command for auto-completion in Bash, which is called on pressing TAB key twice.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- List all commands that you could run:

`compgen -c`

- List all aliases:

`compgen -a`

- List all functions that you could run:

`compgen -A function`

- Show shell reserved keywords:

`compgen -k`

- See all available commands/aliases starting with 'ls':

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
