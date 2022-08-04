---
layout: page
title: linux/groupadd (English)
description: "Add user groups to the system."
content_hash: 22b4b5f659fc18376118567def31eee07577407c
---
# groupadd

Add user groups to the system.
See also: `groups`, `groupdel`, `groupmod`.
More information: <https://manned.org/groupadd>.

- Create a new group:

`sudo groupadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Create a new system group:

`sudo groupadd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Create a new group with the specific groupid:

`sudo groupadd --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>
