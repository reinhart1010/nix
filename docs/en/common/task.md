---
layout: page
title: common/task (English)
description: "Command-line to-do list manager."
content_hash: 908553453b94dc012906748bb2e0a601281b289f
related_topics:
  - title: italiano version
    url: /it/common/task.html
    icon: bi bi-globe
---
# task

Command-line to-do list manager.
More information: <https://taskwarrior.org/docs/>.

- Add a new task which is due tomorrow:

`task add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tomorrow</span>

- Update a task's priority:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` modify priority:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|M|L</span>

- Complete a task:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` done`

- Delete a task:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` delete`

- List all open tasks:

`task list`

- List open tasks due before the end of the week:

`task list due.before:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eow</span>

- Show a graphical burndown chart, by day:

`task burndown.daily`

- List all reports:

`task reports`
