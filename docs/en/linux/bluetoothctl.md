---
layout: page
title: linux/bluetoothctl (English)
description: "Manage Bluetooth devices."
content_hash: 38ffaf92846a33d91956e4b0650369d56bb20432
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluetoothctl

Manage Bluetooth devices.
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
