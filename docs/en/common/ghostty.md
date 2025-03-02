---
layout: page
title: common/ghostty (English)
description: "A fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration."
content_hash: 093c8b29d8c66941637ab535bfc319b1519d2355
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/ghostty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghostty

A fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.
Note: all options from the configuration file can also be used on the command-line (using `--option=argument`).
More information: <https://ghostty.org/docs/config/reference>.

- Open a new Ghostty window (not supported on macOS):

`ghostty`

- Run a specific command in a new Ghostty window (not supported on macOS):

`ghostty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- List all default and configured keybindings:

`ghostty +list-keybinds`

- List all actions (i.e. what can be triggered via keybindings):

`ghostty +list-actions`

- Browse an interactive list of themes:

`ghostty +list-themes`

- Print the default configuration (including comments):

`ghostty +show-config --default --docs`
