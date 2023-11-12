---
layout: page
title: linux/wpa_cli (English)
description: "Add and configure wlan interfaces."
content_hash: 03db642a6a5226d87d866eca198bcb2b9c89eb56
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/wpa_cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wpa_cli

Add and configure wlan interfaces.
More information: <https://manned.org/wpa_cli>.

- Scan for available networks:

`wpa_cli scan`

- Show scan results:

`wpa_cli scan_results`

- Add a network:

`wpa_cli add_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Set a network's SSID:

`wpa_cli set_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` ssid "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSID</span>`"`

- Enable network:

`wpa_cli enable_network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Save config:

`wpa_cli save_config`
