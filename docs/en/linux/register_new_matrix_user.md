---
layout: page
title: linux/register_new_matrix_user (English)
description: "Used to register new users with a given home server when registration has been disabled."
content_hash: f5d1d2473af8e8345ec040501de692f70ea0a9e9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# register_new_matrix_user

Used to register new users with a given home server when registration has been disabled.
More information: <https://manned.org/register_new_matrix_user>.

- Create a user interactively:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>

- Create an admin user interactively:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>` --admin`

- Create an admin user non-interactively (not recommended):

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --admin`
