---
layout: page
title: linux/scriptreplay (English)
description: "Replay a typescript created by the `script` command to `stdout`."
content_hash: aa13b3c9cc9f5d2b7ee22e77ae84d8a5553af86f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# scriptreplay

Replay a typescript created by the `script` command to `stdout`.
More information: <https://manned.org/scriptreplay>.

- Replay a typescript at the speed it was recorded:

`scriptreplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timing_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>

- Replay a typescript at double the original speed:

`scriptreplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timingfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>` 2`

- Replay a typescript at half the original speed:

`scriptreplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/timingfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/typescript</span>` 0.5`
