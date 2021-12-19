---
layout: page
title: common/tb (English)
description: "CLI for managing tasks and notes across multiple boards."
content_hash: 69c4ffae1cc3561f2f3e67f393a9cb64446377ee
---
# tb

CLI for managing tasks and notes across multiple boards.
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
