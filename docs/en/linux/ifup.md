---
layout: page
title: linux/ifup (English)
description: "Enable network interfaces."
content_hash: 5865ca07b8be5434da5ecf8904f37e911a65dab8
last_modified_at: 2024-02-15
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
More information: <https://manpages.debian.org/latest/ifupdown/ifup.8.html>.

- Enable interface eth0:

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Enable all the interfaces defined with "auto" in `/etc/network/interfaces`:

`ifup -a`
