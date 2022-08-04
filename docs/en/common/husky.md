---
layout: page
title: common/husky (English)
description: "Native Git hooks made easy."
content_hash: 82830e4ff4be855d7002d3dc8d16e02a6961f8ce
---
# husky

Native Git hooks made easy.
More information: <https://typicode.github.io/husky>.

- Install Husky in the current directory:

`husky install`

- Install Husky into a specific directory:

`husky install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Set a specific command as a `pre-push` hook for Git:

`husky set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.husky/pre-push</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>`"`

- Add a specific command to the current `pre-commit` hook:

`husky add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.husky/pre-commit</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>`"`

- Uninstall Husky hooks from the current directory:

`husky uninstall`

- Display help:

`husky`
