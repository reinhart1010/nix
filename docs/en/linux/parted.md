---
layout: page
title: linux/parted (English)
description: "A partition manipulation program."
content_hash: bc3384a1333fc6a95d0b1c1128824f37521f528e
last_modified_at: 2025-03-02
related_topics:
  - title: हिन्दी version
    url: /hi/linux/parted.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/parted.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/parted.html
    icon: bi bi-globe
tldri18n_status: 2
---
# parted

A partition manipulation program.
See also: `parted-interactive`, `partprobe`.
More information: <https://www.gnu.org/software/parted/parted.html>.

- List partitions on all block devices:

`sudo parted --list`

- Create a new partition table of the specified label-type:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` --script mklabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun</span>

- Create a new `gpt` partition table with a 500MiB boot partition and give the rest for the system partition:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` --script mklabel gpt mkpart primary 0% 500MiB mkpart primary 500MiB 100%`

- Start interactive mode with the specified disk selected:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
