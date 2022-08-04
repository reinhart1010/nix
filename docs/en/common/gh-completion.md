---
layout: page
title: common/gh-completion (English)
description: "Generate shell completion scripts for GitHub CLI commands."
content_hash: 1743442bf2cc3209ebc41b59ee870589c0163db6
---
# gh completion

Generate shell completion scripts for GitHub CLI commands.
More information: <https://cli.github.com/manual/gh_completion>.

- Display the subcommand help:

`gh completion`

- Print a completion script:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish|powershell</span>

- Append the `gh` completion script to `~/.bashrc`:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.bashrc</span>

- Append the `gh` completion script to `~/.zshrc`:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zshrc</span>
