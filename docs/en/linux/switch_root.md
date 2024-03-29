---
layout: page
title: linux/switch_root (English)
description: "Use a different filesystem as the root of the mount tree."
content_hash: 196c45b66bd0bdd532baa8bcae6b5f0dc590a951
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# switch_root

Use a different filesystem as the root of the mount tree.
Note: switch_root will fail to function if the new root is not the root of a mount. Use bind-mounting as a workaround.
See also: `chroot`, `mount`.
More information: <https://manned.org/switch_root.8>.

- Move `/proc`, `/dev`, `/sys` and `/run` to the specified filesystem, use this filesystem as the new root and start the specified init process:

`switch_root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/sbin/init</span>

- Display help:

`switch_root -h`
