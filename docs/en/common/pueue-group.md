---
layout: page
title: common/pueue-group (English)
description: "Display, add or remove groups."
content_hash: 1a59820245e61d087a0d23ff5151857961c83a93
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pueue group

Display, add or remove groups.
More information: <https://github.com/Nukesor/pueue>.

- Show all groups with their statuses and number of parallel jobs:

`pueue group`

- Add a custom group:

`pueue group --add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>`"`

- Remove a group and move its tasks to the default group:

`pueue group --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>`"`
