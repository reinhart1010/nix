---
layout: page
title: linux/wol (English)
description: "Client for sending Wake-on-LAN magic packets."
content_hash: f7947f3b9d691ac0509f5d4e7ccfe2bde06d4419
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wol

Client for sending Wake-on-LAN magic packets.
More information: <https://sourceforge.net/projects/wake-on-lan/>.

- Send a WoL packet to a device:

`wol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Send a WoL packet to a device in another subnet based on its IP:

`wol --ipaddr=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Send a WoL packet to a device in another subnet based on its hostname:

`wol --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Send a WoL packet to a specific port on a host:

`wol --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>

- Read hardware addresses, IP addresses/hostnames, optional ports and SecureON passwords from a file:

`wol --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Turn on verbose output:

`wol --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>
