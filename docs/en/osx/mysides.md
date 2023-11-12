---
layout: page
title: osx/mysides (English)
description: "Add, list and remove finder favorites."
content_hash: dd8e90ba6567e0babd5022f4cc4daf60c906d5bf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mysides

Add, list and remove finder favorites.
More information: <https://github.com/mosen/mysides>.

- List sidebar favorites:

`mysides list`

- Add a new item to the end of the sidebar favorites:

`mysides add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///Users/Shared/example</span>

- Remove an item by name:

`mysides remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example</span>

- Add the current directory to the sidebar:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- Remove the current directory from the sidebar:

`mysides remove $(basename $(pwd))`
