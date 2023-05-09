---
layout: page
title: linux/dnf (English)
description: "Package management utility for RHEL, Fedora, and CentOS (replaces yum)."
content_hash: a26ed68dcc6d66565b4a13a7f1655052dad0b7d9
last_modified_at: 2023-05-09
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
---
# dnf

Package management utility for RHEL, Fedora, and CentOS (replaces yum).
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://dnf.readthedocs.io>.

- Upgrade installed packages to the newest available versions:

`sudo dnf upgrade`

- Search packages via keywords:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword1 keyword2 ...</span>

- Display details about a package:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a new package (use `-y` to confirm all prompts automatically):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Remove a package:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- List installed packages:

`dnf list --installed`

- Find which packages provide a given command:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- View all past operations:

`dnf history`
