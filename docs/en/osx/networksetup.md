---
layout: page
title: osx/networksetup (English)
description: "Configuration tool for Network System Preferences."
content_hash: b3c3a6edf610567d9bc89062cedb6283fd523c55
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/osx/networksetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# networksetup

Configuration tool for Network System Preferences.
More information: <https://support.apple.com/guide/remote-desktop/about-networksetup-apdd0c5a2d5/mac>.

- List available network service providers (Ethernet, Wi-Fi, Bluetooth, etc):

`networksetup -listallnetworkservices`

- Show network settings for a particular networking device:

`networksetup -getinfo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Wi-Fi</span>`"`

- Get currently connected Wi-Fi network name (Wi-Fi device usually en0 or en1):

`networksetup -getairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>

- Connect to a particular Wi-Fi network:

`networksetup -setairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Airport Network SSID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
