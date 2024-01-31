---
layout: page
title: osx/airport (English)
description: "Wireless network configuration utility."
content_hash: f4522d914de10ce23d9ec6bc0b7b003a4233e2ed
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/airport.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/airport.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/airport.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/airport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airport

Wireless network configuration utility.
More information: <https://keith.github.io/xcode-man-pages/airport.1.html>.

- Show current wireless status information:

`airport --getinfo`

- Sniff wireless traffic on channel 1:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Scan for available wireless networks:

`airport --scan`

- Disassociate from current airport network:

`sudo airport --disassociate`
