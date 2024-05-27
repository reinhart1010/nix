---
layout: page
title: linux/getsebool (English)
description: "Get SELinux boolean value."
content_hash: 95a3c0afbbda2119c5e7fd4d0d09f6ffefdfa15b
last_modified_at: 2024-05-27
tldri18n_status: 2
---
# getsebool

Get SELinux boolean value.
See also: `semanage-boolean`, `setsebool`.
More information: <https://manned.org/man/getsebool>.

- Show the current setting of a boolean:

`getsebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_can_connect_ftp</span>

- Show the current setting of [a]ll booleans:

`getsebool -a`

- Show the current setting of all booleans with explanations:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>
