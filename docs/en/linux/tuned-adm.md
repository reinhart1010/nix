---
layout: page
title: linux/tuned-adm (English)
description: "Manage and optimize system performance tuning profiles on Linux."
content_hash: c11bfbe104f979298062166eeb32c79309fbc44a
last_modified_at: 2024-10-25
tldri18n_status: 2
---
# tuned-adm

Manage and optimize system performance tuning profiles on Linux.
More information: <https://tuned-project.org>.

- List available profiles:

`tuned-adm list`

- Show the currently active profile:

`tuned-adm active`

- Set a specific tuning profile:

`tuned-adm profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Recommend a suitable profile based on the current system:

`tuned-adm recommend`

- Disable tuning:

`tuned-adm off`
