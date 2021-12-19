---
layout: page
title: linux/brctl (English)
description: "Ethernet bridge administration."
content_hash: e3ffe0b75c00e8ef8a03e1759ef2d84466bf6fef
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/brctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brctl.html
    icon: bi bi-globe
---
# brctl

Ethernet bridge administration.
More information: <https://manned.org/brctl>.

- Show a list with information about currently existing Ethernet bridges:

`sudo brctl show`

- Create a new Ethernet bridge interface:

`sudo brctl add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bridge_name</span>

- Delete an existing Ethernet bridge interface:

`sudo brctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bridge_name</span>

- Add an interface to an existing bridge:

`sudo brctl addif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bridge_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>

- Remove an interface from an existing bridge:

`sudo brctl delif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bridge_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>
