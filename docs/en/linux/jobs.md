---
layout: page
title: linux/jobs (English)
description: "Shell builtin for viewing information about processes spawned by the current shell."
content_hash: b1dd0fa9ab634e7b338d6fff56b936284545d7ec
last_modified_at: 2024-11-26
related_topics:
  - title: 한국어 version
    url: /ko/linux/jobs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/jobs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jobs

Shell builtin for viewing information about processes spawned by the current shell.
Options other than `-l` and `-p` are exclusive to `bash`.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-jobs>.

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
