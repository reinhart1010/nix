---
layout: page
title: linux/yum (English)
description: "Package management utility for RHEL, Fedora, and CentOS (for older versions)."
content_hash: c92b22195abb9190c389b67f1d78b9f5347f0452
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/yum.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/yum.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yum

Package management utility for RHEL, Fedora, and CentOS (for older versions).
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://manned.org/yum>.

- Install a new package:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a new package and assume yes to all questions (also works with update, great for automated updates):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Find the package that provides a particular command:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Remove a package:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display available updates for installed packages:

`yum check-update`

- Upgrade installed packages to the newest available versions:

`yum upgrade`
