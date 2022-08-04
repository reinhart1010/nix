---
layout: page
title: linux/dconf-write (English)
description: "Write a value to a dconf database path."
content_hash: 2e21194e8604a512177286f836aefcb6ef13a245
---
# dconf write

Write a value to a dconf database path.
More information: <https://developer.gnome.org/dconf>.

- Write a string to a dconf path (note the nested quotes):

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/example/dconf/path</span>` "'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example Value</span>`'"`

- Write a boolean to a dconf path:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/example/dconf/path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>

- Write an integer to a dconf path:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/example/dconf/path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Write an array to a dconf path:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/example/dconf/path</span>` "[`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'My First Value', 'My Second Value'</span>`]"`

- Write an empty array to a dconf path:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/example/dconf/path</span>` "@as []"`
