---
layout: page
title: linux/homeshick (English)
description: "Synchronize Git dotfiles."
content_hash: a99cabd817f114c28bb05164cd3c14a32fc68042
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# homeshick

Synchronize Git dotfiles.
See also: `chezmoi`, `stow`, `tuckr`, `vcsh`.
More information: <https://github.com/andsens/homeshick/wiki>.

- Create a new castle:

`homeshick generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>

- Add a file to your castle:

`homeshick track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Go to a castle:

`homeshick cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>

- Clone a castle:

`homeshick clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github_username</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Symlink all files from a castle:

`homeshick link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">castle_name</span>
