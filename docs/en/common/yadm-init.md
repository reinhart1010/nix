---
layout: page
title: common/yadm-init (English)
description: "Initialize a new, empty repository for tracking dotfiles."
content_hash: b88c9f0bd72314ef5d92f0e40ff40cae9bba596d
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm-init

Initialize a new, empty repository for tracking dotfiles.
The repository is stored in `$HOME/.local/share/yadm/repo.git`.
More information: <https://yadm.io/docs/getting_started>.

- Execute:

`yadm init`

- Override the worktree:

`yadm init -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/worktree_folder</span>

- Overwrite an existing repository:

`yadm init -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_repository</span>
