---
layout: page
title: windows/tracert (English)
description: "Receive information about each step in the route between your PC and the target."
content_hash: 1c9cdb6e82df0fb11044e4295f96c8aa6902a2f6
last_modified_at: 2023-04-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tracert

Receive information about each step in the route between your PC and the target.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>.

- Trace a route:

`tracert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- Prevent `tracert` from resolving IP addresses to hostnames:

`tracert /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- Force `tracert` to use IPv4 only:

`tracert /4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- Force `tracert` to use IPv6 only:

`tracert /6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- Specify the maximum number of hops in the search for the target:

`tracert /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_hops</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- Display help:

`tracert /?`
