---
layout: page
title: common/todoist (English)
description: "Access <https://todoist.com> from the command-line."
content_hash: 7f457cf1c0739e7b88463e6e254e68ad2d72ef6a
last_modified_at: 2023-11-12
related_topics:
  - title: română version
    url: /ro/common/todoist.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todoist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todoist

Access <https://todoist.com> from the command-line.
More information: <https://github.com/sachaos/todoist>.

- Add a task:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>`"`

- Add a high priority task with a label, project, and due date:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>`" --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --label-ids "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_id</span>`" --project-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>`" --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmr 9am</span>`"`

- Add a high priority task with a label, project, and due date in quick mode:

`todoist quick '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmr 9am</span>`" p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_name</span>`'`

- List all tasks with a header and color:

`todoist --header --color list`

- List all high priority tasks:

`todoist list --filter p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- List today's tasks with high priority that have the specified label:

`todoist list --filter '(@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_name</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>`) & p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`'`
