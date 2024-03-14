---
layout: page
title: linux/groupmod (English)
description: "Modify existing user groups in the system."
content_hash: cf2238eb685939df1d6768ec6df67e5cad6c1882
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# groupmod

Modify existing user groups in the system.
See also: `groups`, `groupadd`, `groupdel`.
More information: <https://manned.org/groupmod>.

- Change the group name:

`sudo groupmod --new-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Change the group ID:

`sudo groupmod --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>
