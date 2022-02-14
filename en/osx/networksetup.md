---
layout: page
title: osx/networksetup (English)
description: "Configuration tool for Network System Preferences."
content_hash: 6e21e39c645775ea36afdaf20d57265d8b637b45
related_topics:
  - title: 中文 version
    url: /zh/osx/networksetup.html
    icon: bi bi-globe
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

`networksetup -setairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Airport Network SSID</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
