---
layout: page
title: linux/dir (English)
description: "List directory contents using one line per file, special characters are represented by backslash escape sequences."
content_hash: 59547fc2c209e678d221a5c5451a4bd2a058dda3
last_modified_at: 2024-08-13
related_topics:
  - title: Nederlands version
    url: /nl/linux/dir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dir

List directory contents using one line per file, special characters are represented by backslash escape sequences.
Works as `ls -C --escape`.
More information: <https://manned.org/dir>.

- List all files, including hidden files:

`dir --all`

- List files including their author (`-l` is required):

`dir -l --author`

- List files excluding those that match a specified blob pattern:

`dir --hide=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- List subdirectories recursively:

`dir --recursive`

- Display help:

`dir --help`
