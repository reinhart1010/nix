---
layout: page
title: common/chezmoi (English)
description: "A multi-machine dotfile manager, written in Go."
content_hash: 06d99f186452124572d3c6e73f3a2f9e92257482
last_modified_at: 2024-05-22
related_topics:
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chezmoi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Chezmoi

A multi-machine dotfile manager, written in Go.
See also: `stow`, `tuckr`, `vcsh`, `homeshick`.
More information: <https://chezmoi.io>.

- Setup up `chezmoi`, creating a Git repository in `~/.local/share/chezmoi`:

`chezmoi init`

- Set up `chezmoi` from existing dotfiles of a Git repository:

`chezmoi init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Start tracking one or more dotfiles:

`chezmoi add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dotfile1 path/to/dotfile2 ...</span>

- Update repository with local changes:

`chezmoi re-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dotfile1 path/to/dotfile2 ...</span>

- Edit the source state of a tracked dotfile:

`chezmoi edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dotfile_or_symlink</span>

- See pending changes:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Pull changes from a remote repository and apply them:

`chezmoi update`
