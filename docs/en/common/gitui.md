---
layout: page
title: common/gitui (English)
description: "A lightweight keyboard-only TUI for Git."
content_hash: 3a05c6490ac7df6c96dfaee8fc66c2351669bcee
last_modified_at: 2024-04-03
tldri18n_status: 2
---
# gitui

A lightweight keyboard-only TUI for Git.
See also: `tig`, `git-gui`.
More information: <https://github.com/extrawurst/gitui>.

- Specify the color theme (defaults to `theme.ron`):

`gitui --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">theme</span>

- Store logging output into a cache directory:

`gitui --logging`

- Use notify-based file system watcher instead of tick-based update:

`gitui --watcher`

- Generate a bug report:

`gitui --bugreport`

- Use a specific Git directory:

`gitui --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Use a specific working directory:

`gitui --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display help:

`gitui --help`

- Display version:

`gitui --version`
