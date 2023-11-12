---
layout: page
title: linux/ahost (English)
description: "DNS lookup utility to display the A or AAAA record linked with a hostname or IP address."
content_hash: 61f39f5d2767294437058708030ea5adf47c6e31
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/ahost.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ahost

DNS lookup utility to display the A or AAAA record linked with a hostname or IP address.
More information: <https://manned.org/ahost>.

- Print an `A` or `AAAA` record associated with a hostname or IP address:

`ahost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Display some extra debugging output:

`ahost -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Display the record with a specified type:

`ahost -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|u</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
