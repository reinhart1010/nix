---
layout: page
title: linux/mkfs.fat (English)
description: "Create an MS-DOS filesystem inside a partition."
content_hash: c08dbd9dad27f3c3ac80997a5185297963b574ad
last_modified_at: 2024-04-18
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.fat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.fat

Create an MS-DOS filesystem inside a partition.
More information: <https://manned.org/mkfs.fat>.

- Create a fat filesystem inside partition 1 on device b (`sdb1`):

`mkfs.fat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-name:

`mkfs.fat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-id:

`mkfs.fat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Use 5 instead of 2 file allocation tables:

`mkfs.fat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
