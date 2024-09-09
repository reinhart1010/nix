---
layout: page
title: linux/sa (English)
description: "Summarize accounting information about commands called by users, including basic information on CPU time spent processing and I/O rates."
content_hash: b396e06c0119a8bbf83b24632e84cfbb1f7c691d
last_modified_at: 2024-09-09
tldri18n_status: 2
---
# sa

Summarize accounting information about commands called by users, including basic information on CPU time spent processing and I/O rates.
Part of the `acct` package.
More information: <https://manned.org/sa.8>.

- Display executable invocations per user (username not displayed):

`sudo sa`

- Display executable invocations per user, showing responsible usernames:

`sudo sa --print-users`

- List resources used recently per user:

`sudo sa --user-summary`
