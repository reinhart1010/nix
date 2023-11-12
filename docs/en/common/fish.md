---
layout: page
title: common/fish (English)
description: "The Friendly Interactive SHell, a command-line interpreter designed to be user friendly."
content_hash: f3073734aa9fe4e063970705f7457b545b1d35fc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/fish.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fish

The Friendly Interactive SHell, a command-line interpreter designed to be user friendly.
More information: <https://fishshell.com>.

- Start an interactive shell session:

`fish`

- Start an interactive shell session without loading startup configs:

`fish --no-config`

- Execute specific commands:

`fish --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'fish is executed'</span>`"`

- Execute a specific script:

`fish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.fish</span>

- Check a specific script for syntax errors:

`fish --no-execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.fish</span>

- Execute specific commands from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'fish is executed'"</span>` | fish`

- Start an interactive shell session in private mode, where the shell does not access old history or save new history:

`fish --private`

- Define and export an environmental variable that persists across shell restarts (builtin):

`set --universal --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_value</span>
