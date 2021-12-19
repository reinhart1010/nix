---
layout: page
title: linux/ifup (English)
description: "Tool used to enable network interfaces."
content_hash: 1eefad094f7da8675474f0da214ea1785a58493c
related_topics:
  - title: français version
    url: /fr/linux/ifup.html
    icon: bi bi-globe
---
# ifup

Tool used to enable network interfaces.
More information: <https://manpages.debian.org/latest/ifupdown/ifup.8.html>.

- Enable interface eth0:

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Enable all the interfaces defined with "auto" in `/etc/network/interfaces`:

`ifup -a`
