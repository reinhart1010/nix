---
layout: page
title: linux/nmcli-device (English)
description: "Manage network interfaces and establish new Wi-Fi connections using NetworkManager."
content_hash: 1cbdac62e952af639b52cb23cf5bfba8af594342
last_modified_at: 2023-08-02
related_topics:
  - title: Türkçe version
    url: /tr/linux/nmcli-device.html
    icon: bi bi-globe
---
# nmcli device

Manage network interfaces and establish new Wi-Fi connections using NetworkManager.
This subcommand can also be called with `nmcli d`.
More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Print the statuses of all network interfaces:

`nmcli device status`

- Print the available Wi-Fi access points:

`nmcli device wifi`

- Connect to a Wi-Fi network with the specified SSID (you will be prompted for a password):

`nmcli --ask device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>

- Print the password and QR code for the current Wi-Fi network:

`nmcli device wifi show-password`
