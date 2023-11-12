---
layout: page
title: common/topydo (English)
description: "A to-do list application that uses the todo.txt format."
content_hash: 364f021ffbc534f72af89f8b3ac7890e2632cb58
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/topydo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# topydo

A to-do list application that uses the todo.txt format.
More information: <https://github.com/topydo/topydo>.

- Add a to-do to a specific project with a given context:

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo_message</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context_name</span>`"`

- Add a to-do with a due date of tomorrow with a priority of `A`:

`topydo add "(A) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo _message</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1d</span>`"`

- Add a to-do with a due date of Friday:

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo_message</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fri</span>`"`

- Add a non-strict repeating to-do (next due = now + rec):

`topydo add "water flowers due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mon</span>` rec:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1w</span>`"`

- Add a strict repeating to-do (next due = current due + rec):

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo_message</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-01-01</span>` rec:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+1m</span>`"`

- Revert the last `topydo` command executed:

`topydo revert`
