---
layout: page
title: linux/jobs (English)
description: "Shell builtin for viewing information about processes spawned by the current shell."
content_hash: 8dedb75dddaef5902c9e43b8671c5927f5b32bba
last_modified_at: 2023-06-17
---
# jobs

Shell builtin for viewing information about processes spawned by the current shell.
Options other than `-l` and `-p` are exclusive to `bash`.
More information: <https://manned.org/jobs>.

- View jobs spawned by the current shell:

`jobs`

- List jobs and their process IDs:

`jobs -l`

- Display information about jobs with changed status:

`jobs -n`

- Display only process IDs:

`jobs -p`

- Display running processes:

`jobs -r`

- Display stopped processes:

`jobs -s`
