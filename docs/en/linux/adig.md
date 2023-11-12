---
layout: page
title: linux/adig (English)
description: "Print information received from Domain Name System (DNS) servers."
content_hash: 8bc00b16ddd1acf4f6a1970e18dd58fab1d48fe9
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/adig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adig

Print information received from Domain Name System (DNS) servers.
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
