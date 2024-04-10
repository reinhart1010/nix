---
layout: page
title: linux/dnf5 (English)
description: "Package management utility for RHEL, Fedora, and CentOS (it replaces dnf, which in turn replaced yum)."
content_hash: 5be33c513977c2dab9c7bb2280379a8aac8b22c7
last_modified_at: 2024-04-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf5.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf5

Package management utility for RHEL, Fedora, and CentOS (it replaces dnf, which in turn replaced yum).
DNF5 is a C++ rewrite of the DNF package manager featuring improved performance and a smaller size.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://dnf5.readthedocs.io/>.

- Upgrade installed packages to the newest available versions:

`sudo dnf5 upgrade`

- Search packages via keywords:

`dnf5 search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword1 keyword2 ...</span>

- Display details about a package:

`dnf5 info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install new packages (Note: use `-y` to confirm all prompts automatically):

`sudo dnf5 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove packages:

`sudo dnf5 remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- List installed packages:

`dnf5 list --installed`

- Find which packages provide a given command:

`dnf5 provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Remove or expire cached data:

`sudo dnf5 clean all`
