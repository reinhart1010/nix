---
layout: page
title: common/pueue-edit (English)
description: "Edit the command or path of a stashed or queued task."
content_hash: 56637934f1f9e617b0ee49a5220290b1a82d117f
---
# pueue edit

Edit the command or path of a stashed or queued task.
More information: <https://github.com/Nukesor/pueue>.

- Edit a task, see `pueue status` to get the task ID:

`pueue edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Edit the path from which a task is executed:

`pueue edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` --path`

- Edit a command with the specified editor:

`EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nano</span>` pueue edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>
