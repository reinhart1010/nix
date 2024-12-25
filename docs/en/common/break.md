---
layout: page
title: common/break (English)
description: "Break out of a `for`, `while`, `until` or `select` loop."
content_hash: 69d12c1d8e341f21e7e627e83d3c22384dfc1ae8
last_modified_at: 2024-12-25
tldri18n_status: 2
---
# break

Break out of a `for`, `while`, `until` or `select` loop.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-break>.

- Break out of a single loop:

`while :; do break; done`

- Break out of nested loops:

`while :; do while :; do break 2; done; done`
