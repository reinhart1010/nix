---
layout: page
title: linux/pro (English)
description: "Manage Ubuntu Pro services."
content_hash: 28cf7ad12d37cb5e91b5250dc0f41ba301b03f3d
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# pro

Manage Ubuntu Pro services.
More information: <https://manned.org/ubuntu-advantage.1>.

- Connect your system to the Ubuntu Pro support contract:

`sudo pro attach`

- Display the status of Ubuntu Pro services:

`pro status`

- Check if the system is affected by a specific vulnerability (and apply a fix if possible):

`pro fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CVE-number</span>

- Display the number of unsupported packages:

`pro security-status`

- List packages that are no longer available for download:

`pro security-status --unavailable`

- List third-party packages:

`pro security-status --thirdparty`
