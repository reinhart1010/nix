---
layout: page
title: linux/e2freefrag (English)
description: "Print the free space fragmentation information for ext2/ext3/ext4 filesystems."
content_hash: 51aaa06cd2612e07cbd110350dce57eb25746b40
---
# e2freefrag

Print the free space fragmentation information for ext2/ext3/ext4 filesystems.
More information: <https://manned.org/e2freefrag>.

- Check how many free blocks are present as contiguous and aligned free space:

`e2freefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Specify chunk size in kilobytes to print how many free chunks are available:

`e2freefrag -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chunk_size_in_kb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
