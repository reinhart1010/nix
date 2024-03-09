---
layout: page
title: common/bpkg (English)
description: "A package manager for Bash scripts."
content_hash: 1c113f5efc7c80fa8cecd6fb701072e2a153b66f
last_modified_at: 2024-03-09
tldri18n_status: 2
---
# bpkg

A package manager for Bash scripts.
More information: <https://github.com/bpkg/bpkg>.

- Update the local index:

`bpkg update`

- Install a package globally:

`bpkg install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package in a subdirectory of the current directory:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a specific version of a package globally:

`bpkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -g`

- Show details about a specific package:

`bpkg show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Run a command, optionally specifying its arguments:

`bpkg run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>
