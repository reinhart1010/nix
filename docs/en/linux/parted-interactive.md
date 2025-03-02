---
layout: page
title: linux/parted-interactive (English)
description: "A partition manipulation program."
content_hash: 46976f719bf0dec6f2679695eb81233583117076
last_modified_at: 2025-03-02
tldri18n_status: 2
---
# parted

A partition manipulation program.
See also: `partprobe`.
More information: <https://www.gnu.org/software/parted/parted.html>.

- Start interactive mode with the specified disk selected:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

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
