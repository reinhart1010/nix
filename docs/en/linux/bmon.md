---
layout: page
title: linux/bmon (English)
description: "Monitor bandwidth and capture network related statistics."
content_hash: 8182082bf9586fbb18fdd81abdce10458880145c
last_modified_at: 2024-02-09
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/bmon.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bmon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bmon

Monitor bandwidth and capture network related statistics.
More information: <https://github.com/tgraf/bmon>.

- Display the list of all the interfaces:

`bmon -a`

- Display data transfer rates in bits per second:

`bmon -b`

- Specify the policy to define which network interface(s) is/are displayed:

`bmon -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_1,interface_2,interface_3</span>

- Specify the interval (in seconds) in which rate per counter is calculated:

`bmon -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.0</span>
