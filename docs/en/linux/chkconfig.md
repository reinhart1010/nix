---
layout: page
title: linux/chkconfig (English)
description: "Manage the runlevel of services on CentOS 6."
content_hash: ed988604d7d27e0c5fe822b410e022d58b8988a4
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/chkconfig.html
    icon: bi bi-globe
---
# chkconfig

Manage the runlevel of services on CentOS 6.
More information: <https://manned.org/chkconfig>.

- List services with runlevel:

`chkconfig --list`

- Show a service's runlevel:

`chkconfig --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>

- Enable service at boot:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- Enable service at boot for runlevels 2, 3, 4, and 5:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2345</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- Disable service at boot:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`

- Disable service at boot for runlevel 3:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`
