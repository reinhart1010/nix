---
layout: page
title: linux/register_new_matrix_user (English)
description: "Register new users in a home server when registration has been disabled."
content_hash: b394ebe4c98a22b9b56e522e327d6f9c5997adb9
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# register_new_matrix_user

Register new users in a home server when registration has been disabled.
More information: <https://manned.org/register_new_matrix_user>.

- Create a user interactively:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>

- Create an admin user interactively:

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>` --admin`

- Create an admin user non-interactively (not recommended):

`register_new_matrix_user --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/homeserver.yaml</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --admin`
