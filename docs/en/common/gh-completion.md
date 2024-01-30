---
layout: page
title: common/gh-completion (English)
description: "Generate shell completion scripts for GitHub CLI commands."
content_hash: fb0e807b5f5b6503d5550a768727cfd803fb0f26
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# gh completion

Generate shell completion scripts for GitHub CLI commands.
More information: <https://cli.github.com/manual/gh_completion>.

- Print a completion script:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish|powershell</span>

- Append the `gh` completion script to `~/.bashrc`:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.bashrc</span>

- Append the `gh` completion script to `~/.zshrc`:

`gh completion --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zshrc</span>

- Display the subcommand help:

`gh completion`
