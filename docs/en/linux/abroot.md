---
layout: page
title: linux/abroot (English)
description: "Utility providing full immutability and atomicity by transacting between 2 root partition states (A⟺B)."
content_hash: 5b263d451ccd3ffdd9ba183f837cd63e543d22e3
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/linux/abroot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abroot

Utility providing full immutability and atomicity by transacting between 2 root partition states (A⟺B).
Updates are performed using OCI images, to ensure that the system is always in a consistent state.
More information: <https://github.com/Vanilla-OS/ABRoot>.

- Add packages to the local image (Note: after executing this command, you need to apply these changes.):

`sudo abroot pkg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove packages from the local image (Note: after executing this command, you need to apply these changes.):

`sudo abroot pkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List packages in the local image:

`sudo abroot pkg list`

- Apply changes in the local image (Note: you need to reboot your system for these changes to be applied):

`sudo abroot pkg apply`

- Rollback your system to previous state:

`sudo abroot rollback`

- Edit/View kernel parameters:

`sudo abroot kargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edit|show</span>

- Display status:

`sudo abroot status`

- Display help:

`abroot --help`
