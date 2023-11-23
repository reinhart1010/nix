---
layout: page
title: linux/systemd-dissect (English)
description: "Introspect and interact with file system OS disk images, specifically Discoverable Disk Images (DDIs)."
content_hash: 28f5824f640d6698c67422247f453ccf3e70f170
last_modified_at: 2023-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-dissect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-dissect

Introspect and interact with file system OS disk images, specifically Discoverable Disk Images (DDIs).
More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- Show general image information about the OS image:

`systemd-dissect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.raw</span>

- Mount an OS image:

`systemd-dissect --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.raw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/image</span>

- Unmount an OS image:

`systemd-dissect --umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/image</span>

- List files in an image:

`systemd-dissect --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.raw</span>

- Attach an OS image to an automatically allocated loopback block device and print its path:

`systemd-dissect --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.raw</span>

- Detach an OS image from a loopback block device:

`systemd-dissect --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>
