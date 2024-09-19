---
layout: page
title: linux/grubby (English)
description: "Tool for configuring `grub` and `zipl` bootloaders."
content_hash: 25554df99694139a6ca8e5c4c0a6eb49347cdbf5
last_modified_at: 2024-09-19
related_topics:
  - title: español version
    url: /es/linux/grubby.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grubby

Tool for configuring `grub` and `zipl` bootloaders.
More information: <https://manned.org/grubby.8>.

- Add kernel boot arguments to all kernel menu entries:

`sudo grubby --update-kernel=ALL --args '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet console=ttyS0</span>`'`

- Remove existing arguments from the entry for the default kernel:

`sudo grubby --update-kernel=DEFAULT --remove-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet</span>

- List all kernel menu entries:

`sudo grubby --info=ALL`
