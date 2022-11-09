---
layout: page
title: linux/apx (English)
description: "Package management utility for Vanilla OS."
content_hash: 6fe298a0007285fc57a550fc7aca03e9d5be5c60
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apx

Package management utility for Vanilla OS.
Install packages inside managed containers or directly inside the host.
More information: <https://github.com/Vanilla-OS/apx>.

- Install a package in the system and initialize the container:

`sudo apx install --sys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` && apx init`

- Install package(s) in the system or install AUR package(s) inside a container:

`sudo apx install --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sys|aur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Run an installed package from AUR:

`apx --aur run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update the list of available packages in the system:

`sudo apx --sys update`

- Upgrade all installed packages in the system to their newest available version:

`sudo apx --sys upgrade`

- Remove package(s) in the system or from the AUR container:

`sudo apx --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sys|aur</span>` remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Enter the container to install packages using `apt` (Use `exit` inside the container to exit it):

`apx enter`
