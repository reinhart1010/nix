---
layout: page
title: common/cidr (English)
description: "Simplifies IPv4/IPv6 CIDR network prefix management with counting, overlap checking, explanation, and subdivision."
content_hash: 80653c36160d9dc707bf5eadfdffca488f8ad680
last_modified_at: 2024-12-17
tldri18n_status: 2
---
# cidr

Simplifies IPv4/IPv6 CIDR network prefix management with counting, overlap checking, explanation, and subdivision.
More information: <https://github.com/bschaatsbergen/cidr>.

- Explain a CIDR range:

`cidr explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>

- Check whether an address belongs to a CIDR range:

`cidr contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.14.5</span>

- Get a count of all addresses in a CIDR range:

`cidr count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>

- Check whether two CIDR ranges overlap:

`cidr overlaps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.14.0/22</span>

- Divide a CIDR range into a specific number of networks:

`cidr divide `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>
