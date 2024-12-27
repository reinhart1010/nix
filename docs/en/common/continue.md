---
layout: page
title: common/continue (English)
description: "Skip to the next iteration of a `for`, `while`, `until` or `select` loop."
content_hash: 5b48f4b56257947d2d7b9fd8a32c14e509c771b2
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# continue

Skip to the next iteration of a `for`, `while`, `until` or `select` loop.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-continue>.

- Skip to the next iteration:

`while :; do continue; echo "This will never be reached"; done`

- Skip to the next iteration from within a nested loop:

`for i in {1..3}; do while :; do continue 2; done; done`
