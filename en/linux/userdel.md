---
layout: page
title: linux/userdel (English)
description: "Remove a user account or remove a user from a group."
content_hash: 44f1173b0e90cd220af99f454facbc9ec7a5debd
related_topics:
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
---
# userdel

Remove a user account or remove a user from a group.
Note: all commands must be executed as root.
More information: <https://manned.org/userdel>.

- Remove a user:

`userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Remove a user along with their home directory and mail spool:

`userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Remove a user from a group:

`userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- Remove a user in other root directory:

`userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/other/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
