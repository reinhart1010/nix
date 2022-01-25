---
layout: page
title: linux/yum (English)
description: "Package management utility for RHEL, Fedora, and CentOS (for older versions)."
content_hash: da7836e216afdf950cdf7f319357eeeaad8105ea
related_topics:
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
---
# yum

Package management utility for RHEL, Fedora, and CentOS (for older versions).
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
