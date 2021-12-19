---
layout: page
title: common/chezmoi (English)
description: "A multi-machine dotfile manager, written in Go."
content_hash: dbb58fbcab65a26f71e195f0e5612d87b3cdef7e
---
# Chezmoi

A multi-machine dotfile manager, written in Go.
More information: <https://chezmoi.io>.

- Initialize chezmoi on your machine:

`chezmoi init`

- Tell chezmoi to manage a dotfile:

`chezmoi add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Edit the source state of a tracked dotfile:

`chezmoi edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- See changes chezmoi would make:

`chezmoi diff`

- Apply the changes:

`chezmoi -v apply`

- Set chezmoi up on another machine by downloading existing dotfiles from a Git repository:

`chezmoi init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/path/to/repository.git</span>

- Fetch the latest changes from a remote repository:

`chezmoi update`
