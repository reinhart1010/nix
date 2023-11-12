---
layout: page
title: linux/apx-stacks (English)
description: "Manage stacks in `apx`."
content_hash: 414e1a5ba3a97d8bd41ed12db022406d594bf4d0
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/apx-stacks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx stacks

Manage stacks in `apx`.
Note: user-created stack configurations are stored in `~/.local/share/apx/stacks`.
More information: <https://github.com/Vanilla-OS/apx>.

- Interactively create a new stack configuration:

`apx stacks new`

- Interactively update a stack configuration:

`apx stacks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List all available stack configurations:

`apx stacks list`

- Remove a specified stack configuration:

`apx stacks rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Import a stack configuration:

`apx stacks import --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/stack.yml</span>

- Export the stack configuration (Note: the output flag is optional, it is exported to the current working directory by default):

`apx stacks export --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>
