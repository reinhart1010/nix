---
layout: page
title: linux/ifup (English)
description: "Enable network interfaces."
content_hash: a3cd13b824f827c8d870c9ecf8f208fb29899d67
last_modified_at: 2024-09-18
related_topics:
  - title: français version
    url: /fr/linux/ifup.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ifup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifup

Enable network interfaces.
More information: <https://manned.org/ifup.8>.

- Enable interface eth0:

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Enable all the interfaces defined with "auto" in `/etc/network/interfaces`:

`ifup -a`
