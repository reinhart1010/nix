---
layout: page
title: linux/dnf5 (English)
description: "Package management utility for RHEL, Fedora, and CentOS (it replaces dnf, which in turn replaced yum)."
content_hash: 0692534651e638d8f62fb898b5d6f613efe91454
last_modified_at: 2024-09-27
related_topics:
  - title: español version
    url: /es/linux/dnf5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf5

Package management utility for RHEL, Fedora, and CentOS (it replaces dnf, which in turn replaced yum).
DNF5 is a C++ rewrite of the DNF package manager featuring improved performance and a smaller size.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://dnf5.readthedocs.io>.

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
