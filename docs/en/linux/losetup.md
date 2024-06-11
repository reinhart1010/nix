---
layout: page
title: linux/losetup (English)
description: "Set up and control loop devices."
content_hash: 7cdb6824b57adc34c78a553b23c045f3756b9753
last_modified_at: 2024-06-11
tldri18n_status: 2
---
# losetup

Set up and control loop devices.
More information: <https://manned.org/losetup>.

- List loop devices with detailed info:

`losetup -a`

- Attach a file to a given loop device:

`sudo losetup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Attach a file to a new free loop device and scan the device for partitions:

`sudo losetup --show --partscan -f /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Attach a file to a read-only loop device:

`sudo losetup --read-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Detach all loop devices:

`sudo losetup -D`

- Detach a given loop device:

`sudo losetup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop</span>
