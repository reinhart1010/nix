---
layout: page
title: windows/gcrane-completion (English)
description: "Generate the autocompletion script for gcrane for the specified shell."
content_hash: 48e49e49347dbd0dc382d9e01fae075506f0830b
last_modified_at: 2024-10-26
tldri18n_status: 2
---
# gcrane completion

Generate the autocompletion script for gcrane for the specified shell.
The available shells are `bash`, `fish`, `powershell`, and `zsh`.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Generate the autocompletion script for your shell:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_name</span>

- Disable completion descriptions:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_name</span>` --no-descriptions`

- Load completions in your current shell session (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Load completions for every new session (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Display help:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
