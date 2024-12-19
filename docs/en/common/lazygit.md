---
layout: page
title: common/lazygit (English)
description: "A simple terminal UI for Git commands, providing an intuitive interface for managing repositories."
content_hash: ad784c98e3ee7b619a5de4818a6df96640ca3ab1
last_modified_at: 2024-12-19
tldri18n_status: 2
---
# lazygit

A simple terminal UI for Git commands, providing an intuitive interface for managing repositories.
More information: <https://github.com/jesseduffield/lazygit>.

- Open Lazygit in the current repository:

`lazygit`

- Open Lazygit for a specific Git repository:

`lazygit --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>

- Start Lazygit with focus on a specific panel:

`lazygit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status|branch|log|stash|...</span>

- Print the default Lazygit configuration:

`lazygit --config`

- Tail the Lazygit logs (useful with debug mode in another terminal):

`lazygit --logs`

- Run Lazygit in debug mode:

`lazygit --debug`

- Print the configuration directory:

`lazygit --print-config-dir`
