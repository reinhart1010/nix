---
layout: page
title: common/pueue-kill (English)
description: "Kill running tasks or whole groups."
content_hash: 62bbadfb1bf04cdbfa0686742e9f32ce031b8671
---
# pueue kill

Kill running tasks or whole groups.
More information: <https://github.com/Nukesor/pueue>.

- Kill all tasks in the default group:

`pueue kill`

- Kill a specific task:

`pueue kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Kill a task and terminate all its child processes:

`pueue kill --children `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Kill all tasks in a group and pause the group:

`pueue kill --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Kill all tasks across all groups and pause all groups:

`pueue kill --all`
