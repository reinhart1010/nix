---
layout: page
title: common/npx (English)
description: "Execute binaries from `npm` packages."
content_hash: 23daaac991c10d0a605b443500bda45348e7e5ea
last_modified_at: 2023-04-10
related_topics:
  - title: Deutsch version
    url: /de/common/npx.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/npx.html
    icon: bi bi-globe
---
# npx

Execute binaries from `npm` packages.
More information: <https://github.com/npm/npx>.

- Execute the command from a local or remote `npm` package:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>

- In case multiple commands with the same name exist, it is possible to specify the package name:

`npx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command if it exists in the current path or in `node_modules/.bin`:

`npx --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Execute a specific command suppressing any output from `npx` itself:

`npx --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>

- Display help:

`npx --help`
