---
layout: page
title: common/tb (English)
description: "Manage tasks and notes across multiple boards."
content_hash: 94747946d4cdc2e6c35aabe8e51d750758a3c531
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tb

Manage tasks and notes across multiple boards.
More information: <https://github.com/klaussinani/taskbook>.

- Add a new task to a board:

`tb --task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_description</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">board_name</span>

- Add a new note to a board:

`tb --note `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">note_description</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">board_name</span>

- Edit item's priority:

`tb --priority @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>

- Check/uncheck item:

`tb --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_id</span>

- Archive all checked items:

`tb --clear`

- Move item to a board:

`tb --move @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">board_name</span>
