---
layout: page
title: common/git-maintenance (English)
description: "Run tasks to optimize Git repository data."
content_hash: 5a5a5b7f1d0744275db6f1e74aa121503ba69ef6
---
# git-maintenance

Run tasks to optimize Git repository data.
More information: <https://git-scm.com/docs/git-maintenance>.

- Register the current repository in the user's list of repositories to daily have maintenance run:

`git maintenance register`

- Start running maintenance on the current repository:

`git maintenance start`

- Halt the background maintenance schedule for the current repository:

`git maintenance stop`

- Remove the current repository from the user's maintenance repository list:

`git maintenance unregister`

- Run a specific maintenance task on the current repository:

`git maintenance run --task=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch</span>
