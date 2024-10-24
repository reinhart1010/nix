---
layout: page
title: linux/init (English)
description: "Linux run level manager."
content_hash: 62ca0b08b308cd722c70a2f77f526ce5fb09db6c
last_modified_at: 2024-10-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># init

Linux run level manager.
Requires the SYSVINIT compile-time option to be enabled if using systemd.
More information: <https://manned.org/man/init.8>.

- Set the system to run a graphical environment:

`sudo init 5`

- Set the system to run multiuser terminal:

`sudo init 3`

- Shut down the system:

`init 0`

- Reboot the system:

`init 6`

- Set the system to run on terminal with only root user allowed and no networking:

`sudo init 1`
