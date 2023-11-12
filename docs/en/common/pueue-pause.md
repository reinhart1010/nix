---
layout: page
title: common/pueue-pause (English)
description: "Pause running tasks or groups."
content_hash: fa05b40058eae89f7b2b0c00b0a635d40a6911cb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pueue pause

Pause running tasks or groups.
See also: `pueue start`.
More information: <https://github.com/Nukesor/pueue>.

- Pause all tasks in the default group:

`pueue pause`

- Pause a running task:

`pueue pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Pause a running task and stop all its direct children:

`pueue pause --children `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Pause all tasks in a group and prevent it from starting new tasks:

`pueue pause --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Pause all tasks and prevent all groups from starting new tasks:

`pueue pause --all`
