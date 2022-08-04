---
layout: page
title: linux/hcitool (English)
description: "Monitor, configure connections, and send special commands to Bluetooth devices."
content_hash: e2e8e6a16c345274fb6a932f40aeadea15ca1cc7
---
# hcitool

Monitor, configure connections, and send special commands to Bluetooth devices.
More information: <https://manned.org/hcitool>.

- Scan for Bluetooth devices:

`hcitool scan`

- Output the name of a device, returning its MAC address:

`hcitool name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- Fetch information about a remote Bluetooth device:

`hcitool info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- Check the link quality to a Bluetooth device:

`hcitool lq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- Modify the transmit power level:

`hcitool tpl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>

- Display the link policy:

`hcitool lp`

- Request authentication with a specific device:

`hcitool auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bdaddr</span>

- Display local devices:

`hcitool dev`
