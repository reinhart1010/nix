---
layout: page
title: common/starship (English)
description: "The minimal, blazing-fast, and infinitely customizable prompt for any shell."
content_hash: ac38d7b789f578dda7c01781868d5265911defe4
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# starship

The minimal, blazing-fast, and infinitely customizable prompt for any shell.
Some subcommands such as `init` have their own usage documentation.
More information: <https://starship.rs>.

- Print the starship integration code for the specified shell:

`starship init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|elvish|fish|ion|powershell|tcsh|zsh</span>

- Explain each part of the current prompt and show the time taken to render them:

`starship explain`

- Print the computed starship configuration (use `--default` to print default configuration instead):

`starship print-config`

- List supported modules:

`starship module --list`

- Edit the starship configuration in the default editor:

`starship configure`

- Create a bug report GitHub issue pre-populated with information about the system and starship configuration:

`starship bug-report`

- Print the completion script for the specified shell:

`starship completions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|elvish|fish|powershell|zsh</span>

- Display help for a subcommand:

`starship `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
