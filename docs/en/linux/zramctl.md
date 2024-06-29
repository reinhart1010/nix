---
layout: page
title: linux/zramctl (English)
description: "Setup and control zram devices."
content_hash: f15896335fc5758e7f8f6bdd761642112c80deeb
last_modified_at: 2024-06-29
related_topics:
  - title: polski version
    url: /pl/linux/zramctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zramctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zramctl

Setup and control zram devices.
Use `mkfs` or `mkswap` to format zram devices to partitions.
More information: <https://manned.org/zramctl>.

- Check if zram is enabled:

`lsmod | grep -i zram`

- Enable zram with a dynamic number of devices (use `zramctl` to configure devices further):

`sudo modprobe zram`

- Enable zram with exactly 2 devices:

`sudo modprobe zram num_devices=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Find and initialize the next free zram device to a 2 GB virtual drive using LZ4 compression:

`sudo zramctl --find --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2GB</span>` --algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lz4</span>

- List currently initialized devices:

`sudo zramctl`
