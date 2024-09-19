---
layout: page
title: linux/setsebool (English)
description: "Set SELinux boolean value."
content_hash: ad3ae83049057eb23875650cae823a0473bde40e
last_modified_at: 2024-09-19
tldri18n_status: 2
---
# setsebool

Set SELinux boolean value.
See also: `semanage-boolean`, `getsebool`.
More information: <https://manned.org/setsebool>.

- Show the current setting of [a]ll booleans:

`getsebool -a`

- Set or unset a boolean temporarily (non-persistent across reboot):

`sudo setsebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_can_network_connect</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|true|on|0|false|off</span>

- Set or unset a boolean [p]ersistently:

`sudo setsebool -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_use_devices</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|true|on|0|false|off</span>

- Set or unset multiple booleans [p]ersistently at once:

`sudo setsebool -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftpd_use_fusefs=1 mount_anyfile=0 ...</span>

- Set or unset a boolean persistently (alternative method using `semanage-boolean`):

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>
