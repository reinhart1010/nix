---
layout: page
title: common/git-maintenance (English)
description: "Run tasks to optimize Git repository data."
content_hash: 7acf00a14840ec27f7fbf6b0949015f2e01e0ca7
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/git-maintenance.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-maintenance

Run tasks to optimize Git repository data.
More information: <https://git-scm.com/docs/git-maintenance>.

- Register the current repository in the user's list of repositories to daily have maintenance run:

`git maintenance register`

- Schedule maintenance tasks on the current repository every hour:

`git maintenance start`

- Halt the background maintenance schedule for the current repository:

`git maintenance stop`

- Remove the current repository from the user's maintenance repository list:

`git maintenance unregister`

- Run a specific maintenance task on the current repository:

`git maintenance run --task=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch</span>
