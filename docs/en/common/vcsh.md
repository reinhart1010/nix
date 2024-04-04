---
layout: page
title: common/vcsh (English)
description: "Version Control System for the home directory using Git repositories."
content_hash: b0eff1cabda737d106c8e8b8597ddb29a64aa092
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# vcsh

Version Control System for the home directory using Git repositories.
See also: `chezmoi`, `stow`, `tuckr`, `homeshick`.
More information: <https://github.com/RichiH/vcsh>.

- Initialize an (empty) repository:

`vcsh init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- Clone a repository into a custom directory name:

`vcsh clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>

- List all managed repositories:

`vcsh list`

- Execute a Git command on a managed repository:

`vcsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_command</span>

- Push/pull all managed repositories to/from remotes:

`vcsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">push|pull</span>

- Write a custom `.gitignore` file for a managed repository:

`vcsh write-gitignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>
