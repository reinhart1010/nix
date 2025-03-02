---
layout: page
title: linux/mknod (English)
description: "Create block or character device special files."
content_hash: 7ce1ed7daa412516286bb093350e49aa261a0bd3
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/mknod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mknod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mknod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mknod

Create block or character device special files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- Create a block device:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">major_device_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minor_device_number</span>

- Create a character device:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">major_device_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minor_device_number</span>

- Create a FIFO (queue) device:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` p`

- Create a device file with default SELinux security context:

`sudo mknod -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">major_device_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minor_device_number</span>
