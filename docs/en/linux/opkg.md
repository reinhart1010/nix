---
layout: page
title: linux/opkg (English)
description: "A lightweight package manager used to install OpenWrt packages."
content_hash: 9af4d9c086727f05dd34806ffd69ecbf2cf183ce
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/opkg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/opkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opkg

A lightweight package manager used to install OpenWrt packages.
More information: <https://openwrt.org/docs/guide-user/additional-software/opkg>.

- Install a package:

`opkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`opkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update the list of available packages:

`opkg update`

- Upgrade one or more specific package(s):

`opkg upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package(s)</span>

- Display information for a specific package:

`opkg info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List all the available packages:

`opkg list`

- Find out which package owns a file:

`opkg search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- List all files belonging to a package:

`opkg files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
