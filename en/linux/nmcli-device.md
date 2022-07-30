---
layout: page
title: linux/nmcli-device (English)
description: "Hardware device management with NetworkManager."
content_hash: 51987e7c407ea82732917b328f756d1107387a99
related_topics:
  - title: Türkçe version
    url: /tr/linux/nmcli-device.html
    icon: bi bi-globe
---
# nmcli device

Hardware device management with NetworkManager.
This subcommand can also be called with `nmcli d`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Print the statuses of all network interfaces:

`nmcli device status`

- Print the available Wi-Fi access points:

`nmcli device wifi`

- Connect to the Wi-Fi network with a specified name and password:

`nmcli device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>` password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Print password and QR code for the current Wi-Fi network:

`nmcli device wifi show-password`
