---
layout: page
title: common/dhcpig (English)
description: "Initiates an advanced DHCP exhaustion attack and stress test."
content_hash: 3081cb45936f56a89fd258bcd9319a25726d1299
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# dhcpig

Initiates an advanced DHCP exhaustion attack and stress test.
DHCPig needs to be run with root privileges.
More information: <https://github.com/kamorin/DHCPig>.

- Exhaust all of the available DHCP addresses using the specified interface:

`sudo ./pig.py `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Exhaust IPv6 addresses using eth1 interface:

`sudo ./pig.py -6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Send fuzzed/malformed data packets using the interface:

`sudo ./pig.py --fuzz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Enable color output:

`sudo ./pig.py -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Enable minimal verbosity and color output:

`sudo ./pig.py -c --verbosity=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Use a debug verbosity of 100 and scan network of neighboring devices using ARP packets:

`sudo ./pig.py -c --verbosity=100 --neighbors-scan-arp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>

- Enable printing lease information, attempt to scan and release all neighbor IP addresses:

`sudo ./pig.py --neighbors-scan-arp -r --show-options `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth1</span>
