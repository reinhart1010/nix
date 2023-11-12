---
layout: page
title: linux/losetup (English)
description: "Set up and control loop devices."
content_hash: edf5e51e362e33513ef5b8c2ca41b42ce049b733
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# losetup

Set up and control loop devices.
More information: <https://manned.org/losetup>.

- List loop devices with detailed info:

`losetup -a`

- Attach a file to a given loop device:

`sudo losetup /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loop</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Attach a file to a new free loop device and scan the device for partitions:

`sudo losetup --show --partscan -f /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Attach a file to a read-only loop device:

`sudo losetup --read-only /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loop</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Detach all loop devices:

`sudo losetup -D`

- Detach a given loop device:

`sudo losetup -d /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loop</span>
