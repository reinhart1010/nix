---
layout: page
title: linux/sa (English)
description: "Summarizes accounting information. Part of the acct package."
content_hash: 604bc977baf1d8d2e34aa623a9511f3f5ce9a1e3
---
# sa

Summarizes accounting information. Part of the acct package.
Shows commands called by users, including basic info on CPU time spent processing and I/O rates.

- Display executable invocations per user (username not displayed):

`sudo sa`

- Display executable invocations per user, showing responsible usernames:

`sudo sa --print-users`

- List resources used recently per user:

`sudo sa --user-summary`
