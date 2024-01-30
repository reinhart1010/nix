---
layout: page
title: linux/waydroid (English)
description: "A container-based approach to boot a full Android system on a regular Linux system like Ubuntu."
content_hash: f2c7d440d46a6051c0272b6f3ae19d22760fe387
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# waydroid

A container-based approach to boot a full Android system on a regular Linux system like Ubuntu.
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
