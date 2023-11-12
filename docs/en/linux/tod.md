---
layout: page
title: linux/tod (English)
description: "A tiny Todoist client in Rust."
content_hash: cbc10440143f471e3b72450eb3eb6b28fd87c1d6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tod

A tiny Todoist client in Rust.
It takes simple input and dumps it in your inbox or another project. Taking advantage of natural language processing to assign due dates, tags, etc.
More information: <https://github.com/alanvardy/tod>.

- Import your projects (this is necessary to enable project prompts):

`tod project import`

- Quickly create a task with due date:

`tod --quickadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Buy more milk today</span>

- Create a new task (you will be prompted for content and project):

`tod task create`

- Create a task in a project:

`tod task create --content "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Write more rust</span>`" --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Get the next task for a project:

`tod task next`

- Get your work schedule:

`tod task list --scheduled --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">work</span>

- Get all tasks for work:

`tod task list --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">work</span>
