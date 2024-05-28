---
layout: page
title: linux/togglesebool (English)
description: "Flip the current (non-persistent) values of SELinux booleans."
content_hash: d0ba9f6e6798cbc809632a162a7f4ff34d3dba68
last_modified_at: 2024-05-28
tldri18n_status: 2
---
# togglesebool

Flip the current (non-persistent) values of SELinux booleans.
Note: This tool has been deprecated and often removed in favor of `setsebool`.
More information: <https://manned.org/man/togglesebool>.

- Flip the current (non-persistent) values of the specified booleans:

`sudo togglesebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virt_use_samba virt_use_usb ...</span>
