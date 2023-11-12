---
layout: page
title: linux/sfill (English)
description: "Securely overwrite the free space and inodes of the partition where the specified directory resides."
content_hash: 524985998d00eb45512cc0745a06a4bcdb37ee5b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sfill

Securely overwrite the free space and inodes of the partition where the specified directory resides.
More information: <https://manned.org/sfill>.

- Overwrite free space and inodes of a disk with 38 writes (slow but secure):

`sfill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mounted_disk_directory</span>

- Overwrite free space and inodes of a disk with 6 writes (fast but less secure) and show status:

`sfill -l -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mounted_disk_directory</span>

- Overwrite free space and inodes of a disk with 1 write (very fast but insecure) and show status:

`sfill -ll -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mounted_disk_directory</span>

- Overwrite only free space of a disk:

`sfill -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mounted_disk_directory</span>

- Overwrite only free inodes of a disk:

`sfill -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mounted_disk_directory</span>
