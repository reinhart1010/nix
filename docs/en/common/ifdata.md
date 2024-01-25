---
layout: page
title: common/ifdata (English)
description: "Display information about a network interface."
content_hash: 97384f2345b100a3a61ac89fbceffe7cf2cbb2c7
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# ifdata

Display information about a network interface.
More information: <https://joeyh.name/code/moreutils/>.

- Display the whole configuration of the specified interface:

`ifdata -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Indicate the [e]xistence of the specified interface via the exit code:

`ifdata -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display the IPv4 [a]dress and the [n]etmask of the specified interface:

`ifdata -pa -pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display the [N]etwork adress, the [b]roadcast adress, and the MTU of the specified interface:

`ifdata -pN -pb -pm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Display help:

`ifdata`
