---
layout: page
title: linux/getsebool (English)
description: "Get SELinux boolean value."
content_hash: 70638540077b7b3cc2d752d426f837ac0eeb1c9c
last_modified_at: 2024-09-19
tldri18n_status: 2
---
# getsebool

Get SELinux boolean value.
See also: `semanage-boolean`, `setsebool`.
More information: <https://manned.org/getsebool>.

- Show the current setting of a boolean:

`getsebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_can_connect_ftp</span>

- Show the current setting of [a]ll booleans:

`getsebool -a`

- Show the current setting of all booleans with explanations:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>
