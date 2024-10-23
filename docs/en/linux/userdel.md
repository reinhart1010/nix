---
layout: page
title: linux/userdel (English)
description: "Remove a user account or remove a user from a group."
content_hash: 1ead7fdf842eb3a2d989ff234aaa0fc870c7a000
last_modified_at: 2024-10-23
related_topics:
  - title: català version
    url: /ca/linux/userdel.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/userdel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdel

Remove a user account or remove a user from a group.
See also: `users`, `useradd`, `usermod`.
More information: <https://manned.org/userdel>.

- Remove a user:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user in other root directory:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-R|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/other/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user along with the home directory and mail spool:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
