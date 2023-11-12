---
layout: page
title: linux/ifmetric (English)
description: "An IPv4 route metrics manipulation tool."
content_hash: 37e6f8bb845bfaa5d3ea104a3a5f7bdf060064d2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ifmetric

An IPv4 route metrics manipulation tool.
More information: <https://0pointer.de/lennart/projects/ifmetric/>.

- Set the priority of the specified network interface (a higher number indicates lower priority):

`sudo ifmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Reset the priority of the specified network interface:

`sudo ifmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
