---
layout: page
title: common/pueue-log (English)
description: "Display the log output of 1 or more tasks."
content_hash: 9c32039cbd584d2a66ff43efa478bcb6825a448b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pueue log

Display the log output of 1 or more tasks.
See also: `pueue status`.
More information: <https://github.com/Nukesor/pueue>.

- Show the last few lines of output from all tasks:

`pueue log`

- Show the full output of a task:

`pueue log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Show the last few lines of output from several tasks:

`pueue log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Print a specific number of lines from the tail of output:

`pueue log --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_lines</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>
