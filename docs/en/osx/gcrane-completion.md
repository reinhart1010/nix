---
layout: page
title: osx/gcrane-completion (English)
description: "Generate the autocompletion script for gcrane for the specified shell."
content_hash: 8700d693c50b46be302878fa72c7583611e27085
last_modified_at: 2024-10-04
tldri18n_status: 2
---
# gcrane completion

Generate the autocompletion script for gcrane for the specified shell.
The available shells are `bash`, `fish`, `powershell`, and `zsh`.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Generate the autocompletion script for your shell:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_name</span>

- Disable completion descriptions:

`grance completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_name</span>` --no-descriptions`

- Load completions in your current shell session (bash/zsh):

`source <(gcrane completion bash/zsh)>`

- Load completions in your current shell session (fish):

`gcrane completion fish | source`

- Load completions for every new session (bash):

`gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane`

- Load completions for every new session (zsh):

`gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane`

- Load completions for every new session (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- Display help:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
