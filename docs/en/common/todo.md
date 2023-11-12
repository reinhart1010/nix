---
layout: page
title: common/todo (English)
description: "A simple, standards-based, cli todo manager."
content_hash: 01371c263ead570b07342719c77b23b32777fffd
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/todo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todo

A simple, standards-based, cli todo manager.
More information: <https://todoman.readthedocs.io>.

- List startable tasks:

`todo list --startable`

- Add a new task to the work list:

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thing_to_do</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">work</span>

- Add a location to a task with a given ID:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Show details about a task:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Mark tasks with the specified IDs as completed:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id1 task_id2 ...</span>

- Delete a task:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Delete done tasks and reset the IDs of the remaining tasks:

`todo flush`
