---
layout: page
title: linux/eselect-repository (English)
description: "An `eselect` module for configuring ebuild repositories for Portage."
content_hash: b843109e3be08e76b71e39ecb996497dfa43db58
last_modified_at: 2024-07-07
tldri18n_status: 2
---
# eselect repository

An `eselect` module for configuring ebuild repositories for Portage.
After enabling a repository, you have to run `emerge --sync repo_name` to download ebuilds.
More information: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- List all ebuild repositories registered on <https://repos.gentoo.org>:

`eselect repository list`

- List enabled repositories:

`eselect repository list -i`

- Enable a repository from the list by its name or index from the `list` command:

`eselect repository enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|index</span>

- Enable an unregistered repository:

`eselect repository add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsync|git|mercurial|svn|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sync_uri</span>

- Disable repositories without removing their contents:

`eselect repository disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo1 repo2 ...</span>

- Disable repositories and remove their contents:

`eselect repository remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo1 repo2 ...</span>

- Create a local repository and enable it:

`eselect repository create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>
