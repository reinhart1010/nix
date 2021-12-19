---
layout: page
title: linux/zypper (English)
description: "SUSE & openSUSE package management utility."
content_hash: 951a5d45f37de0056a24b4289ade5f096e3a73e3
related_topics:
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
---
# zypper

SUSE & openSUSE package management utility.
More information: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronize list of packages and versions available:

`zypper refresh`

- Install a new package:

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade installed packages to the newest available versions:

`zypper update`

- Search package via keyword:

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Show information related to configured repositories:

`zypper repos --sort-by-priority`
