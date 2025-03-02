---
layout: page
title: linux/pacstall (English)
description: "An AUR package manager for Ubuntu."
content_hash: a8e1a83e942d1a406708002a1b5b0daac45e651e
last_modified_at: 2024-10-15
tldri18n_status: 2
---
# pacstall

An AUR package manager for Ubuntu.
More information: <https://github.com/pacstall/pacstall>.

- Search the package database for a package name:

`pacstall --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Install a package:

`pacstall --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`pacstall --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Add a repository to the database (only GitHub and GitLab are supported):

`pacstall --add-repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>

- Update pacstall's scripts:

`pacstall --update`

- Update all packages:

`pacstall --upgrade`

- Display information about a package:

`pacstall --cache-info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List all installed packages:

`pacstall --list`
