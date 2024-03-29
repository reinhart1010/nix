---
layout: page
title: common/pushd (English)
description: "Place a directory on a stack so it can be accessed later."
content_hash: 9fe0421b912cf5399dc790094cc4621a13cf5c78
last_modified_at: 2023-11-12
related_topics:
  - title: dansk version
    url: /da/common/pushd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pushd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pushd

Place a directory on a stack so it can be accessed later.
See also `popd` to switch back to original directory and `dirs` to display directory stack contents.
More information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Switch to directory and push it on the stack:

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Switch first and second directories on the stack:

`pushd`

- Rotate stack by making the 5th element the top of the stack:

`pushd +4`

- Rotate the stack 4 times to the left (the current directory stays at the top by replacing the 5th element):

`pushd -n +4`
