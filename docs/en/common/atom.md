---
layout: page
title: common/atom (English)
description: "A cross-platform pluggable text editor."
content_hash: ef80afa169ec3c3ae84060948acee927e85ec8db
last_modified_at: 2024-02-09
related_topics:
  - title: Deutsch version
    url: /de/common/atom.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atom.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atom.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/atom.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atom.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/atom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atom

A cross-platform pluggable text editor.
Plugins are managed by `apm`.
More information: <https://atom.io/>.

- Open a file or directory:

`atom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Open a file or directory in a [n]ew window:

`atom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Open a file or directory in an existing window:

`atom --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Open Atom in safe mode (does not load any additional packages):

`atom --safe`

- Prevent Atom from forking into the background, keeping Atom attached to the terminal:

`atom --foreground`

- Wait for Atom window to close before returning (useful for Git commit editor):

`atom --wait`
