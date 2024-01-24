---
layout: page
title: common/ifdata (English)
description: "Display information about a network interface."
content_hash: 97384f2345b100a3a61ac89fbceffe7cf2cbb2c7
last_modified_at: 2024-01-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ifdata.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ifdata

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
