---
layout: page
title: linux/ipset (English)
description: "Create IP sets for firewall rules."
content_hash: e12c9c2626963d97fe17f00533427724d4fc0735
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# ipset

Create IP sets for firewall rules.
More information: <https://manned.org/ipset>.

- Create an empty IP set which will contain IP addresses:

`ipset create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_name</span>` hash:ip`

- Destroy a specific IP set:

`ipset destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_name</span>

- Add an IP address to a specific set:

`ipset add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.25</span>

- Delete a specific IP address from a set:

`ipset del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.25</span>

- Save an IP set:

`ipset save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set_name</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ip_set</span>
