---
layout: page
title: linux/parted (English)
description: "A partition manipulation program."
content_hash: dd1e9d074bc00973a306b926086eb31afa2301a9
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/parted.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/parted.html
    icon: bi bi-globe
tldri18n_status: 2
---
# parted

A partition manipulation program.
See also: `partprobe`.
More information: <https://www.gnu.org/software/parted/parted.html>.

- List partitions on all block devices:

`sudo parted --list`

- Start interactive mode with the specified disk selected:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Create a new partition table of the specified label-type:

`sudo parted --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` mklabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun</span>

- Show partition information in interactive mode:

`print`

- Select a disk in interactive mode:

`select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Create a 16 GB partition with the specified filesystem in interactive mode:

`mkpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|logical|extended</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16G</span>

- Resize a partition in interactive mode:

`resizepart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_position_of_partition</span>

- Remove a partition in interactive mode:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
