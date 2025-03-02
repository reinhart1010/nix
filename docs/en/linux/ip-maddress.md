---
layout: page
title: linux/ip-maddress (English)
description: "Manage multicast addresses."
content_hash: a6e2134b2c6bd469519906aed6385b68a364e26f
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/ip-maddress.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip maddress

Manage multicast addresses.
More information: <https://manned.org/ip-maddress>.

- List multicast addresses and how many programs are subscribed to them:

`ip maddress`

- List device specific addresses:

`ip maddress show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Join a multicast group statically:

`sudo ip maddress add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33:33:00:00:00:02</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Leave a static multicast group:

`sudo ip maddress delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33:33:00:00:00:02</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>
