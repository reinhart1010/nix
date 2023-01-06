---
layout: page
title: linux/adig (English)
description: "Prints information received from Domain Name System (DNS) servers."
content_hash: 91ef093b109588df456daf4ebe661eed653151e8
last_modified_at: 2023-01-06
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/adig.html
    icon: bi bi-globe
---
# adig

Prints information received from Domain Name System (DNS) servers.
More information: <https://manned.org/adig>.

- Display A (default) record from DNS for hostname(s):

`adig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Display extra [d]ebugging output:

`adig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Connect to a specific DNS [s]erver:

`adig -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a specific TCP port to connect to a DNS server:

`adig -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Use a specific UDP port to connect to a DNS server:

`adig -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
