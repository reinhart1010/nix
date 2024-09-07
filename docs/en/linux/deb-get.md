---
layout: page
title: linux/deb-get (English)
description: "`apt-get` functionality for `.deb` packages published in third party repositories or via direct download."
content_hash: 67b0447120397b5314163540de56e31acd453c13
last_modified_at: 2024-09-07
tldri18n_status: 2
---
# deb-get

`apt-get` functionality for `.deb` packages published in third party repositories or via direct download.
Works with Linux distributions which use `apt-get`.
More information: <https://github.com/wimpysworld/deb-get>.

- Update the list of available packages and versions:

`deb-get update`

- Search for a given package:

`deb-get search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Show information about a package:

`deb-get show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package, or update it to the latest available version:

`deb-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package (using `purge` instead also removes its configuration files):

`deb-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all installed packages to their newest available versions:

`deb-get upgrade`

- List all available packages:

`deb-get list`
