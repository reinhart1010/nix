---
layout: page
title: linux/faillock (English)
description: "Display and modify authentication failure record files."
content_hash: d14a4b56112d2b8537ad1c32edf73d4e9861b557
last_modified_at: 2024-10-14
tldri18n_status: 2
---
# faillock

Display and modify authentication failure record files.
More information: <https://manned.org/faillock>.

- List login failures of the current user:

`faillock`

- Reset the failure records of the current user:

`faillock --reset`

- List login failures of all users:

`sudo faillock`

- List login failures of the specified user:

`sudo faillock --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Reset the failure records of the specified user:

`sudo faillock --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --reset`
