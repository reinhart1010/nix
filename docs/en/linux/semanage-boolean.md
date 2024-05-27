---
layout: page
title: linux/semanage-boolean (English)
description: "Manage persistent SELinux boolean settings."
content_hash: 296593b6ef3284dbdf992b78feed2964a3974040
last_modified_at: 2024-05-27
tldri18n_status: 2
---
# semanage boolean

Manage persistent SELinux boolean settings.
See also: `semanage` for managing SELinux policies, `getsebool` for checking boolean values, and `setsebool` for applying non-persistent boolean settings.
More information: <https://manned.org/man/semanage-boolean>.

- List all booleans settings:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- List all user-defined boolean settings without headings:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-C|--locallist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--noheading</span>

- Set or unset a boolean persistently:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>
