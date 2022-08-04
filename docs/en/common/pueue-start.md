---
layout: page
title: common/pueue-start (English)
description: "Resume operation of specific tasks or groups of tasks."
content_hash: e05902a6ef945a22ae68db192e3bda36cd0b9320
---
# pueue start

Resume operation of specific tasks or groups of tasks.
See also: `pueue pause`.
More information: <https://github.com/Nukesor/pueue>.

- Resume all tasks in the default group:

`pueue start`

- Resume a specific task:

`pueue start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Resume multiple tasks at once:

`pueue start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Resume all tasks and start their children:

`pueue start --all --children`

- Resume all tasks in a specific group:

`pueue start group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>
