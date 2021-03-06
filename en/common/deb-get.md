---
layout: page
title: common/deb-get (English)
description: "`apt-get` functionality for `.deb` packages published in third party repositories or via direct download."
content_hash: 8b1f57be38738807a651c284ca661fe515a20fc4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># deb-get

`apt-get` functionality for `.deb` packages published in third party repositories or via direct download.
Works with Linux distributions which use `apt-get`.
More information: <https://github.com/wimpysworld/deb-get>.

- Update the list of available packages and versions:

`sudo deb-get update`

- Search for a given package:

`sudo deb-get search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Show information about a package:

`sudo deb-get show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package, or update it to the latest available version:

`sudo deb-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package (using `purge` instead also removes its configuration files):

`sudo deb-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all installed packages to their newest available versions:

`sudo deb-get upgrade`

- List all available packages:

`deb-get list`
