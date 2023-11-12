---
layout: page
title: linux/pamac (English)
description: "A command-line utility for the GUI package manager pamac."
content_hash: 81dd2f3ae4e1e8d7e9044d7aa2b9ef2806d00555
last_modified_at: 2023-11-12
related_topics:
  - title: українська version
    url: /uk/linux/pamac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamac

A command-line utility for the GUI package manager pamac.
If you can't see the AUR packages, enable it in `/etc/pamac.conf` or in the GUI.
More information: <https://wiki.manjaro.org/index.php/Pamac>.

- Install a new package:

`pamac install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and its no longer required dependencies (orphans):

`pamac remove --orphans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search the package database for a package:

`pamac search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List installed packages:

`pamac list --installed`

- Check for package updates:

`pamac checkupdates`

- Upgrade all packages:

`pamac upgrade`
