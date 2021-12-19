---
layout: page
title: linux/synopkg (English)
description: "Package management utility for Synology DiskStation Manager."
content_hash: 46433f862d699906ae3ca4c7db7bd10b5edf6610
---
# synopkg

Package management utility for Synology DiskStation Manager.
More information: <https://www.synology.com/dsm>.

- List the names of installed packages:

`synopkg list --name`

- List packages which depend on a specific package:

`synopkg list --depend-on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Start/Stop a package:

`sudo synopkg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Print the status of a package:

`synopkg status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall a package:

`sudo synopkg uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Check if updates are available for a package:

`synopkg checkupdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all packages to the latest version:

`sudo synopkg upgradeall`

- Install a package from a synopkg file:

`sudo synopkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.spk</span>
