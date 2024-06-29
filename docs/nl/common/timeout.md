---
layout: page
title: common/timeout (Nederlands)
description: "Voer een commando uit met een tijdslimiet."
content_hash: 7547480a64795586bec0d22429d578def4005c3e
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/timeout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timeout

Voer een commando uit met een tijdslimiet.
Meer informatie: <https://www.gnu.org/software/coreutils/timeout>.

- Voer `sleep 10` uit en beëindig het na 3 seconden:

`timeout 3s sleep 10`

- Stuur een signaal naar het commando nadat de tijdslimiet is verlopen (standaard SIGTERM):

`timeout --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>
