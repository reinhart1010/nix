---
layout: page
title: linux/pacstall (English)
description: "An AUR package manager for Ubuntu."
content_hash: 5790da158030331b70a07da19da33760141a56aa
---
# pacstall

An AUR package manager for Ubuntu.
More information: <https://github.com/pacstall/pacstall>.

- Search the package database for a package name:

`pacstall --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install a package:

`pacstall --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package:

`pacstall --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Add a repository to the database (only GitHub and GitLab are supported):

`pacstall --add-repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>

- Update pacstall's scripts:

`pacstall --update`

- Update all packages:

`pacstall --upgrade`

- Display information about a package:

`pacstall --query-info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List all installed packages:

`pacstall --list`
