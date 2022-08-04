---
layout: page
title: linux/groupmod (English)
description: "Modify existing user groups in the system."
content_hash: 5ae8a480fde61d6251dc8c2032b4c4960422baaa
---
# groupmod

Modify existing user groups in the system.
See also: `groups`, `groupadd`, `groupdel`.
More information: <https://manned.org/groupmod>.

- Change the group name:

`sudo groupmod --new-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Change the group id:

`sudo groupmod --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>
