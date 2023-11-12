---
layout: page
title: linux/apx-subsystems (English)
description: "Manage subsystems in `apx`."
content_hash: 583cfea86b8d1c5aebf58212e236a4867cc2b929
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/apx-subsystems.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx subsystems

Manage subsystems in `apx`.
Subsystems are containers that can be created based on pre-existing stacks.
More information: <https://github.com/Vanilla-OS/apx>.

- Interactively create a new subsystem:

`apx subsystems new`

- List all available subsystems:

`apx subsystems list`

- Reset a specific subsystem to its initial state:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- [f]orce reset a specific subsystem:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` --force`

- Remove a specific subsystem:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- [f]orce remove a specific subsystem:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` --force`
