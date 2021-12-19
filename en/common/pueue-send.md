---
layout: page
title: common/pueue-send (English)
description: "Send input to a task."
content_hash: e8392d3d6e743cc97b7e6aee8e8dce8899deb024
---
# pueue send

Send input to a task.
More information: <https://github.com/Nukesor/pueue>.

- Send input to a running command:

`pueue send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>`"`

- Send confirmation to a task expecting y/N (e.g. apt, cp):

`pueue send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>
