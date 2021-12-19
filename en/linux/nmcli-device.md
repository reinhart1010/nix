---
layout: page
title: linux/nmcli-device (English)
description: "Hardware device management with NetworkManager."
content_hash: 532edbfc5522cdc11422a0983a6b3a46591c14f6
---
# nmcli device

Hardware device management with NetworkManager.
More information: <https://man.archlinux.org/man/nmcli.1>.

- Print the statuses of all network interfaces:

`nmcli device status`

- Print the available Wi-Fi access points:

`nmcli device wifi`

- Connect to the Wi-Fi network with a specified name and password:

`nmcli device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>` password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Print password and QR code for the current Wi-Fi network:

`nmcli device wifi show-password`
