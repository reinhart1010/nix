---
layout: page
title: linux/userdel (English)
description: "Remove a user account or remove a user from a group."
content_hash: 7cce222d393de767dc3e82b1e0b5cf96ad0504d1
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# userdel

Remove a user account or remove a user from a group.
See also: `users`, `useradd`, `usermod`.
More information: <https://manned.org/userdel>.

- Remove a user:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user in other root directory:

`sudo userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/other/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user along with the home directory and mail spool:

`sudo userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
