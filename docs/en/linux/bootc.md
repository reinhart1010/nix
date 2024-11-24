---
layout: page
title: linux/bootc (English)
description: "Boot and upgrade via container images."
content_hash: fc570445c8c6617eae368c7e099707a4e3d88dcf
last_modified_at: 2024-11-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bootc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bootc

Boot and upgrade via container images.
Manages transactional, in-place operating system updates using OCI/Docker container images.
More information: <https://containers.github.io/bootc/>.

- Show deployments in the order they will appear in the bootloader:

`bootc status`

- Check if any updates are available:

`bootc upgrade --check`

- Prepare a new update and reboot into it:

`bootc upgrade --apply`

- Change OS base to new container image:

`bootc switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Reboot into the previous ostree deployment:

`bootc rollback`
