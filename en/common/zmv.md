---
layout: page
title: common/zmv (English)
description: "Move or rename files matching a specified extended glob pattern."
content_hash: 61ec3883d072c998b23de6b5ecf8160b8091ffe2
---
# zmv

Move or rename files matching a specified extended glob pattern.
See also `zcp` and `zln`.
More information: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Move files using a regular expression-like pattern:

`zmv '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- Preview the result of a move, without making any actual changes:

`zmv -n '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- Interactively move files, with a prompt before every change:

`zmv -i '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- Verbosely print each action as it's being executed:

`zmv -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`
