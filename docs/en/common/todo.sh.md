---
layout: page
title: common/todo.sh (English)
description: "Simple and extensible shell script for managing your `todo.txt` file."
content_hash: 7e4580a4c02129510ae1fa7ff0a0c8715a99d1a7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# todo.sh

Simple and extensible shell script for managing your `todo.txt` file.
More information: <https://github.com/todotxt/todo.txt-cli>.

- List every item:

`todo.sh ls`

- Add an item with project and context tags:

`todo.sh add '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context</span>`'`

- Mark an item as [do]ne:

`todo.sh do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_no</span>

- Remove an item:

`todo.sh rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_no</span>

- Set an item's [pri]ority (A-Z):

`todo.sh pri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_no</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>

- Replace an item:

`todo.sh replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_no</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_description</span>`'`
