---
layout: page
title: common/pueue-restart (English)
description: "Restart tasks."
content_hash: 6515401040d0c947a5c61cb87912d2784d0c3dd1
---
# pueue restart

Restart tasks.
More information: <https://github.com/Nukesor/pueue>.

- Restart a specific task:

`pueue restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Restart multiple tasks at once, and start them immediately (do not enqueue):

`pueue restart --start-immediately `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Restart a specific task from a different path:

`pueue restart --edit-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Edit a command before restarting:

`pueue restart --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Restart a task in-place (without enqueuing as a separate task):

`pueue restart --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Restart all failed tasks and stash them:

`pueue restart --all-failed --stashed`
