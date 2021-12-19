---
layout: page
title: linux/wpa_cli (English)
description: "Add and configure wlan interfaces."
content_hash: 1801b00e7b52bfcfc704a4e9e84c4b935edf917b
---
# wpa_cli

Add and configure wlan interfaces.

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
