---
layout: page
title: common/chezmoi (English)
description: "A multi-machine dotfile manager, written in Go."
content_hash: a064d3bdf21c8b6973cb81efce1e487172b1ada5
last_modified_at: 2024-02-09
related_topics:
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chezmoi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Chezmoi

A multi-machine dotfile manager, written in Go.
More information: <https://chezmoi.io>.

- Setup up `chezmoi`, creating a Git repository in `~/.local/share/chezmoi`:

`chezmoi init`

- Start tracking one or more dotfiles:

`chezmoi add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dotfile1 path/to/dotfile2 ...</span>

- Edit the source state of a tracked dotfile:

`chezmoi edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dotfile_or_symlink</span>

- See pending changes:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Set up `chezmoi` from existing dotfiles of a Git repository:

`chezmoi init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Pull changes from a remote repository and apply them:

`chezmoi update`
