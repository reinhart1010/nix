---
layout: page
title: common/salt (English)
description: "Execute commands and assert state on remote salt minions."
content_hash: 22a7a41a5434fbf658a4db01e5cf6c8fa4751dd5
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# salt

Execute commands and assert state on remote salt minions.
More information: <https://docs.saltproject.io/en/latest/ref/cli/index.html>.

- List connected minions:

`salt '*' test.ping`

- Execute a highstate on all connected minions:

`salt '*' state.highstate`

- Upgrade packages using the OS package manager (apt, yum, brew) on a subset of minions:

`salt '*.example.com' pkg.upgrade`

- Execute an arbitrary command on a particular minion:

`salt '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minion_id</span>`' cmd.run "ls "`
