---
layout: page
title: linux/togglesebool (English)
description: "Flip the current (non-persistent) values of SELinux booleans."
content_hash: 88cb5048cb04914a6a3309658a541b0a329bfb77
last_modified_at: 2024-09-19
tldri18n_status: 2
---
# togglesebool

Flip the current (non-persistent) values of SELinux booleans.
Note: This tool has been deprecated and often removed in favor of `setsebool`.
More information: <https://manned.org/togglesebool>.

- Flip the current (non-persistent) values of the specified booleans:

`sudo togglesebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virt_use_samba virt_use_usb ...</span>
