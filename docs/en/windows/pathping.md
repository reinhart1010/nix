---
layout: page
title: windows/pathping (English)
description: "A trace route tool combining features of `ping` and `tracert`."
content_hash: 9bf3475c50737ea7ec355dc2fe4ef16dff118e5f
related_topics:
  - title: 中文 version
    url: /zh/windows/pathping.html
    icon: bi bi-globe
---
# pathping

A trace route tool combining features of `ping` and `tracert`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>.

- Ping and trace the route to a host:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Do not perform reverse lookup of IP address to hostname:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -n`

- Specify the maximum number of hops to search for the target (the default is 30):

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_hops</span>

- Specify the milliseconds to wait between pings (the default is 240):

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>

- Specify the number of queries per hop (the default is 100):

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">queries</span>

- Force IPV4 usage:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -4`

- Force IPV6 usage:

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -6`

- Display detailed usage information:

`pathping /?`
