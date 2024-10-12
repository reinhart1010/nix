---
layout: page
title: common/zmv (English)
description: "Move or rename files matching a specified extended glob pattern."
content_hash: c789901291088df8e854691b9c1b0eb0cb493e1c
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# zmv

Move or rename files matching a specified extended glob pattern.
See also `zcp` and `zln`.
More information: <https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Move files using a regular expression-like pattern:

`zmv '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- Preview the result of a move, without making any actual changes:

`zmv -n '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- Interactively move files, with a prompt before every change:

`zmv -i '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- Verbosely print each action as it's being executed:

`zmv -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`
