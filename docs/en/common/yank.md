---
layout: page
title: common/yank (English)
description: "Read input from `stdin` and display a selection interface that allows a field to be selected and copied to the clipboard."
content_hash: 119daea74897d82bcd38a5ccef68203d68b6bd97
last_modified_at: 2022-12-04
related_topics:
  - title: 中文 version
    url: /zh/common/yank.html
    icon: bi bi-globe
---
# yank

Read input from `stdin` and display a selection interface that allows a field to be selected and copied to the clipboard.
More information: <https://manned.org/yank>.

- Yank using the default delimiters (\f, \n, \r, \s, \t):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sudo dmesg</span>` | yank`

- Yank an entire line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sudo dmesg</span>` | yank -l`

- Yank using a specific delimiter:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo hello=world</span>` | yank -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">=</span>

- Only yank fields matching a specific pattern:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps ux</span>` | yank -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[0-9]+</span>`"`
