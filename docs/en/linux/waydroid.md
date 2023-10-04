---
layout: page
title: linux/waydroid (English)
description: "A container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu."
content_hash: 14b7003b50f009da5b280ae4d1038aaef9d9b8e2
last_modified_at: 2023-10-04
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># waydroid

A container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu.
More information: <https://docs.waydro.id>.

- Start Waydroid:

`waydroid`

- Initialize Waydroid (required on first run or after reinstalling Android):

`waydroid init`

- Install a new Android app from a file:

`waydroid app install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.apk</span>

- Launch an Android app by its package name:

`waydroid app launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Start or stop the Waydroid session:

`waydroid session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>

- Manage the Waydroid container:

`waydroid container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|freeze|unfreeze</span>
