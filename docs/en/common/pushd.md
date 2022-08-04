---
layout: page
title: common/pushd (English)
description: "Place a directory on a stack so it can be accessed later."
content_hash: 31c0fc77c7b75b522c07994460766aed5adc9974
---
# pushd

Place a directory on a stack so it can be accessed later.
See also `popd` to switch back to original directory and `dirs` to display directory stack contents.

- Switch to directory and push it on the stack:

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- Switch first and second directories on the stack:

`pushd`

- Rotate stack by making the 5th element the top of the stack:

`pushd +4`
