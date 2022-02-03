---
layout: page
title: linux/bluetoothctl (English)
description: "Manage Bluetooth devices from the command-line."
content_hash: 371666eb23759dd153614b0d19621f6485ad3526
related_topics:
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothctl.html
    icon: bi bi-globe
---
# bluetoothctl

Manage Bluetooth devices from the command-line.
More information: <https://bitbucket.org/serkanp/bluetoothctl>.

- Enter the `bluetoothctl` shell:

`bluetoothctl`

- List all known devices:

`bluetoothctl devices`

- Power the Bluetooth controller on or off:

`bluetoothctl power `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Pair with a device:

`bluetoothctl pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Remove a device:

`bluetoothctl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Connect to a paired device:

`bluetoothctl connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Disconnect from a paired device:

`bluetoothctl disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Display help:

`bluetoothctl help`
