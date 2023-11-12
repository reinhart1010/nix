---
layout: page
title: common/l2ping (English)
description: "Send an L2CAP echo request and receive an answer."
content_hash: 06172deaa854bfa1869a98938267c99a5818a772
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# l2ping

Send an L2CAP echo request and receive an answer.
More information: <https://manned.org/l2ping>.

- Ping a Bluetooth device:

`sudo l2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Reverse ping a Bluetooth device:

`sudo l2ping -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Ping a Bluetooth device from a specified interface:

`sudo l2ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hci0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Ping Bluetooth device with a specified sized data package:

`sudo l2ping -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">byte_count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Ping flood a Bluetooth device:

`sudo l2ping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Ping a Bluetooth device a specified amount of times:

`sudo l2ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amount</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Ping a Bluetooth device with a specified delay between requests:

`sudo l2ping -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>
