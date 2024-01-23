---
layout: page
title: linux/switch_root (English)
description: "Use a different filesystem as the root of the mount tree."
content_hash: c55c1342270ca7d80a695b9e81287a4bc61e5531
last_modified_at: 2024-01-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/switch_root.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># switch_root

Use a different filesystem as the root of the mount tree.
NOTE: switch_root will fail to function if the new root is not the root of a mount. Use bind-mounting as a workaround.
See also: `chroot`, `mount`.
More information: <https://manned.org/switch_root.8>.

- Move `/proc`, `/dev`, `/sys` and `/run` to the specified filesystem, use this filesystem as the new root and start the specified init process:

`switch_root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/sbin/init</span>

- Display help:

`switch_root -h`
