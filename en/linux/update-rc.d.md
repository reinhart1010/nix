---
layout: page
title: linux/update-rc.d (English)
description: "Install and remove services which are System-V style init script links."
content_hash: a2b71c3414fc7e13b688fc8d6522a883372669b2
---
# update-rc.d

Install and remove services which are System-V style init script links.
Init scripts are in the `/etc/init.d/`.
More information: <https://manned.org/update-rc.d>.

- Install a service:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` defaults`

- Enable a service:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` enable`

- Disable a service:

`update-rc.d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` disable`

- Forcibly remove a service:

`update-rc.d -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql</span>` remove`
