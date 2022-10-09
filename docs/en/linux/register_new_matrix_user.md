---
layout: page
title: linux/register_new_matrix_user (English)
description: "Used to register new users with a given home server when registration has been disabled."
content_hash: f5d1d2473af8e8345ec040501de692f70ea0a9e9
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># register_new_matrix_user

Used to register new users with a given home server when registration has been disabled.
More information: <https://manned.org/register_new_matrix_user>.

- Create a user interactively:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>

- Create an admin user interactively:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>` --admin`

- Create an admin user non-interactively (not recommended):

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --admin`
