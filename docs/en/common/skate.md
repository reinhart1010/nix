---
layout: page
title: common/skate (English)
description: "Simple and powerful key-value store."
content_hash: 4ec0bb3fcb9176c0f2b7f810fc988c54fd70d655
last_modified_at: 2023-04-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># skate

Simple and powerful key-value store.
More information: <https://github.com/charmbracelet/skate>.

- Store a key and a value on the default database:

`skate set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Show your keys saved on the default database:

`skate list`

- Delete key and value from the default database:

`skate delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`"`

- Create a new key and value in a new database:

`skate set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`"@"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Show your keys saved in a non default database:

`skate list @"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>`"`

- Delete key and value from a specific database:

`skate delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`"@"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>`"`

- Show the databases available:

`skate list-dbs`

- Delete local db and pull down fresh copy from Charm Cloud:

`skate reset @"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_name</span>`"`
